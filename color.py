# Copyright 2016 by Denis Vavrischuk. All Rights Reserved.

version_info = (0, 0, 5)

__author__ = 'wolkodlack@gmail.com'
__version__ = '.'.join(map(str, version_info))
__date__ = "$Jan 29, 2016 03:01:00 AM$"

def LT_(color):
    return color + 60

# Colors list
BLACK = 0
RED = 1
GREEN = 2
YELLOW = 3
BLUE = 4
MAGENTA = 5
CYAN = 6
WHITE = 7

LT_BLACK = LT_(BLACK)
LT_RED = LT_(RED)
LT_GREEN = LT_(GREEN)
LT_YELLOW = LT_(YELLOW)
LT_BLUE = LT_(BLUE)
LT_MAGENTA = LT_(MAGENTA)
LT_CYAN = LT_(CYAN)
LT_WHITE = LT_(WHITE)


import logging

import sys

from logging import CRITICAL, FATAL, ERROR, WARNING, WARN, INFO, DEBUG, NOTSET

"""
Level mapping dictionary
"""
_levelNames = logging._levelNames
# {
#     CRITICAL : 'CRITICAL',
#     ERROR : 'ERROR',
#     WARNING : 'WARNING',
#     INFO : 'INFO',
#     DEBUG : 'DEBUG',
#     NOTSET : 'NOTSET',
#     'CRITICAL' : CRITICAL,
#     'ERROR' : ERROR,
#     'WARN' : WARNING,
#     'WARNING' : WARNING,
#     'INFO' : INFO,
#     'DEBUG' : DEBUG,
#     'NOTSET' : NOTSET,
# }



"""
Log Level templates
"""
_levelMap = {
    CRITICAL:   '<fg=white>${name} <fg=lyellow><bg=red><b>${levelname}</b><bg-cl>: ${message}<cl>',
    ERROR:      '${name} <bg=yellow><fg=black>${levelname}<cl>: <fg=lred>${message}<cl>',
    WARNING:    '<f>${name}</f> <bg=magenta>${levelname}:<bg-cl> <i>${message}</i>',
    INFO:       '${name} <u>${levelname}:</u> ${message}',
    DEBUG:      '${name} <bg=green><fg=lyellow>${levelname}:<bg-cl> ${message}<cl>',
    NOTSET:     '<fg=white>${name} <bg=lblack>${levelname}:<bg-cl> <c>${message}</c><cl>',
}

"""
Color format tags mapping
"""
_tagMap = {
    '<cl>':     '\x1b[0m',       # Clear Reset
    '<b>':      '\x1b[1m',       # Bold
    '</b>':     '\x1b[22m',      # Bold-End

    '<f>':      '\x1b[2m',       # Faint
    '</f>':     '\x1b[22m',      # Faint-End.  Same as Bold-End

    '<i>':      '\x1b[3m',       # Italic
    '</i>':     '\x1b[23m',      # Italic-End

    '<u>':      '\x1b[4m',       # Underlined
    '</u>':     '\x1b[24m',       # Underlined

    '<c>':      '\x1b[9m',        # Crossed-out
    '</c>':     '\x1b[29m',       # Crossed-out-END

    '<fg=black>':   '\x1b[30m',
    '<fg=red>':    '\x1b[31m',
    '<fg=green>':   '\x1b[32m',
    '<fg=yellow>':  '\x1b[33m',
    '<fg=blue>':    '\x1b[34m',
    '<fg=magenta>': '\x1b[35m',
    '<fg=cyan>':    '\x1b[36m',
    '<fg=white>':   '\x1b[37m',

    '<fg=lblack>':   '\x1b[90m',
    '<fg=lred>':    '\x1b[91m',
    '<fg=lgreen>':   '\x1b[92m',
    '<fg=lyellow>':  '\x1b[93m',
    '<fg=lblue>':    '\x1b[94m',
    '<fg=lmagenta>': '\x1b[95m',
    '<fg=lcyan>':    '\x1b[96m',
    '<fg=lwhite>':   '\x1b[97m',

    '<fg-cl>':       '\x1b[39m',

    '<bg=black>':   '\x1b[40m',
    '<bg=red>':    '\x1b[41m',
    '<bg=green>':   '\x1b[42m',
    '<bg=yellow>':  '\x1b[43m',
    '<bg=blue>':    '\x1b[44m',
    '<bg=magenta>': '\x1b[45m',
    '<bg=cyan>':    '\x1b[46m',
    '<bg=white>':   '\x1b[47m',

    '<bg=lblack>':   '\x1b[100m',
    '<bg=lred>':    '\x1b[101m',
    '<bg=lgreen>':   '\x1b[102m',
    '<bg=lyellow>':  '\x1b[103m',
    '<bg=lblue>':    '\x1b[104m',
    '<bg=lmagenta>': '\x1b[105m',
    '<bg=lcyan>':    '\x1b[106m',
    '<bg=lwhite>':   '\x1b[107m',
    '<bg-cl>':       '\x1b[49m',
}

