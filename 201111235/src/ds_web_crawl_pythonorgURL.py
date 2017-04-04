# coding: utf-8
    
import requests
import re
rResponse = requests.get('http://python.org/')
_html = rResponse.text
print len(_html)

print type(_html)

import re

p=re.compile('href="(http://.*?)"')
nodes=p.findall(_html)
print "http url은 몇 개?",len(nodes)
for i, node in enumerate(nodes):
    print i, node
    
    
import re
p=re.compile('<h1>(.*?)</h1>')
h1tags=p.findall(_html)
for tag in h1tags:
    print tag
    
import re
p=re.compile('<p>(.*?)</p>')
ptags=p.findall(_html)

print len(ptags)
print ptags[0]

from urllib import urlopen
from bs4 import BeautifulSoup
#_html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
_html = urlopen("http://en.wikipedia.org/wiki/HTML").read()
tree = BeautifulSoup(_html, "lxml")
counter=0
for link in tree.findAll("a"):
    if 'href' in link.attrs:
        if counter<20:
            print counter, link.attrs['href']
        counter+=1
print "Total: ", counter
    
    
    
print type(_html)
print len(_html)

from lxml import etree
_htmlTree = etree.HTML(_html)
result = etree.tostring(_htmlTree, pretty_print=True, method="html")
print len(result)
nodes = _htmlTree.xpath('//*[@href]')
print len(nodes)
for i, node in enumerate(nodes):
    if i<20:
        print i, node.attrib
        
        

                        
import lxml.html
from lxml.cssselect import CSSSelector
import requests
r = requests.get('http://python.org/')

html = lxml.html.fromstring(r.text)
sel=CSSSelector('a[href]')
# Apply the selector to the DOM tree.
nodes = sel(html)
print len(nodes)
for i,node in enumerate(nodes):
    #print lxml.html.tostring(item)
    if i<20:
        print i, node.get('href'), node.text
                        
                        
                        
import lxml.html
from lxml.cssselect import CSSSelector
import requests
r = requests.get('http://python.org/')

html = lxml.html.fromstring(r.text)
sel=CSSSelector('a[href]')
nodes = sel(html)
for node in nodes:
    print node.text
    print "----------"
    
    