#(경로표시), 거리, (이동속도는 데이터로 넘겨줌) = 시간 표시

import requests
import json

headers = {"appKey" : "1e35c118-1297-49dd-84d4-b96b03c11ba9",
           "Accept-Language" : "ko",
           "Content-Type" : "application/json"}

#passList,gpsTime,endPoiId,angle:선택값

data={"startX":"129.1008722",
       "startY":"35.13469",
       "angle":"",
       "speed":"30",
       "endPoiId":"",
       "endX":"129.1031735",
       "endY":"35.134032",
       "passList":"",
       "reqCoordType":"WGS84GEO",
       "startName":"부경대학교 대연캠퍼스 향파관",
       "endName":"부경대학교 대연캠퍼스 대운동장",
       "searchOption":"10",
       "resCoordType":"WGS84GEO",
       "gpsTime":"",
       "sort":"index"}

r= requests.post("https://api2.sktelecom.com/tmap/routes/pedestrian?version=1&format=json", params=data, headers=headers)

##print response
#print (r.json())

res=json.loads(r.text)
tdistance=res['features'][0]['properties']['totalDistance']
ttime=res['features'][0]['properties']['totalTime']
print(data['startName']+"에서", data['endName']+"까지","총 이동 거리는 약",tdistance,"m 이며, 총 소요 시간은 약",ttime//60,"분 입니다.")