#!/usr/bin/env python

import pastebin

try:
    paste_url = pastebin.paste('test')
    print paste_url                    # print the paste url
except pastebin.PasteError, err:          # handle pastebin API error.
    print err
    exit(0)
