#!python3
# mapIt.py - Launches a map in the browser using an address form the command line or clipboard.
# type mapIt.py + an address you would like to search for.

import webbrowser,sys,pyperclip
if len(sys.argv) > 1:
    # Get address from command line.
    address = ''.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
