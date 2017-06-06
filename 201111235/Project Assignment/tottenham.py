# coding: utf-8
import requests
import urllib
from scrapy.selector import Selector


##################################

url = 'https://www.premierleague.com/players/4999/Son-Heung-Min/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4
target=open('data/tottenham/playerlist.txt','w')
nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()
    name=node.css("h1>div::text").extract()
    if number and name:
        number=number[0].strip()
        name=name[0].strip()
    target.write(number+'\t')
    target.write(name+'\t')
    print number,name
nodes=Selector(text=_html).xpath("//*[@class='topStat']")
i=0
for node in nodes:
    value = node.css("span[class='stat']>span::text").extract()

    if value and stats:

        value = value[0].strip()
    target.write(value+'\t')

    print stats[i], value
    cal[i]=value
    i=i+1


total=int(cal[2])+int(cal[3])
target.write(str(total)+'\t')
if total!=0:
    winper=(float(cal[2])/total)*100
    target.write(str(winper))
else:
    winper=0
    target.write(str(winper))

target.write('\n')
print "출장횟수:",total
print "출장 횟수 대비 승률:",winper,"%"
print number,"txt파일로 저장완료\n"
##################################

url = 'https://www.premierleague.com/players/3955/Kyle-Walker/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()
    name=node.css("h1>div::text").extract()
    if number and name:
        number=number[0].strip()
        name=name[0].strip()
    target.write(number+'\t')
    target.write(name+'\t')
    print number,name
nodes=Selector(text=_html).xpath("//*[@class='topStat']")
i=0
for node in nodes:
    value = node.css("span[class='stat']>span::text").extract()

    if value and stats:

        value = value[0].strip()
    target.write(value+'\t')

    print stats[i], value
    cal[i]=value
    i=i+1


total=int(cal[2])+int(cal[3])
target.write(str(total)+'\t')
if total!=0:
    winper=(float(cal[2])/total)*100
    target.write(str(winper))
else:
    winper=0
    target.write(str(winper))

target.write('\n')
print "출장횟수:",total
print "출장 횟수 대비 승률:",winper,"%"
print number,"txt파일로 저장완료\n"
##################################

url = 'https://www.premierleague.com/players/3507/Danny-Rose/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()
    name=node.css("h1>div::text").extract()
    if number and name:
        number=number[0].strip()
        name=name[0].strip()
    target.write(number+'\t')
    target.write(name+'\t')
    print number,name
nodes=Selector(text=_html).xpath("//*[@class='topStat']")
i=0
for node in nodes:
    value = node.css("span[class='stat']>span::text").extract()

    if value and stats:

        value = value[0].strip()
    target.write(value+'\t')

    print stats[i], value
    cal[i]=value
    i=i+1

total=int(cal[2])+int(cal[3])
target.write(str(total)+'\t')
if total!=0:
    winper=(float(cal[2])/total)*100
    target.write(str(winper))
else:
    winper=0
    target.write(str(winper))

target.write('\n')
print "출장횟수:",total
print "출장 횟수 대비 승률:",winper,"%"
print number,"txt파일로 저장완료\n"
print "출장횟수:",total
print "출장 횟수 대비 승률:",winper,"%"
print number,"txt파일로 저장완료\n"

##################################

url = 'https://www.premierleague.com/players/4916/Toby-Alderweireld/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()
    name=node.css("h1>div::text").extract()
    if number and name:
        number=number[0].strip()
        name=name[0].strip()
    target.write(number+'\t')
    target.write(name+'\t')
    print number,name
nodes=Selector(text=_html).xpath("//*[@class='topStat']")
i=0
for node in nodes:
    value = node.css("span[class='stat']>span::text").extract()

    if value and stats:

        value = value[0].strip()
    target.write(value+'\t')

    print stats[i], value
    cal[i]=value
    i=i+1


total=int(cal[2])+int(cal[3])
target.write(str(total)+'\t')
if total!=0:
    winper=(float(cal[2])/total)*100
    target.write(str(winper))
else:
    winper=0
    target.write(str(winper))

target.write('\n')
print "출장횟수:",total
print "출장 횟수 대비 승률:",winper,"%"
print number,"txt파일로 저장완료\n"

##################################

url = 'https://www.premierleague.com/players/4666/Jan-Vertonghen/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()
    name=node.css("h1>div::text").extract()
    if number and name:
        number=number[0].strip()
        name=name[0].strip()
    target.write(number+'\t')
    target.write(name+'\t')
    print number,name
