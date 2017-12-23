#!/usr/bin/env python

"""hello

Hello is a tiny and useless program that is meant to demonstrate the docker-shim.

Usage:
    hello (-h | --help)
    hello greet <name>
    hello update
    hello --version

Options
    -h --help           Show the help.
    --version           Show the version.
"""

import sys

from docopt import docopt


def hello(args):
    if args['greet']:
        print("Hello, {}".format(args['<name>']))


def main():
    exit(hello(docopt(__doc__, version="hello {0}".format("GENERATE AT BUILD TIME"))))


if __name__ == "__main__":
    main()
