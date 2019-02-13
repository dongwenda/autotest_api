import requests

class SessionReq:
    '''
    session 请求
    '''

    def __init__(self, headers_dict=None, **kwargs):
        self.session = requests.Session()
        if headers_dict:
            self.set_headers(headers_dict)

    def send(self, method, url,
             response_cookies=False, response_dict=False, response_str=False, response_ori=True,
             **kwargs):
        '''
        self, method, url,
            params=None, data=None, headers=None, cookies=None, files=None,
            auth=None, timeout=None, allow_redirects=True, proxies=None,
            hooks=None, stream=None, verify=None, cert=None, json=None,
             response_cookies=False, response_dict=False, response_str=True
        '''

        kwargs.setdefault('allow_redirects', True)
        kwargs.setdefault('verify', False)
        response = self.session.request(method.upper(), url, **kwargs)
        response_method = self._get_response_method(response_cookies=response_cookies,
                                                    response_dict=response_dict,
                                                    response_str=response_str,
                                                    response_ori=response_ori)
        return response_method(response)

    def _get_response_method(self, response_cookies, response_dict, response_str, response_ori):
        # 返回response的方法
        if response_dict:
            return self._response_json_to_dict
        elif response_cookies:
            return self._response_cookies
        elif response_str:
            return self._response_str
        elif response_ori:
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

    def set_headers(self, headers_dict):
        '''设置默认的请求头'''
        self.session.headers.update(headers_dict)

    def clear_headers(self):
        '''清除头信息'''
        self.session.headers.clear()

    def get_cookies(self):
        '''获取cookies'''
        return self.session.cookies.values()

    def get_cookie(self, name):
        '''获取cookies的某个值'''
        return self.session.cookies.get(name)