nodes=Selector(text=_html).xpath("//*[@class='topStat']")
i=0
for node in nodes:
    value = node.css("span[class='stat']>span::text").extract()

    if value and stats:

        value = value[0].strip()
    target.write(value+'\t')

    print stats[i], value
    cal[i]=value
    i=i+1


total=int(cal[2])+int(cal[3])
target.write(str(total)+'\t')
if total!=0:
    winper=(float(cal[2])/total)*100
    target.write(str(winper))
else:
    winper=0
    target.write(str(winper))

target.write('\n')
print "출장횟수:",total
print "출장 횟수 대비 승률:",winper,"%"
print number,"txt파일로 저장완료\n"

##################################

url = 'https://www.premierleague.com/players/3905/Kieran-Trippier/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()
    name=node.css("h1>div::text").extract()
    if number and name:
        number=number[0].strip()
        name=name[0].strip()
    target.write(number+'\t')
    target.write(name+'\t')
    print number,name
nodes=Selector(text=_html).xpath("//*[@class='topStat']")
i=0
for node in nodes:
    value = node.css("span[class='stat']>span::text").extract()

    if value and stats:

        value = value[0].strip()
    target.write(value+'\t')

    print stats[i], value
    cal[i]=value
    i=i+1


total=int(cal[2])+int(cal[3])
target.write(str(total)+'\t')
if total!=0:
    winper=(float(cal[2])/total)*100
    target.write(str(winper))
else:
    winper=0
    target.write(str(winper))

target.write('\n')
print "출장횟수:",total
print "출장 횟수 대비 승률:",winper,"%"
print number,"txt파일로 저장완료\n"

##################################

url = 'https://www.premierleague.com/players/13813/Kevin-Wimmer/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()
    name=node.css("h1>div::text").extract()
    if number and name:
        number=number[0].strip()
        name=name[0].strip()
    target.write(number+'\t')
    target.write(name+'\t')
    print number,name
nodes=Selector(text=_html).xpath("//*[@class='topStat']")
i=0
for node in nodes:
    value = node.css("span[class='stat']>span::text").extract()

    if value and stats:

        value = value[0].strip()
    target.write(value+'\t')

    print stats[i], value
    cal[i]=value
    i=i+1


total=int(cal[2])+int(cal[3])
target.write(str(total)+'\t')
if total!=0:
    winper=(float(cal[2])/total)*100
    target.write(str(winper))
else:
    winper=0
    target.write(str(winper))

target.write('\n')
print "출장횟수:",total
print "출장 횟수 대비 승률:",winper,"%"
print number,"txt파일로 저장완료\n"

##################################

url = 'https://www.premierleague.com/players/4408/Ben-Davies/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()
    name=node.css("h1>div::text").extract()
    if number and name:
        number=number[0].strip()
        name=name[0].strip()
    target.write(number+'\t')
    target.write(name+'\t')
    print number,name
nodes=Selector(text=_html).xpath("//*[@class='topStat']")
i=0
for node in nodes:
    value = node.css("span[class='stat']>span::text").extract()

    if value and stats:

        value = value[0].strip()
    target.write(value+'\t')

    print stats[i], value
    cal[i]=value
    i=i+1


total=int(cal[2])+int(cal[3])
target.write(str(total)+'\t')
if total!=0:
    winper=(float(cal[2])/total)*100
    target.write(str(winper))
else:
    winper=0
    target.write(str(winper))

target.write('\n')
print "출장횟수:",total
print "출장 횟수 대비 승률:",winper,"%"
print number,"txt파일로 저장완료\n"

##################################

url = 'https://www.premierleague.com/players/4842/Erik-Lamela/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()
    name=node.css("h1>div::text").extract()
    if number and name:
        number=number[0].strip()
        name=name[0].strip()
    target.write(number+'\t')
    target.write(name+'\t')
    print number,name
nodes=Selector(text=_html).xpath("//*[@class='topStat']")
i=0
for node in nodes:
    value = node.css("span[class='stat']>span::text").extract()

    if value and stats:

        value = value[0].strip()
    target.write(value+'\t')

    print stats[i], value
    cal[i]=value
    i=i+1

total=int(cal[2])+int(cal[3])
target.write(str(total)+'\t')
if total!=0:
    winper=(float(cal[2])/total)*100
    target.write(str(winper))
else:
    winper=0
    target.write(str(winper))

target.write('\n')
print "출장횟수:",total
print "출장 횟수 대비 승률:",winper,"%"
print number,"txt파일로 저장완료\n"

