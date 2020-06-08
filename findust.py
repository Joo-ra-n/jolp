import requests
from bs4 import BeautifulSoup
import pandas

M = '&numOfRows=1&pageNo=1&stationName=수창동&dataTerm=DAILY&ver=1.3'
key = 'T%2BSKyJKmZyzmUWiFt%2F9YBFdL7nC3qKKrbwx2E0cJtsQL4Tp429jfVaYEIZqxmKcstLagRsBlT%2BMQ81SsAwr2Nw%3D%3D'
url = 'http://openapi.airkorea.or.kr/openapi/services/rest/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo?serviceKey=' + key + M

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
ItemList = soup.findAll('item')

# for item in ItemList:
a = item.find('datatime').text
g = item.find('pm10value').text
i = item.find('pm25value').text
s = item.find('pm10grade1h').text
t = item.find('pm25grade1h').text

print('측정소: 수창동')
print('측정시간:' + a)
print('미세먼지 농도:' + g + '㎍/㎥ ( ' + s + ' )')
print('초미세먼지 농도:' + i + '㎍/㎥ ( ' + s + ' )')
print('( 좋음: 1 ),( 보통: 2 ),( 나쁨: 3 ),( 매우나쁨: 4)')
