# coding: utf-8
import requests
import urllib
from scrapy.selector import Selector


##################################

url = 'https://www.premierleague.com/players/5175/Kurt-Zouma/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4
target=open('data/chelsea/playerlist.txt','w')
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

url = 'https://www.premierleague.com/players/2620/Gary-Cahill/stats'
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

url = 'https://www.premierleague.com/players/1353/John-Terry/stats'
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

url = 'https://www.premierleague.com/players/4496/César-Azpilicueta/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()

    if number :
        number=number[0].strip()
        name=("Cesar-Azpilicueta")
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

url = 'https://www.premierleague.com/players/2417/Cesc-Fàbregas/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()

    if number and name:
        number=number[0].strip()
        name=("Cesc-Fabregas")
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

url = 'https://www.premierleague.com/players/4503/Eden-Hazard/stats'
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

url = 'https://www.premierleague.com/players/3861/Nemanja-Matic/stats'
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

url = 'https://www.premierleague.com/players/4748/Willian/stats'
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

url = 'https://www.premierleague.com/players/5179/Ruben-Loftus-Cheek/stats'
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

url = 'https://www.premierleague.com/players/4972/Pedro/stats'
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

url = 'https://www.premierleague.com/players/4941/Diego-Costa/stats'
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

url = 'https://www.premierleague.com/players/3983/Victor-Moses/stats'
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

url = 'https://www.premierleague.com/players/7450/Michy-Batshuayi/stats'
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
import urllib
url =  urllib.unquote("https%3a%2f%2fwww.premierleague.com%2fplayers%2f13492%2fN%27Golo-Kant%25C3%25A9%2fstats")

r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()

    if number :
        number=number[0].strip()
        name=("N Golo Kante")
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

url = 'https://www.premierleague.com/players/10439/Ola-Aina/stats'
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

url = 'https://www.premierleague.com/players/4105/Nathaniel-Chalobah/stats'
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

url = 'https://www.premierleague.com/players/4100/David-Luiz/stats'
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

url = 'https://www.premierleague.com/players/4093/Marcos-Alonso/stats'
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

url = 'https://www.premierleague.com/players/2537/Asmir-Begovic/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","CleanSheet","Wins","Losses"]
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

url = 'https://www.premierleague.com/players/4911/Thibaut-Courtois/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","CleanSheet","Wins","Losses"]
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