##################################

url = 'https://www.premierleague.com/players/4112/Eric-Dier/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()
    name=node.css("h1>div::text").extract()
    if number and name:
        number=number[0].strip()
        name=name[0].strip()
    target.write(number+'\t')
    target.write(name+'\t')
    print number,name
nodes=Selector(text=_html).xpath("//*[@class='topStat']")
i=0
for node in nodes:
    value = node.css("span[class='stat']>span::text").extract()

    if value and stats:

        value = value[0].strip()
    target.write(value+'\t')

    print stats[i], value
    cal[i]=value
    i=i+1


total=int(cal[2])+int(cal[3])
target.write(str(total)+'\t')
if total!=0:
    winper=(float(cal[2])/total)*100
    target.write(str(winper))
else:
    winper=0
    target.write(str(winper))

target.write('\n')
print "출장횟수:",total
print "출장 횟수 대비 승률:",winper,"%"
print number,"txt파일로 저장완료\n"

##################################

url = 'https://www.premierleague.com/players/4123/Mousa-Dembélé/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()

    if number:
        number=number[0].strip()

    target.write(number+'\t')
    target.write('Mousa Dembele\t')
    print number,'Mousa Dembele'
nodes=Selector(text=_html).xpath("//*[@class='topStat']")
i=0
for node in nodes:
    value = node.css("span[class='stat']>span::text").extract()

    if value and stats:

        value = value[0].strip()
    target.write(value+'\t')

    print stats[i], value
    cal[i]=value
    i=i+1


total=int(cal[2])+int(cal[3])
target.write(str(total)+'\t')
if total!=0:
    winper=(float(cal[2])/total)*100
    target.write(str(winper))
else:
    winper=0
    target.write(str(winper))

target.write('\n')
print "출장횟수:",total
print "출장 횟수 대비 승률:",winper,"%"
print number,"txt파일로 저장완료\n"


##################################

url = 'https://www.premierleague.com/players/9167/Dele-Alli/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()
    name=node.css("h1>div::text").extract()
    if number and name:
        number=number[0].strip()
        name=name[0].strip()
    target.write(number+'\t')
    target.write(name+'\t')
    print number,name
nodes=Selector(text=_html).xpath("//*[@class='topStat']")
i=0
for node in nodes:
    value = node.css("span[class='stat']>span::text").extract()

    if value and stats:

        value = value[0].strip()
    target.write(value+'\t')

    print stats[i], value
    cal[i]=value
    i=i+1


total=int(cal[2])+int(cal[3])
target.write(str(total)+'\t')
if total!=0:
    winper=(float(cal[2])/total)*100
    target.write(str(winper))
else:
    winper=0
    target.write(str(winper))

target.write('\n')
print "출장횟수:",total
print "출장 횟수 대비 승률:",winper,"%"
print number,"txt파일로 저장완료\n"

##################################

url = 'https://www.premierleague.com/players/4845/Christian-Eriksen/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()
    name=node.css("h1>div::text").extract()
    if number and name:
        number=number[0].strip()
        name=name[0].strip()
    target.write(number+'\t')
    target.write(name+'\t')
    print number,name
nodes=Selector(text=_html).xpath("//*[@class='topStat']")
i=0
for node in nodes:
    value = node.css("span[class='stat']>span::text").extract()

    if value and stats:

        value = value[0].strip()
    target.write(value+'\t')

    print stats[i], value
    cal[i]=value
    i=i+1


total=int(cal[2])+int(cal[3])
target.write(str(total)+'\t')
if total!=0:
    winper=(float(cal[2])/total)*100
    target.write(str(winper))
else:
    winper=0
    target.write(str(winper))

target.write('\n')
print "출장횟수:",total
print "출장 횟수 대비 승률:",winper,"%"
print number,"txt파일로 저장완료\n"
##################################

url = 'https://www.premierleague.com/players/3960/Harry-Kane/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()
    name=node.css("h1>div::text").extract()
    if number and name:
        number=number[0].strip()
        name=name[0].strip()
    target.write(number+'\t')
    target.write(name+'\t')
    print number,name
nodes=Selector(text=_html).xpath("//*[@class='topStat']")
i=0
for node in nodes:
    value = node.css("span[class='stat']>span::text").extract()

    if value and stats:

        value = value[0].strip()
    target.write(value+'\t')

    print stats[i], value
    cal[i]=value
    i=i+1

