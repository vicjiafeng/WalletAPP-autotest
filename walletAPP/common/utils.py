#! /usr/bin/python
# -*- coding: UTF-8 -*-
import json
import requests
from .conf import ConfigYaml


def logintimes_request():                                                           # 登录错误次数限制
    url = ConfigYaml().get_conf_url() + ConfigYaml().get_conf_path()['logintimes_path']
    headers = ConfigYaml().get_conf_headers()
    data = ConfigYaml().get_conf_data()['logintimes']['json']
    r = requests.post(url, headers=headers, json=data)
    res = r.text
    json_dict = json.loads(res)
    return json_dict


def login_request():                                                                      # 登录
    url = ConfigYaml().get_conf_url() + ConfigYaml().get_conf_path()['login_path']
    headers = ConfigYaml().get_conf_headers()
    data = ConfigYaml().get_conf_data()['login']['json']
    r = requests.post(url, headers=headers, json=data)
    res = r.text
    json_dict = json.loads(res)
    return json_dict

# 调用登录接口，获取token并设置全局变量
token = login_request()['data']['token']
# 获取登录态后测试用例集
class TestCase01(object):

    def setup(self):
        print('获取登录态后执行测试用例')

    def teardowm(self):
        print("测试用例执行完成")

    def history_request(self):                                                       # 发起查看交易历史
        url = ConfigYaml().get_conf_url() + ConfigYaml().get_conf_path()['history_path']
        authorization = token
        headers = {'authorization': authorization}
        payload = ConfigYaml().get_conf_data()['history']['payload']
        r = requests.get(url, headers=headers, params=payload)
        res = r.text
        json_dict = json.loads(res)
        return json_dict

    def transactiondetail_request(self):                                              # 查看交易历史详情
        url = ConfigYaml().get_conf_url() + ConfigYaml().get_conf_path()['transactiondetail_path']
        authorization = token
        headers = {'authorization': authorization}
        payload = TestCase01.history_request(self)['data']['transactionList'][0]['transactionId']
        data = {"transactionId": payload}
        r = requests.get(url, headers=headers, params=data)
        res = r.text
        json_dict = json.loads(res)
        return json_dict

    def banklist_request(self):                                                    # 发起查看银行列表
        url = ConfigYaml().get_conf_url() + ConfigYaml().get_conf_path()['banklist_path']
        authorization = token
        headers = {'authorization': authorization}
        r = requests.get(url, headers=headers)
        res = r.text
        json_dict = json.loads(res)
        return json_dict

    def profile_request(self):                                                     # 发起查看个人页
        url = ConfigYaml().get_conf_url() + ConfigYaml().get_conf_path()['profile_path']
        authorization = token
        headers = {'authorization': authorization}
        r = requests.get(url, headers=headers)
        res = r.text
        json_dict = json.loads(res)
        return json_dict

    def good_request(self):                                                     # 展示商城
        url = ConfigYaml().get_conf_url() + ConfigYaml().get_conf_path()['good_path']
        authorization = token
        headers = {'authorization': authorization}
        r = requests.post(url, headers=headers)
        res = r.text
        json_dict = json.loads(res)
        return json_dict

    def channellist_request(self):                                                     # 渠道列表页
        url = ConfigYaml().get_conf_url() + ConfigYaml().get_conf_path()['channellist_path']
        authorization = token
        headers = {'authorization': authorization}
        data = ConfigYaml().get_conf_data()['channellist']['json']
        r = requests.post(url, headers=headers, json=data)
        res = r.text
        json_dict = json.loads(res)
        return json_dict

    def addbank_request(self):                                                          # 发起添加银行
        url = ConfigYaml().get_conf_url() + ConfigYaml().get_conf_path()['addbank_path']
        authorization = token
        headers = {'authorization': authorization}
        data = ConfigYaml().get_conf_data()['addbank']['json']
        r = requests.post(url, headers=headers, json=data)
        res = r.text
        json_dict = json.loads(res)
        return json_dict

    def confirmbankinfo_request(self):                                                  # 提交新增银行
        url = ConfigYaml().get_conf_url() + ConfigYaml().get_conf_path()['confirmbankinfo_path']
        authorization = token
        headers = {'authorization': authorization}
        data = ConfigYaml().get_conf_data()['confirmbankinfo']['json']
        r = requests.post(url, headers=headers, json=data)
        res = r.text
        json_dict = json.loads(res)
        return json_dict

    def deletebankinfo_request(self):                                                 # 删除银行账户
        url = ConfigYaml().get_conf_url() + ConfigYaml().get_conf_path()['deletebankinfo_path']
        authorization = token
        headers = {'authorization': authorization}
        payload = TestCase01.banklist_request(self)['data'][0]['buid']
        data = {"buid": payload}
        r = requests.post(url=url, headers=headers, json=data)
        res = r.text
        json_dict = json.loads(res)
        return json_dict

    def saveprofile_request(self):                                                     # 更新邮箱或邮编
        url = ConfigYaml().get_conf_url() + ConfigYaml().get_conf_path()['saveprofile_path']
        authorization = token
        headers = {'authorization': authorization}
        data = ConfigYaml().get_conf_data()['saveprofile']['json1']
        r = requests.post(url=url, headers=headers, json=data)
        res = r.text
        json_dict = json.loads(res)
        return json_dict

    def sendsms_request(self):                                                          # 更新手机号-发送短信验证码
        url = ConfigYaml().get_conf_url() + ConfigYaml().get_conf_path()['saveprofile_path']
        authorization = token
        headers = {'authorization': authorization}
        data = ConfigYaml().get_conf_data()['sendsms']['json']
        r = requests.post(url=url, headers=headers, json=data)
        res = r.text
        json_dict = json.loads(res)
        return json_dict

    def channel_request(self):
        url = ConfigYaml().get_conf_url() + ConfigYaml().get_conf_path()['channel_path']
        authorization = token
        headers = {'authorization': authorization}
        payload = ConfigYaml().get_conf_data()['channel']['payload1']
        r = requests.get(url, headers=headers, params=payload)
        res = r.text
        json_dict = json.loads(res)
        return json_dict

    def paytimes_request(self):                                                          # 验证交易次数
        url = ConfigYaml().get_conf_url() + ConfigYaml().get_conf_path()['paytimes_path']
        authorization = token
        headers = {'authorization': authorization}
        r = requests.post(url=url, headers=headers)
        res = r.text
        json_dict = json.loads(res)
        return json_dict

    def pixdirect_request(self):                                                          # PIX渠道提现
        url = ConfigYaml().get_conf_url() + ConfigYaml().get_conf_path()['pixdirect_path']
        authorization = token
        headers = {'authorization': authorization}
        data = ConfigYaml().get_conf_data()['pixdirect']['pass']
        r = requests.post(url=url, headers=headers, json=data)
        res = r.text
        json_dict = json.loads(res)
        return json_dict

    def resetwalletpwd_request(self):                                                      # 设置新支付密码
        url = ConfigYaml().get_conf_url() + ConfigYaml().get_conf_path()['resetwalletpwd_path']
        authorization = token
        headers = {'authorization': authorization}
        data = ConfigYaml().get_conf_data()['resetwalletpwd']['json']
        r = requests.post(url=url, headers=headers, json=data)
        res = r.text
        json_dict = json.loads(res)
        return json_dict

    def resetuserpwd_request(self):                                                         # 设置新登录密码
        url = ConfigYaml().get_conf_url() + ConfigYaml().get_conf_path()['resetuserpwd_path']
        authorization = token
        headers = {'authorization': authorization}
        data = ConfigYaml().get_conf_data()['resetuserpwd']['json']
        r = requests.post(url=url, headers=headers, json=data)
        res = r.text
        json_dict = json.loads(res)
        return json_dict


'''
# 注册需要短信验证码，需要捞日志，返回数据包含token，用于之后设置密码，填写个人信息
def register_request(self):
    url = ConfigYaml().get_conf_url() + ConfigYaml().get_conf_path()['register_path']
    headers = ConfigYaml().get_conf_headers()
    data = ConfigYaml().get_conf_data()['register']['json']
    r = requests.post(url, headers=headers, json=data)
    res = r.text
    json_dict = json.loads(res)
    return json_dict
'''