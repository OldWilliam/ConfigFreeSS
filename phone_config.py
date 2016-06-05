#Generate phone configuraton file

#1.conbine the original data like "aes-256-cfb:97396512@us1.iss.tf:443"
#2.encrypt it by base64
#3.gen qr_code by api
#  http://api.wwei.cn/wwei.html?data=weixin&apikey=20160605147782

import base64
import urllib
import json

apikey = '20160605147782'
qr_api = 'api.wwei.cn/wwei.html'

#parama:list
#return:str
def combine(origin_data):
    data = origin_data[3]+':'+origin_data[2]+'@'+origin_data[0]+':'+origin_data[1]
    return data
    print '\n\n######combined data: '+data

#parama:str
#return:str
def encrypt(data):
   return base64.b64encode(data)

def main(origin):
    data = combine(origin)
    data = encrypt(data)
    data = 'ss://'+ data
    params = urllib.urlencode({'data':data,'apikey':apikey})
    f = urllib.urlopen(qr_api,params)
    json_str =  f.read()
    f.close()
    response_dic = json.loads(json_str)
    qr_url = response_dic['data']['qr_filepath']
    print qr_url