total=int(cal[2])+int(cal[3])
target.write(str(total)+'\t')
if total!=0:
    winper=(float(cal[2])/total)*100
    target.write(str(winper))
else:
    winper=0
    target.write(str(winper))

target.write('\n')
print "출장횟수:",total
print "출장 횟수 대비 승률:",winper,"%"
print number,"txt파일로 저장완료\n"

##################################

url = 'https://www.premierleague.com/players/4816/Victor-Wanyama/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()
    name=node.css("h1>div::text").extract()
    if number and name:
        number=number[0].strip()
        name=name[0].strip()
    target.write(number+'\t')
    target.write(name+'\t')
    print number,name
nodes=Selector(text=_html).xpath("//*[@class='topStat']")
i=0
for node in nodes:
    value = node.css("span[class='stat']>span::text").extract()

    if value and stats:

        value = value[0].strip()
    target.write(value+'\t')

    print stats[i], value
    cal[i]=value
    i=i+1


total=int(cal[2])+int(cal[3])
target.write(str(total)+'\t')
if total!=0:
    winper=(float(cal[2])/total)*100
    target.write(str(winper))
else:
    winper=0
    target.write(str(winper))

target.write('\n')
print "출장횟수:",total
print "출장 횟수 대비 승률:",winper,"%"
print number,"txt파일로 저장완료\n"

##################################

url = 'https://www.premierleague.com/players/15481/Vincent-Janssen/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()
    name=node.css("h1>div::text").extract()
    if number and name:
        number=number[0].strip()
        name=name[0].strip()
    target.write(number+'\t')
    target.write(name+'\t')
    print number,name
nodes=Selector(text=_html).xpath("//*[@class='topStat']")
i=0
for node in nodes:
    value = node.css("span[class='stat']>span::text").extract()

    if value and stats:

        value = value[0].strip()
    target.write(value+'\t')

    print stats[i], value
    cal[i]=value
    i=i+1


total=int(cal[2])+int(cal[3])
target.write(str(total)+'\t')
if total!=0:
    winper=(float(cal[2])/total)*100
    target.write(str(winper))
else:
    winper=0
    target.write(str(winper))

target.write('\n')
print "출장횟수:",total
print "출장 횟수 대비 승률:",winper,"%"
print number,"txt파일로 저장완료\n"


##################################

url = 'https://www.premierleague.com/players/7490/Josh-Onomah/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()
    name=node.css("h1>div::text").extract()
    if number and name:
        number=number[0].strip()
        name=name[0].strip()
    target.write(number+'\t')
    target.write(name+'\t')
    print number,name
nodes=Selector(text=_html).xpath("//*[@class='topStat']")
i=0
for node in nodes:
    value = node.css("span[class='stat']>span::text").extract()

    if value and stats:

        value = value[0].strip()
    target.write(value+'\t')

    print stats[i], value
    cal[i]=value
    i=i+1


total=int(cal[2])+int(cal[3])
target.write(str(total)+'\t')
if total!=0:
    winper=(float(cal[2])/total)*100
    target.write(str(winper))
else:
    winper=0
    target.write(str(winper))

target.write('\n')
print "출장횟수:",total
print "출장 횟수 대비 승률:",winper,"%"
print number,"txt파일로 저장완료\n"
##################################

url = 'https://www.premierleague.com/players/7488/Harry-Winks/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()
    name=node.css("h1>div::text").extract()
    if number and name:
        number=number[0].strip()
        name=name[0].strip()
    target.write(number+'\t')
    target.write(name+'\t')
    print number,name
nodes=Selector(text=_html).xpath("//*[@class='topStat']")
i=0
for node in nodes:
    value = node.css("span[class='stat']>span::text").extract()

    if value and stats:

        value = value[0].strip()
    target.write(value+'\t')

    print stats[i], value
    cal[i]=value
    i=i+1


total=int(cal[2])+int(cal[3])
target.write(str(total)+'\t')
if total!=0:
    winper=(float(cal[2])/total)*100
    target.write(str(winper))
else:
    winper=0
    target.write(str(winper))

target.write('\n')
print "출장횟수:",total
print "출장 횟수 대비 승률:",winper,"%"
print number,"txt파일로 저장완료\n"

##################################

url = 'https://www.premierleague.com/players/20742/Pau-López/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()

    if number:
        number=number[0].strip()

    target.write(number+'\t')
    target.write('Pau Lopez\t')
    print number,'Pau Lopez'
