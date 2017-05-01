import os
import mylib

keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
key=mylib.getKey(keyPath)
KEY=str(key['dataseoul'])
TYPE='xml'
SERVICE='SearchSTNBySubwayLineService'
START_INDEX=str(1)
END_INDEX=str(100)
LINE_NUM=str(2)

params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX,LINE_NUM)
import urlparse
_url='http://openAPI.seoul.go.kr:8088/'
url=urlparse.urljoin(_url,params)
#print url
import requests
data=requests.get(url).text
import re
p=re.compile('<STATION_NM>(.+?)</STATION_NM>')
res=p.findall(data)
for item in res:
    print item