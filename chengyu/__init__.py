import http.client, urllib, json

def getchengyures(userId,word):
    conn = http.client.HTTPSConnection('apis.tianapi.com')  #接口域名
    headers = {'Content-type':'application/x-www-form-urlencoded'}
    params = urllib.parse.urlencode({'key':'API的key',
                                     'word':word,'userid':userId})
    conn.request('POST','/chengyujielong/index',params,headers)
    tianapi = conn.getresponse()
    result = tianapi.read()
    data = result.decode('utf-8')
    dict_data = json.loads(data)
    print(dict_data)
    return dict_data['result']['tip']
