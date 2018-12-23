# -*- coding: UTF-8 -*-
# @Time       : 2018/12/23 13:56
# @Author     : Weiqiang.long
# @File       : test_post.py
# @Software   : PyCharm
# @Description: 
# @TODO       : 创建文章
import pprint
import unittest, requests

from requests.auth import HTTPBasicAuth


class Test_Post(unittest.TestCase):
    '''测试文章接口'''

    def setUp(self):
        self.base_url = "http://XXXXXX:8000/wp-json/wp/v2/"

        # 鉴权账号、密码
        self.basicAuth_name = 'test'
        self.basicAuth_password = '0Jnp SokY KZkX Zpx2 zWtQ HQzj'

        self.data = {
            'title': 'test-test-update',
            'content': 'test api-publish-update'
        }



    def get(self, path, data=None):
        url = self.base_url + path
        pprint.pprint('请求地址为:{0}'.format(url))
        res = requests.get(url=url, params=data)
        # pprint.pprint('接口返回数据为:{0}'.format(res.json()))
        return res

    def post(self, path, data):
        url = self.base_url + path
        pprint.pprint('请求地址为:{0}'.format(url))
        res = requests.post(url=url, data=data, auth=HTTPBasicAuth(self.basicAuth_name, self.basicAuth_password))
        # pprint.pprint('接口返回数据为:{0}'.format(res.json()))
        return res

    def delete(self, path, data=None):
        url = self.base_url + path
        pprint.pprint('请求地址为:{0}'.format(url))
        res = requests.delete(url=url, params=data, auth=HTTPBasicAuth(self.basicAuth_name, self.basicAuth_password))
        # pprint.pprint('接口返回数据为:{0}'.format(res.json()))
        return res



    def test_1_get_one_post(self):
        '''获取最新的一篇文章'''
        data = {'per_page': 1}
        res = self.get('posts', data=data)
        result = res.json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(result), data['per_page'])
        self.assertEqual(result[0]['status'], 'publish')


    def test_2_create_one_post(self):
        '''新增一篇文章'''
        data = {
            'title': 'test-test-test',
            'content': 'test api-publish',
            'status': 'publish'
        }
        res = self.post('posts', data=data)
        result = res.json()
        # 将文章id作为全局变量，后面操作会用到此id
        global post_id
        post_id = result['id']
        # print(post_id)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(result['title']['raw'], data['title'])
        self.assertEqual(result['content']['raw'], data['content'])
        self.assertEqual(result['status'], data['status'])



    def test_3_get_id_post(self):
        '''通过指定id获取文章详情'''
        id = post_id
        res = self.get('posts/{0}'.format(id))
        result = res.json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(result['id'], id)


    def test_4_update_one_post(self):
        '''更新一篇文章'''
        id = post_id
        res = self.post('posts/{0}'.format(id), data=self.data)
        result = res.json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(result['id'], id)
        self.assertEqual(result['title']['raw'], self.data['title'])
        self.assertEqual(result['content']['raw'], self.data['content'])


    def test_5_delete_one_post(self):
        '''删除一篇文章'''
        id = post_id
        res = self.delete('posts/{0}'.format(id), data={'force': 'true'})   # force：是否绕过垃圾并强行删除
        result = res.json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(result['deleted'], True)
        self.assertEqual(result['previous']['id'], id)
        # print(self.data)
        self.assertEqual(result['previous']['title']['raw'], self.data['title'])
        self.assertEqual(result['previous']['content']['raw'], self.data['content'])


if __name__ == '__main__':
    unittest.main()




