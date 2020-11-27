from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse
import pymysql
import time

# 초기값들 세팅
# RDS info
host = 'rds-mariadb-jolp.c4c7vriv1s2u.ap-northeast-2.rds.amazonaws.com'
port = 3306
username = 'admin'
password = 'xkzl1020'
database = 'finedust'

conn = pymysql.connect(host=host,
                       user=username,
                       password=password,
                       db=database,
                       port=port,
                       charset='utf8')


key = 'T%2BSKyJKmZyzmUWiFt%2F9YBFdL7nC3qKKrbwx2E0cJtsQL4Tp429jfVaYEIZqxmKcstLagRsBlT%2BMQ81SsAwr2Nw%3D%3D'
url1 = 'http://openapi.airkorea.or.kr/openapi/services/rest'
url2 = '/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey='


placelist = ['신암동', '시지동', '만촌동']
while (True):
    for placepick in placelist:
        place = parse.quote(placepick)
        placeuni = parse.unquote(place)
        M = '&numOfRows=1&pageNo=1&stationName=' + place + '&dataTerm=DAILY&ver=1.3'
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

        print('측정소: ' + placeuni)
        print('측정시간: ' + a)
        print('미세먼지 농도: ' + g + '㎍/㎥ ( ' + s + ' )')
        print('초미세먼지 농도: ' + i + '㎍/㎥ ( ' + t + ' )')
        # print('( 좋음: 1 ),( 보통: 2 ),( 나쁨: 3 ),( 매우나쁨: 4)')

        # 위도 경도 설정
        if placepick == '신암동':
            lat = 35.8898
            long = 128.633
        elif placepick == '시지동':
            lat = 35.8377
            long = 128.6975
        elif placepick == '만촌동':
            lat = 35.8837
            long = 128.6383

        cursor = conn.cursor()
        sql = 'INSERT INTO sinamdong(time, latitude, longitude, PM10, PM25, gradePM10, gradePM25) VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}")'.format(a, lat, long, g, i, s, t)
        cursor.execute(sql)
        conn.commit()
    time.sleep(3600)