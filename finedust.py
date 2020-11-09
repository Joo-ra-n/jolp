from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse
import pymysql
import requests
import base64
import logging
import sys

place = parse.quote('신암동')

M = '&numOfRows=1&pageNo=1&stationName=' + place + '&dataTerm=DAILY&ver=1.3'
key = 'T%2BSKyJKmZyzmUWiFt%2F9YBFdL7nC3qKKrbwx2E0cJtsQL4Tp429jfVaYEIZqxmKcstLagRsBlT%2BMQ81SsAwr2Nw%3D%3D'
url1 = 'http://openapi.airkorea.or.kr/openapi/services/rest'
url2 = '/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey='
long_url = url1 + url2 + key + M

html = urlopen(long_url)
soup = BeautifulSoup(html, "html.parser")
ItemList = soup.findAll('item')

#  데이터를 변수에 입력
for item in ItemList:
    a = item.find('datatime').text
    g = item.find('pm10value').text
    i = item.find('pm25value').text
    s = item.find('pm10grade1h').text
    t = item.find('pm25grade1h').text

print('측정소: ' + parse.unquote(place))
print('측정시간: ' + a)
print('미세먼지 농도: ' + g + '㎍/㎥ ( ' + s + ' )')
print('초미세먼지 농도: ' + i + '㎍/㎥ ( ' + s + ' )')
print('( 좋음: 1 ),( 보통: 2 ),( 나쁨: 3 ),( 매우나쁨: 4)')

# RDS info
host = 'rds-mariadb-jolp.c4c7vriv1s2u.ap-northeast-2.rds.amazonaws.com'
port = 3306
username = 'rds-mariadb-jolp'
database = 'finedust'
password = ''

# Client Credentials Flow
def main():
    # get headers
    headers = get_headers(client_id, client_secret)

    #call RDS
    conn, cursor = connect_RDS(host, port, username, password, database)

if __name__ == '__main__':
    main()

def connect_RDS(host, port, username, password, database):
    try:
        conn = pymysql.connect(host, user=username, passwd=password, db=database,
                               port=port, use_unicode=True, charset='utf8')
        cursor = conn.cursor()
    except:
        logging.error("RDS에 연결되지 않았습니다.")
        sys.exit(1)

    return conn, cursor

query = '''
insert into artists (id, name, followerasdfasdfasf
values
'''