nodes=Selector(text=_html).xpath("//*[@class='topStat']")
i=0
for node in nodes:
    value = node.css("span[class='stat']>span::text").extract()

    if value and stats:

        value = value[0].strip()
    target.write(value+'\t')

    print stats[i], value
    cal[i]=value
    i=i+1


total=int(cal[2])+int(cal[3])
target.write(str(total)+'\t')
if total!=0:
    winper=(float(cal[2])/total)*100
    target.write(str(winper))
else:
    winper=0
    target.write(str(winper))

target.write('\n')
print "출장횟수:",total
print "출장 횟수 대비 승률:",winper,"%"
print number,"txt파일로 저장완료\n"

##################################

url = 'https://www.premierleague.com/players/4549/Moussa-Sissoko/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()
    name=node.css("h1>div::text").extract()
    if number and name:
        number=number[0].strip()
        name=name[0].strip()
    target.write(number+'\t')
    target.write(name+'\t')
    print number,name
nodes=Selector(text=_html).xpath("//*[@class='topStat']")
i=0
for node in nodes:
    value = node.css("span[class='stat']>span::text").extract()

    if value and stats:

        value = value[0].strip()
    target.write(value+'\t')

    print stats[i], value
    cal[i]=value
    i=i+1


total=int(cal[2])+int(cal[3])
target.write(str(total)+'\t')
if total!=0:
    winper=(float(cal[2])/total)*100
    target.write(str(winper))
else:
    winper=0
    target.write(str(winper))

target.write('\n')
print "출장횟수:",total
print "출장 횟수 대비 승률:",winper,"%"
print number,"txt파일로 저장완료\n"

##################################

url = 'https://www.premierleague.com/players/15938/Georges-Kévin-Nkoudou/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()

    if number :
        number=number[0].strip()

    target.write(number+'\t')
    target.write('Georges Kevin-Nkoudou\t')
    print number,'Georges Kevin-Nkoudou'
nodes=Selector(text=_html).xpath("//*[@class='topStat']")
i=0
for node in nodes:
    value = node.css("span[class='stat']>span::text").extract()

    if value and stats:

        value = value[0].strip()
    target.write(value+'\t')

    print stats[i], value
    cal[i]=value
    i=i+1


total=int(cal[2])+int(cal[3])
target.write(str(total)+'\t')
if total!=0:
    winper=(float(cal[2])/total)*100
    target.write(str(winper))
else:
    winper=0
    target.write(str(winper))

target.write('\n')
print "출장횟수:",total
print "출장 횟수 대비 승률:",winper,"%"
print number,"txt파일로 저장완료\n"



##################################

url = 'https://www.premierleague.com/players/4664/Hugo-Lloris/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Clean Sheets","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()
    name=node.css("h1>div::text").extract()
    if number and name:
        number=number[0].strip()
        name=name[0].strip()
    target.write(number+'\t')
    target.write(name+'\t')
    print number,name
nodes=Selector(text=_html).xpath("//*[@class='topStat']")
i=0
for node in nodes:
    value = node.css("span[class='stat']>span::text").extract()

    if value and stats:

        value = value[0].strip()
    target.write(value+'\t')

    print stats[i], value
    cal[i]=value
    i=i+1


total=int(cal[2])+int(cal[3])
target.write(str(total)+'\t')
if total!=0:
    winper=(float(cal[2])/total)*100
    target.write(str(winper))
else:
    winper=0
    target.write(str(winper))

target.write('\n')
print "출장횟수:",total
print "출장 횟수 대비 승률:",winper,"%"
print number,"txt파일로 저장완료\n"
##################################

url = 'https://www.premierleague.com/players/4398/Michel-Vorm/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Clean Sheets","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()
    name=node.css("h1>div::text").extract()
    if number and name:
        number=number[0].strip()
        name=name[0].strip()
    target.write(number+'\t')
    target.write(name+'\t')
    print number,name
nodes=Selector(text=_html).xpath("//*[@class='topStat']")
i=0
for node in nodes:
    value = node.css("span[class='stat']>span::text").extract()

    if value and stats:

        value = value[0].strip()
    target.write(value+'\t')

    print stats[i], value
    cal[i]=value
    i=i+1


total=int(cal[2])+int(cal[3])
target.write(str(total)+'\t')
if total!=0:
    winper=(float(cal[2])/total)*100
    target.write(str(winper))
else:
    winper=0
    target.write(str(winper))

target.write('\n')
print "출장횟수:",total
print "출장 횟수 대비 승률:",winper,"%"
print number,"txt파일로 저장완료\n"
target.close()