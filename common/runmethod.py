# -*- coding: utf-8 -*-
import requests
import json

class RunMethod:

    def __init__(self):
        #self.res = self.run_main(method,url,data,headers)
        pass

    def post_main(self, url, data, headers):
        if headers != None:
            return requests.post(url=url,data=data,headers=headers).json()
        else:
            return requests.post(url=url,data=data).json()

    def get_main(self, url, data, headers):
        if headers != None:
            r = requests.get(url=url,params=data,headers=headers)
        else:
            r = requests.get(url=url,params=data)
        print(r.status_code)
        return r.json()

    def run_main(self,method,url,data=None,headers=None):
        if method == 'POST':
            res = self.post_main(url,data,headers)
        else:
            res = self.get_main(url,data,headers)
        return json.dumps(res,indent=2,ensure_ascii=False)

if __name__ == '__main__':
    url = 'https://www.apiopen.top/weatherApi'
    payload = {
        'city': '成都'
    }
    #r = RunMethod(url,'GET',payload)
    #print(r.res)
    '''
    url2 = 'http://httpbin.org/post'
    r2 = RunMethod('POST',url2,payload)
    print(r2.res)
    '''
    url2 = 'http://ost'
    r2 = RunMethod()
    r2.run_main('GET,',url2)

