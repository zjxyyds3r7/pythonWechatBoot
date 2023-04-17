import http.client, urllib, json
import pickle
import random

l = pickle.load(open('list.pkl', 'rb'))
def getRainbow():
    """
    conn = http.client.HTTPSConnection('apis.tianapi.com')  # 接口域名
    params = urllib.parse.urlencode({'key': 'api的key'})
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    conn.request('POST', '/caihongpi/index', params, headers)
    tianapi = conn.getresponse()
    result = tianapi.read()
    data = result.decode('utf-8')
    dict_data = json.loads(data)
    print(dict_data)
    return dict_data.get("result").get("content")"""
    
    return random.choice(l)

# for i in range(1000):
#     l.append(getRainbow())
#     with open('list.pkl', 'wb') as f:
#         pickle.dump(l, f, 0)


# print(len(l))
if __name__ == "__main__":
    print(getRainbow())
