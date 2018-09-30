# from urllib import request
# import ssl
# import json
# gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
# # client_id 为官网获取的AK， client_secret 为官网获取的SK
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_' \
#        'type=client_credentials&client_id=RkgwyM7BU6VlrAfEM6FMvC7l&client_secret=KQ5vAdcNGul5FMyGfUudWwgGjkseo1Iw'
# req = request.Request(host)
# response = request.urlopen(req, context=gcontext).read().decode('UTF-8')
# result = json.loads(response)
# if (result):
#     print(result)

token={'scope': 'public vis-classify_dishes vis-classify_car brain_all_scope vis-classify_animal vis-classify_plant brain_object_detect brain_realtime_logo brain_dish_detect brain_car_detect brain_animal_classify brain_plant_classify brain_advanced_general_classify wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test权限 vis-classify_flower lpq_开放 cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base iop_autocar oauth_tp_app smartapp_smart_game_openapi oauth_sessionkey', 'expires_in': 2592000, 'session_key': '9mzdAvCQyIakJwxrTk5VnTMShJ3tY7NxRnnomKUcQ//X1cHg/U0TInjaFRrHIRsshaZyEeCA7t2MMYuEqyZX3zvuzlow/w==', 'access_token': '24.923858acb11cfb865cc04194a7e6bbad.2592000.1540295564.282335-14271675', 'session_secret': 'c1780390190a0d9f7df271d11867b633', 'refresh_token': '25.1b420238ab721e9d70b19d3058477830.315360000.1853063564.282335-14271675'}
import base64
import requests
host = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general'
headers={
   'Content-Type':'application/x-www-form-urlencoded'
}
host=host+'?access_token='+token['access_token']
f=open("D:/DatasetB_20180919/image.txt").readlines()
h1={}
h2=open("pred/baidu.txt",'w')
for i,x in enumerate(f):
    if i>=142:
        img=open("D:/DatasetB_20180919/test/"+x.strip('\t').strip('\n'),'rb')
        img=base64.b64encode(img.read())
        data={}
        data['access_token']=token
        data['image']=img
        res=requests.post(url=host,headers=headers,data=data)
        req=res.json()
        print(req)
        h1[x.strip('\t').strip('\n')]=req
        # h2.write(x.strip('\t').strip('\n')+'\t'+req+'\n')
h2.close()

