# coding: utf-8
from __future__ import print_function, unicode_literals
import re
import sys
import requests
from lxml.html import fromstring

try:
    raw_input
except NameError:
    raw_input = input  # py3

re_split = re.compile(r'\s+')


def set_hook():
    _old_excepthook = sys.excepthook

    def excepthook(exctype, value, traceback):
        if exctype == KeyboardInterrupt:
            print()
            sys.exit(0)
        _old_excepthook(exctype, value, traceback)

    sys.excepthook = excepthook


def main():
    while True:
        words = raw_input('> ').strip()
        for word in re_split.split(words):
            response = requests.get('http://wooordhunt.ru/word/{}'.format(word))
            root = fromstring(response.text)
            try:
                t = root.cssselect('span.transcription')[0].text
                t = t.strip().replace("ˈ", "'").replace('ː', ':')
                translate = root.cssselect('span.t_inline_en')[0].text
                print('{} - {}'.format(t, translate))
            except IndexError:
                pass


if __name__ == '__main__':
    set_hook()
    main()
