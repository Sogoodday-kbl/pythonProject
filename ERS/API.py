import json
import pytest
import requests
import yaml


class Test_Interface:

    def Get(self,InterfaceLink):
        #打开参数化文件，取其中一个数据
        with open ('../ERS/API.yaml',encoding='utf-8') as f:
            datas=yaml.safe_load(f)
            datas=datas[InterfaceLink]
        #打开这个数据中的url数据
        GetInterface=requests.get(datas['url'])
        assert datas['assert'] in GetInterface.json().values()

    @pytest.mark.parametrize("InterfaceLink",['ERSQA'])
    def test_Get(self,InterfaceLink):
        get1=Test_Interface()
        get1.Get(InterfaceLink)

    def Post(self,InterfaceLink):
        with open ('../ERS/API.yaml',encoding='utf-8') as f:
            datas=yaml.safe_load(f)
            datas=datas[InterfaceLink]

        for mainkey in datas:
            d = {}
            for item in datas[mainkey].split():
                key, value = item.split(':')
                d[key] = value
            datas[mainkey] = d

        payLoad=d.dictsToRemoveKeys(key[1],key[2])
        print (payLoad)
        PostInterface = requests.post(datas['url'], datas=payLoad)
        print(PostInterface.json())
            #del d[key[1],key[1],]
            #d.dictsToRemoveKeys()

    @pytest.mark.parametrize("InterfaceLink", ['ERSQA3'])
    def test_Post(self,InterfaceLink):
        post1 = Test_Interface()
        post1.Post(InterfaceLink)

####有没有普遍post的方法，通过yaml来取键值对参数呢
        #payLoad = json.dumps(payLoad)
        # paylod=dict(Parameters1=datas[''],Pwd=datas['Pwd'],companyname=datas['companyname'])
        # PostInterface=requests.post(datas['url'],datas=payLoad)
        # assert datas['assert'] in PostInterface.json().values()


# http请求类，最常用的get请求和post请求的公共写法
# class test_http:
#     def http_get_method(self, baseUrl):
#         res = requests.get(baseUrl)
#         res = res.text
#         # res = str(res)
#         return res
#
#     def http_post_method(self, baseUrl, headers, payLoad):
#         payLoad = json.dumps(payLoad)
#         res = requests.post(url=baseUrl, headers=headers, data=payLoad)
#         requests.post(url=baseUrl, headers=headers, data=payLoad)
#         res = res.text
#         res = str(res)

#
# #post接口请求示例
# def LoginERS():
#     paylod=dict(Mobile='17521170226',Pwd='123456',companyname='今天你完善信息了吗')
#     r=requests.post('https://userqa.1renshi.com/Account/LoginByPasswordWithCompanyName',data=paylod)
#
#     # get接口请求示例
#     r1 = requests.get('https://busapiqa.1renshi.com/Common/User/CompanyNameList?page=1&limit=10', cookies=r.cookies)
#     print(r.status_code)
#     print(r.text)
#     print(r1.json())
#     print(r.cookies)
#
# if __name__ == '__main__':
#     LoginERS()
#
#
#
#
#
# # class Sign:
# #     # 实例化session对象 SessionRequest
# #     SessionRequest = requests.session()
# #
# #     # post请求
# #     @classmethod
# #     def send_post(cls, url, data, headers):
# #         response = cls.SessionRequest.post(url=url, data=json.dumps(data), headers=headers)
# #         return response.json()
# #
# #     # get请求
# #     @classmethod
# #     def send_get(cls, url, params, headers):
# #         response = cls.SessionRequest.get(url=url, params=params, headers=headers)
# #         return response.json()
#
#
# #Python - 保持登录状态进行接口测试
# # 1.简单粗暴式。此方法比较小白，前提是已经通过fiddler抓包等方式拿到了cookie，然后直接塞进去。
#
# import requests
#
# trainsUrl = 'http://XXX.com/trains'
# headers = {
#     "Content-Type": "application/json;charset=UTF-8",
# }
# cookies = {
#     "XXXthor": "XXXXXX105a42"
# }
# prames = {
#     'depId': '1',
#     'arrId': '2',
#     'goDate': 'XXXX'
# }
# res = requests.get(url=trainsUrl, cookies=cookies, params=prames, headers=headers).json()
#
# #2.从登录接口获取,这种方式是先运行登录接口，然后从loginRes中获取cookies，以供后续接口使用。
#
# import requests
#
# loginUrl = "http://XXX.com/login"
# data1 = {
#      "userName": "157XXXX",
#      "userPwd": "XXXX"
# }
# headers = {
#      "Content-Type": "application/json;charset=UTF-8"
# }
# # 运行登录接口
# loginRes = requests.post(url=loginUrl, json=data1, headers=headers)
# trainsUrl = 'http://XXX.com/trains'
# parames = {
#     'depId': '1',
#     'arrId': '2',
#     'goDate': '1538100286000'
# }
# # 运行trainsUrl接口时，从loginRes中获取cookies
# res = requests.get(url=trainsUrl, params=parames, cookies=loginRes.cookies).json()
#
#
# #3.使用会话对象保持登录 - --摘自网络
#
# import requests
#
# # Session 会话对象
# # 会话对象让你能够跨请求保持某些参数。它也会在同一个 Session 实例发出的所有请求之间保持 cookie
# # 会话对象具有主要的 Requests API 的所有方法。你可以当成 Request去使用
# sessionRequest = requests.session()  # 实例化会话对象
# loginUrl = "http://XXX.com/login"
# data = {
#      "userName": "157XXXX",
#      "userPwd": "XXX"
# }
# headers = {
#     "Content-Type": "application/json;charset=UTF-8"
# }
# # 第二次请求的url
# trainsUrl = 'http://XXX/trains'
# parames = {
#     'depId': '1',
#     'arrId': '2',
#     'goDate': 'XXXXX'
# }
# # 登录
# resp = sessionRequest.post(url=loginUrl, json = data, headers = headers)
# # 请求trains接口
# trainsResp = sessionRequest.get(url=trainsUrl, params=parames)