_aColors = {
    'BLACK':    BLACK,
    'RED':      RED,
    'GREEN':    GREEN,
    'YELLOW':   YELLOW,
    'BLUE':     BLUE,
    'MAGENTA':  MAGENTA,
    'CYAN':     CYAN,
    'WHITE':    WHITE,
    BLACK:      'BLACK',
    RED:        'RED',
    GREEN:      'GREEN',
    YELLOW:     'YELLOW',
    BLUE:       'BLUE',
    MAGENTA:    'MAGENTA',
    CYAN:       'CYAN',
    WHITE:      'WHITE',

    'LT_BLACK':  LT_BLACK,
    'LT_RED':    LT_RED,
    'LT_GREEN':  LT_GREEN,
    'LT_YELLOW': LT_YELLOW,
    'LT_BLUE':   LT_BLUE,
    'LT_MAGENTA':LT_MAGENTA,
    'LT_CYAN':   LT_CYAN,
    'LT_WHITE':  LT_WHITE,

    LT_BLACK:   'LT_BLACK',
    LT_RED:     'LT_RED',
    LT_GREEN:   'LT_GREEN',
    LT_YELLOW:  'LT_YELLOW',
    LT_BLUE:    'LT_BLUE',
    LT_MAGENTA: 'LT_MAGENTA',
    LT_CYAN:    'LT_CYAN',
    LT_WHITE:   'LT_WHITE'

}


class ColorFormatter(logging.Formatter):
    """
    ColorFormater Class
    """
    _levelMap = _levelMap
    _tagMap = _tagMap


    def __init__(self, fmt=None, datefmt=None):
        if fmt is None:
            pass
        elif isinstance(fmt, dict):
            for level in fmt:
                if level in fmt.keys():
                    _levelMap[level] = fmt[level]
        else:
            raise ValueError('Wrong format: %s' % type(fmt).__name__)

        super(ColorFormatter, self).__init__(None, datefmt)

        self.datefmt = datefmt


    def format(self, record):
        from string import Template

        record.message = record.getMessage()
        if self.usesTime():
            record.asctime = self.formatTime(record, self.datefmt)

        _fmt = self._levelMap[record.levelno]
        _fmt = self.doTagMap(_fmt)

        _tpl = Template(_fmt)
        tmlArgs = dict(record.__dict__)
        r = _tpl.substitute(tmlArgs)

        return r

    def doTagMap(self, _fmt):
        """
        Does formatting to terminal color scheme

        :param _fmt: string
        :return: string
        """
        for i in self._tagMap:
            _fmt = _fmt.replace(i, self._tagMap[i])

        return _fmt

