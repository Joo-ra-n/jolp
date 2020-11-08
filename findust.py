from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse
import sqlite3

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

def dbcon():
    return sqlite3.connect('mydb.db')

def create_table():
    try:
        db = dbcon()
        c = db.cursor()
        execute1 = 'CREATE TABLE finedust (place varchar(30), time varchar(50), '
        execute2 = 'PM10 varchar(5), PM25 varchar(5), gradePM10 varchar(1), gradePM25 varchar(1))'
        c.execute(execute1 + execute2)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally: db.close()

def insert_data():
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (parse.unquote(place), a, g, i, s, t)
        c.execute("INSERT INTO finedust VALUES (?, ?, ?, ?, ?, ?)", setdata)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally: db.close()


