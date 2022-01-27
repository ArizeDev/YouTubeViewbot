from webbot import Browser

# We are currently using webbot as it is faster than selenium depending on what ide you are using.
# If you want faster responses, use vscode.

import os, time, random

# These are some modules that is rarely used

with open("basicterminal/proxies.txt", "r") as _proxies:
     proxies =  []
     proxies += [proxy.strip() for proxy in _proxies.readlines()]

# This is where you import the website url

website_url = ""

# Here are the scripts for this repository

for _proxy in proxies:
    web  = webbot.Browser(
           proxy = _proxy
    )
    
    try:
       web.go_to(website_url)
       print (" [/] View Registered (%s)" % (_proxy))
    except Exception as E:
       pass
