# coding: utf-8
import requests
import urllib
from scrapy.selector import Selector


##################################

url = 'https://www.premierleague.com/players/4546/Mathieu-Debuchy/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4
target=open('data/arsenal/playerlist.txt','w')
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

url = 'https://www.premierleague.com/players/3046/Kieran-Gibbs/stats'
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

url = 'https://www.premierleague.com/players/4246/Per-Mertesacker/stats'
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

url = 'https://www.premierleague.com/players/10423/Gabriel/stats'
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

url = 'https://www.premierleague.com/players/4030/Laurent-Koscielny/stats'
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

url = 'https://www.premierleague.com/players/4472/Nacho-Monreal/stats'
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

url = 'https://www.premierleague.com/players/4474/Héctor-Bellerín/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()

    if number :
        number=number[0].strip()
        name=("Hector-Bellerin")
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

url = 'https://www.premierleague.com/players/4248/Carl-Jenkinson/stats'
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

url = 'https://www.premierleague.com/players/4714/Mesut-Özil/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()

    if number :
        number=number[0].strip()
        name=("Mesut-Ozil")
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

url = 'https://www.premierleague.com/players/4252/Alex-Oxlade-Chamberlain/stats'
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

url = 'https://www.premierleague.com/players/3548/Aaron-Ramsey/stats'
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

url = 'https://www.premierleague.com/players/4477/Santiago-Cazorla/stats'
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

url = 'https://www.premierleague.com/players/3549/Francis-Coquelin/stats'
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

url = 'https://www.premierleague.com/players/5239/Mohamed-Elneny/stats'
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

url = 'https://www.premierleague.com/players/4717/Alex-Iwobi/stats'
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

url = 'https://www.premierleague.com/players/2839/Theo-Walcott/stats'
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

url = 'https://www.premierleague.com/players/4973/Alexis-Sánchez/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()

    if number:
        number=number[0].strip()
        name=("Alexis-Sanchez")
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

url = 'https://www.premierleague.com/players/4718/Yaya-Sanogo/stats'
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

url = 'https://www.premierleague.com/players/3452/Danny-Welbeck/stats'
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

url = 'https://www.premierleague.com/players/12136/Granit-Xhaka/stats'
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

url = 'https://www.premierleague.com/players/11575/Rob-Holding/stats'
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

url = 'https://www.premierleague.com/players/3869/Shkodran-Mustafi/stats'
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

url = 'https://www.premierleague.com/players/7081/Lucas-Pérez/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","Goals","Wins","Losses"]
cal=[None]*4

nodes=Selector(text=_html).xpath("//*[@class='playerDetails']")
for node in nodes:
    number=node.css("div[class='number']::text").extract()

    if number:
        number=number[0].strip()
        name=("Lucas-Perez")
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

url = 'https://www.premierleague.com/players/2651/Petr-Cech/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","CleanSheets","Wins","Losses"]
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

url = 'https://www.premierleague.com/players/10420/David-Ospina/stats'
r=requests.get(url)
_html=r.text

stats=["Appearances","CleanSheets","Wins","Losses"]
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