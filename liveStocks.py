#!python3
# liveStocks.py - Launches live stock chart via Yahoo in the browser using an address form the command line or clipboard.
# type liveStocks.py + an address you would like to search for.

import webbrowser,sys,pyperclip
if len(sys.argv) > 1:
    # Get address from command line.
    stock = ''.join(sys.argv[1:])
else:
    # Get address from clipboard.
    stock = pyperclip.paste()

webbrowser.open('https://finance.yahoo.com/quote/' + stock)
