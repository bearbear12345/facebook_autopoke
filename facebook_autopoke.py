import mechanize
import time
import os
import sys

arg = sys.argv
exp = 60
browser = mechanize.Browser()
browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0')]
browser.set_handle_robots(False)

browser.open("http://m.facebook.com/pokes")
browser._factory.is_html = True
browser.select_form(nr=0)
browser.form['email'] = arg[0]
browser.form['pass'] = arg[1]
browser.submit()
browser._factory.is_html = True
while True:
        try:
		browser.open("http://m.facebook.com/pokes")
		browser._factory.is_html = True
		for l in browser.links(text_regex="Poke back"):
			result = True
			browser._factory.is_html = True
			if result:
				browser.follow_link(text_regex="Poke back",nr=0)
                                print("Poke!")
                                if exp > 31:
                                        exp -= 30
                if exp < 180:
                        exp += 1
                time.sleep(exp)
	except:
		print "There was some sort of error :("
                break