class ColorLogger(ColorFormatter):

    _useFormat = False

    _levelMap = _levelMap
    _tagMap = _tagMap


    def _log(self, level=INFO, msg=''):
        """Log record"""
        from logging import makeLogRecord

        clInf = self.aLevelMap[level]
        clInf['ln'] = True

        rec = {
            'name':     'root',
            'levelname': _levelNames[level],
            'msg':      msg,
            'levelno':  level
        }
        logRecord = makeLogRecord(rec)
        dt = self.format(record=logRecord)

        if self._useFormat:
            print(dt)
        else:
            self.colorLog(msg, **clInf)

    def critical(self, msg):
        self._log(level=CRITICAL, msg=msg)

    def error(self, msg):
        self._log(level=ERROR, msg=msg)

    def warning(self, msg):
        self._log(level=WARNING, msg=msg)

    def info(self,msg):
        self._log(level=INFO, msg=msg)

    def debug(self, msg):
        self._log(level=DEBUG, msg=msg)

    def notice(self, msg):
        self._log(level=NOTSET, msg=msg)



class TerminalColorOut(ColorLogger):

    _aColors = _aColors

    aLevelMap = {
        CRITICAL:   {'fg': YELLOW,      'bg': RED,      'b': True     },
        ERROR:      {'fg': BLACK,       'bg': YELLOW    },
        WARNING:    {'fg': LT_YELLOW,   'bg': LT_BLACK  },
        INFO:       {'fg': BLUE,        'bg': WHITE},
        DEBUG:      {'fg': MAGENTA      },
        NOTSET:     {'fg': BLACK,       'bg': LT_BLACK  },
    }

    def getFG(self, color=WHITE, light=False):
        # if color is None:
        #     return None

        r = 90 if light else 30
        if type(color) is str:
            color = self._aColors[color]
        # sys.stdout.write('FGr: %s c: %s' % (r,color) )

        return r + color

    def getBG(self, color=WHITE, light=False):
        if color is None:
            return None

        r = 100 if light else 40
        if type(color) is str:
            color = self._aColors[color]
        # sys.stdout.write('BGr: %s c: %s' % (r,color) )

        return r + color

    def getTextSequence(self, **kwargs):
        #fg=None, bg=None, b=False, f=False, i=False, u=False, c=False):
        """
        @param fg:  ForeGround color - 30-37 | 90-97
        @param bg:  BackGround color - 40-47 | 100-107
        @param b:   bold
        @param f:   faint
        @param i:   italic
        @param u:   underlined
        @param c:   Crossed-out
        @return:
        """
        ESC = '\x1b['

        ret = []
        if not kwargs.get('fg', None) is None:
            ret.append(str(kwargs.get('fg', None)))
        if not kwargs.get('bg', None) is None:
            ret.append(str(kwargs.get('bg', None)))

        if kwargs.get('b', False) is True:
            ret.append('1')
        if kwargs.get('f', False) is True:
            ret.append('2')
        if kwargs.get('i', False) is True:
            ret.append('3')
        if kwargs.get('u', False) is True:
            ret.append('4')
        if kwargs.get('c', False) is True:
            ret.append('9')     # Crossed-out

        if len(ret) == 0:
            ret.append('0')       # No ASCI escape needed, Resetting to default
            # ret.append('49')    # Reset BackGround color
            # ret.append('39')    # Reset ForeGround color

        return ''.join([ESC, ';'.join(ret), 'm'])

    #
    def colorLog(self, msg, **kwargs ):
        # fg=WHITE, bg=None, b=False, f=False, i=False, u=False, c=False, ln=False):
        """
        @param msg:
        @param kwargs:
            @param msg: String {Message}
            @param fg:  foreground
            @param bg:  background
            @param b:   bold
            @param f:   faint
            @param i:   italic
            @param u:   underlined
            @param c:   crossed-out
            @param ln:  new line
        @return:
        """

        fg = kwargs.get('fg', WHITE)
        bg = kwargs.get('bg', None)

        kwargs['fg'] = self.getFG(fg)
        kwargs['bg'] = self.getBG(bg)

        ts = self.getTextSequence(**kwargs)
        jn = [ts, msg, self.getTextSequence()]
        if kwargs.get('ln', False):
            jn.append('\n')

        sys.stdout.write(''.join(jn))
        # sys.stdout.flush()
