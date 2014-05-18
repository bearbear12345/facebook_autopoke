#!/usr/bin/python
# -*- coding: utf-8 -*-

USERNAME = ""
PASSWORD = ""

def update():
    global totalPokes
    f = open('pokecount.txt', 'w')
    f.write(str(totalPokes))
    f.close()

import mechanize
import time
import os
os.system('clear') # Clears the screen (*nix)
MAX_DELAY = 60
delay = 10

# Get poke count
if os.path.isfile('pokecount.txt'):
    f = open('pokecount.txt', 'r')
    totalPokes = int(f.read())
else:
    f = open('pokecount.txt', 'w')
    totalPokes = 0
    update()
f.close()

# Blocked IDs
blocked = []
if os.path.isfile('blocked_ids.txt'):
    f = open('blocked_ids.txt', 'r')
    blocked = f.read().splitlines()
else:
    f = open('blocked_ids.txt', 'w')
f.close()

print 'Initial Poke Count: ' + str(totalPokes)

browser = mechanize.Browser()
browser.addheaders = [('User-agent',
                      'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.61'
                      )]
browser.set_handle_robots(False)
browser.open('http://m.facebook.com/pokes')
browser._factory.is_html = True
browser.select_form(nr=0)
browser.form['email'] = USERNAME
browser.form['pass'] = PASSWORD
browser.submit()
browser._factory.is_html = True
while True:
    try:
        print 'Checking pokes...'
        tempPokeCount = 0
        browser.open('http://m.facebook.com/pokes')
        browser._factory.is_html = True
        for link in browser.links(text_regex='Poke Back'):
            uid = link.url[link.url.index('poke_target=')
                + 12:link.url.index('&redirect_url=')]
            if not uid in blocked:
                result = True
                browser._factory.is_html = True
                if result:
                    browser.follow_link(link)
                    tempPokeCount += 1
                    totalPokes += 1
                    update()
                    print 'Poked user', uid + '! Total Pokes: ' + str(totalPokes) \
                        + '\n'
        if tempPokeCount != 0 and delay > 1:
            delay = delay / 2 + 1
        if tempPokeCount == 0 and delay < MAX_DELAY:
            delay *= 2
    except:
        print 'There was some sort of error :('
    print 'Waiting ' + str(delay)
    time.sleep(delay)
