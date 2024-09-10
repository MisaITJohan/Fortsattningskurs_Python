__doc__ = """Utility functions"""
__author__ = "mier"
__version__ = "0.1"
__all__ = ["debug_msg",
           "err_msg",
           "sys_msg",
           "parse_arguments"]

import argparse
import inspect
import sys


def debug_msg(*args):
    """Utility function. Prints debugging info on stderr"""
    msg = ' '.join(args)
    caller = inspect.stack()[1].function
    if caller == "<module>":
        caller = "main"
    print(f"({caller}) {msg}", file=sys.stderr)


def err_msg(*args):
    """Utility function. Prints a message on stderr"""
    msg = ' '.join(args)
    caller = inspect.stack()[1].function
    if caller == "<module>":
        caller = "main"
    print(f"({caller}) {msg}", file=sys.stderr)


def sys_msg(*args):
    """Utility function. Prints a message on stdout"""
    msg = ' '.join(args)
    caller = inspect.stack()[1].function
    if caller == "<module>":
        caller = "main"
    print(f"({caller}) {msg}", file=sys.stdout)


def parse_arguments():
    """Parse command line options and positional arguments"""
    parser = argparse.ArgumentParser(add_help=True,
                                     description="Hangman - guess the hidden word"
    )
    help_dict = {
        'debug': 'Print debug info',
        'verbose': "Enable verbose output",
        'number' : "Number of attempts allowed by the game"
    }

    parser.add_argument('-d', '--debug',
                        default=False,
                        action='store_true',
                        help=help_dict['debug']
                        )
    parser.add_argument('-v', '--verbose',
                        default=False,
                        action='store_true',
                        help=help_dict['verbose']
                        )
    parser.add_argument('-n',
                        metavar='N',
                        dest='n',
                        type=int,
                        default=10,
                        action='store',
                        help=help_dict['number']
                        )
    parser.add_argument('--difficulty',
                        type=int,
                        default=1,
                        action='store'
                        )
    try:
        args = parser.parse_args()
    except argparse.ArgumentError as e:
        err_msg(f"Caught argparse.ArgumentError: {e}")
    return args
