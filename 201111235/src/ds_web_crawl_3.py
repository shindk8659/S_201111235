
#coding:utf-8

from urllib import urlopen

keyword='sangmyung univ'
resp = urlopen('https://www.google.com/search?q='+keyword)
html=resp.read()
len(html)

import os
f=open(os.path.join('googlesearch1.html'),'w')
f.write(html)
f.close()

from urllib import FancyURLopener
class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0'
print MyOpener.version


myopener = MyOpener()
page = myopener.open('http://www.google.com/search?q='+keyword)
html=page.read()

import os
f=open(os.path.join('googlesearch2.html'),'w')
f.write(html)
f.close()
import webbrowser
mygoogle='file://'+'localhost'+os.path.join(os.getcwd(), 'googlesearch2.html')
print mygoogle