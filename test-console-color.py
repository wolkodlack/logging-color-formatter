#!/usr/bin/python2.7
# #!/usr/bin/python
# coding: utf-8
# Author: wolkodlack@gmail.com

# Copyright 2016 by Denis Vavrischuk. All Rights Reserved.

version_info = (0, 0, 5)

__author__ = 'wolkodlack@gmail.com'
__version__ = '.'.join(map(str, version_info))
__date__ = "$Jan 29, 2016 03:01:00 AM$"

import sys
import os

if os.path.abspath(os.path.dirname(__file__)).split('/')[-1]=='bin':
    # Subpackages integration section #############################################
    SOURCE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
    # Add library dirs into search path
    for path in [SOURCE_ROOT]:
        if not path in sys.path:
            #    sys.path.append(path)
            sys.path.insert(1, path)    # inserting path after current dir
    ###############################################################################
    from lib.logging.color import TerminalColorOut, ColorFormatter, _aColors
else:
    from color import TerminalColorOut, ColorFormatter, _aColors

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description='Checks color output feature',
                                     epilog='(c) Denis Vavrischuk')

    parser.add_argument("--check",
                        action='store_true',
                        help='Executes tests')

    args = parser.parse_args()
    ###################################################################################
    # print 'ParserArgs: ', args

    if len(sys.argv)==1:
        parser.print_usage()






    # for i in [BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]:
    #     a.colorLog('-> %i %s ' % (i, a._aColors[i]), fg=i, bg=LT_(i), ln=True)

    def checkDirectColorLog():
        a = TerminalColorOut()
        # Test of logging methods ##################
        for i in [False, True]:
            a._useFormat = i    # Switch here

            a.notice('It\'s just test NOTICE')
            a.debug('It\'s just my console-color test')
            a.info('Don\'t wonder.')
            a.warning('Can you see this?')
            a.error('How are you?')
            a.critical('Hello %username%')

            print '------ END of DirectColorLog check %s ------\n' % ('with format' if i else 'without format')

    def checkLoggingColorLog():
        import logging
        # create formatter and add it to the handlers

        logger = logging.getLogger()
        logger.setLevel(logging.NOTSET)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ## create file handler which logs even debug messages
        fh = logging.FileHandler('spam.log')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        # Example of overloading print-color-format in constructor call
        fmt = {
            logging.CRITICAL: '${asctime} <fg=white>${name} <fg=lyellow><bg=red><b>${levelname}</b><bg-cl>: ${message}<cl>',
            logging.ERROR: '${asctime} ${name} <bg=yellow><fg=black>${levelname}<cl>: <fg=lred>${message}<cl>'
        }
        fmt = 'aaa'
        _datefmt = '%y-%m-%d %H:%M:%S'
        _datefmt = '%%M:%S' # FIXME: What's going on here?

        formatter = ColorFormatter(fmt=fmt, datefmt=_datefmt)
        # Example of verloading print-color-format after contstruction
        formatter._levelMap[logging.CRITICAL] = '${asctime} <fg=white>${name} <fg=lyellow><bg=red><b>${levelname}</b><bg-cl>: ${message}<cl>'


        ## create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.NOTSET)
        ch.setFormatter(formatter)
        logger.addHandler(ch)


        logger.debug('>> debug message')
        logger.info('>> info message')
        logger.warn('>> warn message')
        logger.error('>> error message')
        logger.critical('>> critical message')

        print '------ END of LoggingColorLog check ------\n'

    def checkColorOut():
        a = TerminalColorOut()
        # # Different color checks ###################
        a.colorLog('1. just  test  test',
                   bg=_aColors['BLUE'],
                   fg=_aColors['LT_BLUE'],
                   b=True,
                   ln=True
                   )
        a.colorLog('2. just  test  ',
                   bg=_aColors['LT_BLACK'],
                   f=True,
                   ln=True
                   )
        a.colorLog('3. just test   ',
                   bg=_aColors['LT_CYAN'],
                   fg=_aColors['BLACK'],
                   i=True,
                   b=True
                   )
        a.colorLog('4. just test   \r\n',
                   bg=_aColors['BLACK'],
                   u=True,
                   b=True,
                   c=True
                   )
        print '------ END of ColorOut check ------\n'

    # Starting appropriate tests
    if args.check:
        checkDirectColorLog()
        checkLoggingColorLog()
        checkColorOut()