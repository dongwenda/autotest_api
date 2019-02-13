import base64
import requests
import unittest
import re

postID = 0


class TestWP(unittest.TestCase):

    def setUp(self):
        encodestr = base64.b64encode('dongwenda:YHC5 b0TU iFcX cDpN mzS4 cfC3'.encode('utf-8')).decode('utf-8')
        self.headers = {'Authorization': 'Basic ' + encodestr}
        self.url = 'http://203.195.161.41:8000/'

    def test_create_a_post(self):
        # 创建文章
        api = self.url + 'wp-json/wp/v2/posts'
        payload = {
            'stastus': 'publish',
            'title': '创建一篇文章',
            'content': '创建内容！！！',
            'author': '1'
        }
        r = requests.post(api, data=payload, headers=self.headers)
        res_str=r.content.decode("unicode_escape")
        #print(res_str)
        self.assertIn(payload['title'], res_str, "==Failed==")
        postID = re.search(r'"id":(\d+),', res_str).group(1)

    def test_retrieve_a_post(self):
        # 获取一篇文章
        api = self.url + 'wp-json/wp/v2/posts/'
        payload = {
            'id': postID
        }
        r = requests.get(api, params=payload, headers=self.headers)
        res_str = r.content.decode("unicode_escape")
        #print(res_str)

    def test_update_a_post(self):
        # 编辑文章
        api = self.url + 'wp-json/wp/v2/posts/'
        payload = {
            'id': postID,
            'content': '编辑文章！！！！'
        }
        r = requests.get(api, params=payload, headers=self.headers)
        res_str = r.content.decode("unicode_escape")
        #print(res_str)

    def test_delete_a_post(self):
        # 删除文章
        api = self.url + 'wp-json/wp/v2/posts/'+str(postID)
        r = requests.delete(api, headers=self.headers)
        res_str = r.content.decode("unicode_escape")
        print(res_str)


if __name__ == '__main__':
    unittest.main()