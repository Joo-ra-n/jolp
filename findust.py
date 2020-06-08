from urllib.request import urlopen
from bs4 import BeautifulSoup

M = '&numOfRows=1&pageNo=1&stationName=%EC%8B%A0%EC%95%94%EB%8F%99&dataTerm=DAILY&ver=1.3'
key = 'T%2BSKyJKmZyzmUWiFt%2F9YBFdL7nC3qKKrbwx2E0cJtsQL4Tp429jfVaYEIZqxmKcstLagRsBlT%2BMQ81SsAwr2Nw%3D%3D'
url1 = 'http://openapi.airkorea.or.kr/openapi/services/rest'
url2 = '/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey='
long_url = url1 + url2 + key + M
print(long_url)

html = urlopen(long_url)
soup = BeautifulSoup(html, "html.parser")
ItemList = soup.findAll('item')

for item in ItemList:
    a = item.find('datatime').text
    g = item.find('pm10value').text
    i = item.find('pm25value').text
    s = item.find('pm10grade1h').text
    t = item.find('pm25grade1h').text

print('측정소: 신암동')
print('측정시간:' + a)
print('미세먼지 농도:' + g + '㎍/㎥ ( ' + s + ' )')
print('초미세먼지 농도:' + i + '㎍/㎥ ( ' + s + ' )')
print('( 좋음: 1 ),( 보통: 2 ),( 나쁨: 3 ),( 매우나쁨: 4)')
