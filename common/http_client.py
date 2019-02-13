import requests

import time
class Req:

    def __init__(self, headers=None, cookies=None, allow_redirects=True, proxies=None, verify=None, timeout=15, response_dict=False, response_str=False):
        self.headers = headers     # dict
        self.cookies = cookies  # dict
        self.allow_redirects = allow_redirects     # bool
        self.proxies = proxies # {'http': 'http://v_kinddong:abcd_1234@proxy.webank.com:8080','https': 'http://v_kinddong:abcd_1234@proxy.webank.com:8080'}
        self.verify = verify   #bool
        self.timeout = timeout  #int

        self.response_dict = response_dict
        self.response_str = response_str

        # http连接异常的场合，重新连接的次数，默认为3，可以动态设定
        self.iRetryNum = 3
        self.errorMsg = ""
        # 内容 = {用例编号：响应数据}
        self.responses = {}
        # 内容 = {用例编号：异常信息}
        self.resErr = {}


    def send(self, method, url,
             response_cookies=False, response_dict=False, response_str=False, response_ori=True,
             **kwargs):
        '''
        self, method='GET', url=None,
                 params_dict=None,
                 data=None, json=None, files=None, auth=None,
                 headers_dict=None, cookies=None, allow_redirects=None, proxies=None, verify=False, timeout=None, stream=None, cert=None,
                 response_cookies=False, response_json_to_dict=False, response_str=True

        # request的默认参数
        request(self, method, url,
            params=None, data=None, headers=None, cookies=None, files=None,
            auth=None, timeout=None, allow_redirects=True, proxies=None,
            hooks=None, stream=None, verify=None, cert=None, json=None):
        '''
        kwargs = self._get_kwargs(**kwargs)
        response = requests.request(method.lower(), url, **kwargs)
        response_method = self._get_response_method(response_cookies=response_cookies,
                                                    response_dict=response_dict,
                                                    response_str=response_str,
                                                    response_ori=response_ori)
        return response_method(response)

    def _get_kwargs(self, **kwargs):
        kwargs.setdefault('allow_redirects', self.allow_redirects)
        kwargs.setdefault('headers', self.headers)
        kwargs.setdefault('cookies', self.cookies)
        kwargs.setdefault('proxies', self.proxies)
        kwargs.setdefault('verify', self.verify)
        kwargs.setdefault('timeout', self.timeout)
        return kwargs

    def _get_response_method(self, **kwargs):
        # 返回response的方法
        if kwargs['response_dict']:
            return self._response_json_to_dict
        elif kwargs['response_cookies']:
            return self._response_cookies
        elif kwargs['response_str']:
            return self._response_str
        elif kwargs['response_ori']:
            return self._reponse_ori

    def _response_json_to_dict(self, response):
        # 返回json转换为dict
        return response.json()

    def _response_str(self, response):
        # 返回str
        return response.content.decode("unicode_escape")

    def _response_cookies(self, response):
        # 返回cookies
        # 返回requests.cookies.RequestsCookieJar实例
        # 可以直接传入 cookies参数去使用
        return response.cookies

    def _reponse_ori(self, response):
        # 返回原始的response
        return response

    def del_cookies(self):
        # 删除cookie
        # 设置为None之后，下次就不会请求，就不会带上初始化的cookie
        self.cookies = None
        return

    def set_cookies(self, cookies):
        # 设置cookie
        # cookies可以是dict，也可以是requests.cookies.RequestsCookieJar的实例
        self.cookies = cookies
        return

    def del_headers(self):
        # 删除headers
        self.headers = None

    def set_headers(self, headers_dict):
        # 设置headers
        self.headers = headers_dict

if __name__ == '__main__':
    req = Req()
    # r = req.send(method='get', url='http://httpbin.org/get', headers_dict={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'},
    #      proxies={'http': 'http://v_kinddong:abcd_1234@proxy.webank.com:8080',
    #               'https': 'http://v_kinddong:abcd_1234@proxy.webank.com:8080'},
    #      params_dict={'key1': '送送送', 'key2': '干嘛是'}, response_str=True)

    r = req.send(method="POST", url="http://httpbin.org/post", json = {'data':'哦哦'},
                 proxies={
                     'http': 'http://v_kinddong:abcd_1234@proxy.webank.com:8080',
                     'https': 'http://v_kinddong:abcd_1234@proxy.webank.com:8080'
                 },response_cookies=True)

    # r = req.send(method='get', url='https://fanyi.baidu.com', headers_dict={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'},
    #      proxies={'http': 'http://v_kinddong:abcd_1234@proxy.webank.com:8080',
    #               'https': 'http://v_kinddong:abcd_1234@proxy.webank.com:8080'}, response_str=True)
    print(r)