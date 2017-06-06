# coding: utf-8
import requests
import urllib
from scrapy.selector import Selector


##################################

url = 'https://www.premierleague.com/players/3311/Bacary-Sagna/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4
target=open('data/manchestercity/playerlist.txt','w')
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

url = 'https://www.premierleague.com/players/3653/Vincent-Kompany/stats'
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

url = 'https://www.premierleague.com/players/4141/Aleksandar-Kolarov/stats'
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

url = 'https://www.premierleague.com/players/2413/Gaël-Clichy/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()

    if number:
        number=number[0].strip()
        name=("Gael-Clichy")
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

url = 'https://www.premierleague.com/players/6058/Nicolás-Otamendi/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()

    if number:
        number=number[0].strip()
        name=("Nicolas-Otamendi")
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

url = 'https://www.premierleague.com/players/5344/Fernando/stats'
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

url = 'https://www.premierleague.com/players/4803/Jesús-Navas/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()

    if number:
        number=number[0].strip()
        name=("Jesus-Navas")
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

url = 'https://www.premierleague.com/players/4288/Kevin-De-Bruyne/stats'
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

url = 'https://www.premierleague.com/players/3799/Fabian-Delph/stats'
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

url = 'https://www.premierleague.com/players/4145/David-Silva/stats'
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

url = 'https://www.premierleague.com/players/4804/Fernandinho/stats'
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

url = 'https://www.premierleague.com/players/4148/Yaya-Touré/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()

    if number:
        number=number[0].strip()
        name=("Yaya-Toure")
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

url = 'https://www.premierleague.com/players/4316/Raheem-Sterling/stats'
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

url = 'https://www.premierleague.com/players/4328/Sergio-Agüero/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()

    if number:
        number=number[0].strip()
        name=("Sergio-Aguero")
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

url = 'https://www.premierleague.com/players/13554/Kelechi-Iheanacho/stats'
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

url = 'https://www.premierleague.com/players/5101/Ilkay-Gündogan/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()

    if number :
        number=number[0].strip()
        name=("Ilkay-Gundogan")
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

url = 'https://www.premierleague.com/players/4505/John-Stones/stats'
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

url = 'https://www.premierleague.com/players/19604/Nolito/stats'
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

url = 'https://www.premierleague.com/players/5384/Leroy-Sané/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()

    if number:
        number=number[0].strip()
        name=("Leroy-Sane")
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

url = 'https://www.premierleague.com/players/19680/Gabriel-Jesus/stats'
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

url = 'https://www.premierleague.com/players/5810/Claudio-Bravo/stats'
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

url = 'https://www.premierleague.com/players/10466/Willy-Caballero/stats'
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
