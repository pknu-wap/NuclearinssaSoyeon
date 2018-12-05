import requests

import json

from datetime import datetime, timedelta


headers = {"appKey" : "1e35c118-1297-49dd-84d4-b96b03c11ba9",

           "Accept-Language" : "ko",

           "Content-Type" : "application/json"}



print("사용자의 속력을 측정하겠습니다. 우선 출발지와 목적지를 선택해 주세요")

print("------------------------------------------------------------")

places={1:'가온관', 2:'건축관', 3:'공학1관', 4:'나래관', 5:'나비센터', 6:'누리관'

       , 7:'대운동장', 8:'대학극장', 9:'대학본부', 10:'동원장보고관', 11:'디자인관',12:'미래관',13:'부산창업카페'

       ,14:'세종1관',15:'세종2관',16:'수산과학관',17:'수산질병관리원',18:'수조실험동'

       ,19:'식품가공공장',20:'아름관',21:'양어장',22:'양어장관리사',23:'웅비관',24:'워커하우스',25:'위드센터'

       ,26:'인문사회경영관',27:'자연과학1관',28:'자연과학2관',29:'장영실관',30:'부경대학교 어린이집'

       ,31:'청운관',32:'체육관',33:'충무관',34:'테니스장',35:'풋살장',36:'학술정보관',37:'한솔관'

       ,38:'한어울터',39:'한울관',40:'해양공동연구관',41:'부산행복연합기숙사',42:'향파관',43:'호연관',44:'환경해양관'}


def print_places():

       for i in range(1, 11):

              print(i, ". ", places[i], sep="", end=' ')

       print("\n", end='')

       for i in range(11, 21):

              print(i, ". ", places[i], sep="", end=' ')

       print("\n", end='')

       for i in range(21, 31):

              print(i, ". ", places[i], sep="", end=' ')

       print("\n", end='')

       for i in range(31, 41):

              print(i, ". ", places[i], sep="", end=' ')

       print("\n", end='')

       for i in range(41, 45):

              print(i, ". ", places[i], sep="", end=' ')

       print("\n")

print_places()

def select_src() :

       start = input("출발지를 선택해 주세요. (1~44) ")

       return places[int(start)]



def select_dst():

       end = input("도착지를 선택해 주세요. (1~44) ")

       return places[int(end)]




src=select_src()

dst=select_dst()

POIsrc_param={"searchKeyword" : src,

              "areaLLCode" : "26",

              "areaLMCode" : "290",

              "resCoordType" : "WGS84GEO",

              "searchType" : "name",

              "searchtypCd" : "A",

              "radius" : 0,

              "reqCoordType" : "WGS84GEO",

              "centerLon" : "",

              "centerLat" : "",

              "multiPoint" : "N",

              }

POIdst_param={"searchKeyword" : dst,

              "areaLLCode" : "26",

              "areaLMCode" : "290",

              "resCoordType" : "WGS84GEO",

              "searchType" : "name",

              "searchtypCd" : "A",

              "radius" : 0,

              "reqCoordType" : "WGS84GEO",

              "centerLon" : "",

              "centerLat" : "",

              "multiPoint" : "N",

              }



srcCoordinate=requests.get("https://api2.sktelecom.com/tmap/pois?version=1&format=json", params=POIsrc_param, headers=headers)

dstCoordinate=requests.get("https://api2.sktelecom.com/tmap/pois?version=1&format=json", params=POIdst_param, headers=headers)

srcCoord=json.loads(srcCoordinate.text)

dstCoord=json.loads(dstCoordinate.text)



startX=srcCoord['searchPoiInfo']['pois']['poi'][0]["frontLon"]

startY=srcCoord['searchPoiInfo']['pois']['poi'][0]["frontLat"]

endX=dstCoord['searchPoiInfo']['pois']['poi'][0]["frontLon"]

endY=dstCoord['searchPoiInfo']['pois']['poi'][0]["frontLat"]



data={"startX":startX,

      "startY":startY,

      "angle":"",

      "endPoiId":"",

      "endX":endX,

      "endY":endY,

      "passList":"",

      "reqCoordType":"WGS84GEO",

      "startName":src,

      "endName":dst,

      "searchOption":"10",

      "resCoordType":"WGS84GEO",

      "gpsTime":"",

      "sort":"index"}



r= requests.post("https://api2.sktelecom.com/tmap/routes/pedestrian?version=1&format=json", params=data, headers=headers)



res=json.loads(r.text)

tdistance=res['features'][0]['properties']['totalDistance']

ttime=res['features'][0]['properties']['totalTime']



i=0

while(res['features'][i]['properties']['description']!='도착'):

    description=res['features'][i]['properties']['description']

    #print(description)

    i+=1



print(data['startName']+"에서", data['endName']+"까지","총 이동 거리는 약",tdistance,"m입니다.")

print("-------------------------------------------------------------")


now = datetime.now()


print("현재 출발 시간은",now,"입니다. \n\n지금부터 목적지까지 이동해주시기 바랍니다.")
print("목적지에 도착하면 stop을 눌러주세요.")

text = "목적지에 도착하면 stop을 눌러주세요"
while text != 'stop':
    print('-이동중 입니다-')
    text = input()

later = datetime.now()
times = (later-now)

print ("\n\n도착시간은",later,"입니다.\n\n총 걸린 시간은",times,"입니다.") 

print("-----------------------------------------------------------")
usertime = int(input("걸린시간(분)을 입력해주세요: "))

usertime_sec =  usertime*60

user_speed = tdistance/usertime_sec

print("------------------------------------------------------------")
print("사용자의 속력은", user_speed,"(m/sec)입니다.")
 

