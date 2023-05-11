#! /usr/bin/python
# -*- coding: UTF-8 -*-
import pytest, allure, os, logging
from .common.utils import *
from .common.log_util import Logger

# logger函数变量
logger = Logger().get_log()
# epic描述
@allure.epic('wallet客户端接口自动化')
# 模块名称
@allure.feature("wallet客户端")
class TestClass(object):
    # 标记用例执行顺序
    @pytest.mark.run(order=1)
    # 用户故事
    @allure.story('客户端登录次数统计场景')
    # 用例等级
    @allure.severity(allure.severity_level.NORMAL)
    # 用例描述
    @allure.description('walletApp-Login times场景')
    # 用例步骤
    @allure.step('测试登录次数统计')
    # 用例标题
    @allure.title('walletApp-Login Times')
    def test_logintimes_request(self):
        with allure.step("1、登录页输入手机号"):
            print('输入登录手机号')
        with allure.step("2、触发logintimes接口"):
            login_times_response = logintimes_request()
            print('调用登录统计次数接口,日志打印返回数据')
        with allure.step("3、执行断言"):
            # 打印日志
            logger.info("登录次数统计响应数据：%s" % login_times_response)
            # 断言返回结果msg字段
            assert 'success' == login_times_response['message']
            print('统计成功')

    @pytest.mark.run(order=2)
    # 用户故事
    @allure.story('客户端登录场景')
    # 用例等级
    @allure.severity(allure.severity_level.BLOCKER)
    # 用例描述
    @allure.description('walletApp登录场景')
    # 测试步骤
    @allure.step('测试登录客户端')
    # 用例标题
    @allure.title('walletApp-Login')
    def test_login_request(self):
        with allure.step("1、登录界面输入账户密码"):
            print('输入登录手机号密码')
        with allure.step("2、点击登录按键"):
            login_response = login_request()
            print('调用登录接口，日志打印返回数据')
        with allure.step("3、执行断言"):
            logger.info("登录接口响应数据：%s" % login_response)
            assert 'success' == login_response['message']
            print('登录成功')

    @pytest.mark.run(order=3)
    # 用户故事
    @allure.story('展示用户个人信息场景')
    # 用例等级
    @allure.severity(allure.severity_level.CRITICAL)
    # 用例描述
    @allure.description('walletApp-Profile场景')
    # 测试步骤
    @allure.step('测试客户端查看个人页')
    # 用例标题
    @allure.title('walletApp-Profile')
    def test_profile_request(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、进入个人页"):
            profile_response = TestCase01.profile_request(self)
            print('调用profile接口，日志打印返回数据')
        with allure.step("3、执行断言"):
            logger.info("请求个人信息页响应数据：%s" % profile_response)
            assert 'success' == profile_response['message']
            print('查看个人页成功')

    @pytest.mark.skip('no need')
    @pytest.mark.run(order=4)
    # 用户故事
    @allure.story('首页展示商场场景')
    # 用例等级
    @allure.severity(allure.severity_level.NORMAL)
    # 用例描述
    @allure.description('walletApp-Market Goods场景')
    # 测试步骤
    @allure.step('测试客户端展示商城列表')
    # 用例标题
    @allure.title('walletApp-Market Goods')
    def test_good_request(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、调用商城列表接口"):
            good_response = TestCase01.good_request(self)
            print('调用接口成功，日志打印返回数据')
        with allure.step("3、执行断言"):
            logger.info("商城列表页响应数据：%s" % good_response)
            assert 'OK' == good_response['message']
            print('拉取商城列表成功')

    @pytest.mark.run(order=5)
    # 用户故事
    @allure.story('首页展示渠道列表页场景')
    # 用例等级
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('walletApp-Channel List场景')
    # 测试步骤
    @allure.step('测试客户端查询渠道列表')
    # 用例标题
    @allure.title('walletApp-Transaction Channel List')
    def test_channellist_request(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、调用渠道列表页接口"):
            channel_list_response = TestCase01.channellist_request(self)
            print('调用接口成功，日志打印返回数据')
        with allure.step("3、执行断言"):
            logger.info("渠道列表响应数据：%s" % channel_list_response)
            assert 'success' == channel_list_response['message']
            print('渠道列表页查询成功')

    @pytest.mark.run(order=6)
    # 用户故事
    @allure.story('用户查询账单场景')
    # 用例等级
    @allure.severity(allure.severity_level.CRITICAL)
    # 用例描述
    @allure.description('walletApp-Transaction History List场景')
    # 测试步骤
    @allure.step('测试客户端查看交易历史记录')
    # 用例标题
    @allure.title('walletApp-Transaction History List')
    def test_history_request(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、进入History列表页"):
            history_response = TestCase01.history_request(self)
            print('调用交易列表接口,日志打印返回数据')
        with allure.step("3、执行断言"):
            logger.info("账单列表响应数据：%s" % history_response)
            assert 'success' == history_response['message']
            print('查看交易历史成功')

    @pytest.mark.run(order=7)
    # 用户故事
    @allure.story('用户查看账单详情场景')
    # 用例等级
    @allure.severity(allure.severity_level.CRITICAL)
    # 用例描述
    @allure.description('walletApp-View Transaction History场景')
    # 测试步骤
    @allure.step('测试客户端查看交易历史详情')
    # 用例标题
    @allure.title('walletApp-Transaction Detail')
    def test_transactiondetail_request(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、进入History列表页"):
            print('调用交易列表接口')
        with allure.step("3、点击列表页第一条记录，查看详情"):
            transaction_detail_response = TestCase01.transactiondetail_request(self)
            print('进入交易详情页,日志打印返回数据')
        with allure.step("4、执行断言"):
            logger.info("账单详情响应数据：%s" % transaction_detail_response)
            assert 'success' == transaction_detail_response['message']
            print('查看交易历史成功')

    @pytest.mark.run(order=8)
    # 用户故事
    @allure.story('用户查看银行账户列表场景')
    # 用例等级
    @allure.severity(allure.severity_level.CRITICAL)
    # 用例描述
    @allure.description('walletApp-Bank list场景')
    # 测试步骤
    @allure.step('测试客户端查看银行列表记录')
    # 用例标题
    @allure.title('walletApp-BankList')
    def test_banklist_request(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、进入bank列表页"):
            bank_list_response = TestCase01.banklist_request(self)
            print('调用bank列表接口,日志打印返回数据')
        with allure.step("3、执行断言"):
            logger.info("请求银行账户列表页响应数据：%s" % bank_list_response)
            assert 'success' == bank_list_response['message']
            print('查看银行列表成功')

    @pytest.mark.run(order=9)
    @allure.story('用户添加银行账户进入编辑页场景')
    # 用例等级
    @allure.severity(allure.severity_level.CRITICAL)
    # 用例描述
    @allure.description('walletApp-Add Bank Account场景')
    # 测试步骤
    @allure.step('测试客户端添加银行记录进入编辑页')
    # 用例标题
    @allure.title('walletApp-Add Bank Account')
    def test_addbank_request(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取login接口响应token')
        with allure.step("2、进入bank列表页"):
            print('调用bank列表接口')
        with allure.step('3、点击add bank按键'):
            add_bank_response = TestCase01.addbank_request(self)
            print('调用添加银行接口')
        with allure.step("4、执行断言"):
            logger.info("请求添加银行账户进入编辑页响应数据：%s" % add_bank_response)
            assert 'OK' == add_bank_response['message']
            print('调用addbank接口成功')

    @pytest.mark.run(order=10)
    @allure.story('用户新增银行账户场景')
    # 用例等级
    @allure.severity(allure.severity_level.CRITICAL)
    # 用例描述
    @allure.description('walletApp-Confirm Add Bank Account场景')
    # 测试步骤
    @allure.step('测试客户端提交添加银行记录')
    # 用例标题
    @allure.title('walletApp-Confirm Add Bank Account')
    def test_confirmbankinfo_request(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、进入bank列表页"):
            print('调用bank列表接口')
        with allure.step("3、点击add bank按键"):
            print('调用添加银行接口')
        with allure.step("4、提交申请"):
            confirm_bankinfo_response = TestCase01.confirmbankinfo_request(self)
            print('调用提交接口')
        with allure.step("5、执行断言"):
            logger.info("新增银行账户响应数据：%s" % confirm_bankinfo_response)
            assert 'success' == confirm_bankinfo_response['message']
            print('添加银行账户成功')

    @pytest.mark.run(order=11)
    @allure.story('用户删除银行账户场景')
    # 用例等级
    @allure.severity(allure.severity_level.CRITICAL)
    # 用例描述
    @allure.description('walletApp-Delete Bank Account场景')
    # 测试步骤
    @allure.step('测试客户端删除银行账户')
    # 用例标题
    @allure.title('walletApp-Delete Bank Account')
    def test_deletebankinfo_request(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、进入bank列表页"):
            print('调用bank列表接口')
        with allure.step("3、选中第一条银行账户"):
            print('查看银行账户详情')
        with allure.step("4、点击delete按键"):
            delete_bankinfo_response = TestCase01.deletebankinfo_request(self)
            print('调用删除账户接口')
        with allure.step("5、执行断言"):
            logger.info("删除银行账户响应数据：%s" % delete_bankinfo_response)
            assert 'success' == delete_bankinfo_response['message']
            print('删除银行账户成功')

    @pytest.mark.run(order=12)
    # 用户故事
    @allure.story('用户更新CEP或Email场景')
    # 用例等级
    @allure.severity(allure.severity_level.CRITICAL)
    # 用例描述
    @allure.description('walletApp更新个人信息场景')
    # 测试步骤
    @allure.step('测试更新用户邮箱或邮编')
    # 用例标题
    @allure.title('walletApp-Update&Save Profile')
    def test_saveprofile_request(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、发起更新CEP请求"):
            print('输入新的CEP')
        with allure.step("3、点击change CEP按键"):
            save_profile_response = TestCase01.saveprofile_request(self)
            print('调用保存接口')
        with allure.step("4、执行断言"):
            logger.info("更新个人信息响应数据：%s" % save_profile_response)
            assert 'OK' == save_profile_response['message']
            print('更新/保存成功')

    @pytest.mark.run(order=13)
    # 用户故事
    @allure.story('用户发送短信验证码场景(更新手机号)')
    # 用例等级
    @allure.severity(allure.severity_level.CRITICAL)
    # 用例描述
    @allure.description('walletApp更新个人手机号发送smsOTP场景')
    # 测试步骤
    @allure.step('测试更新用户手机号发送短信验证码')
    # 用例标题
    @allure.title('walletApp-Send SMS')
    def test_sendsms_request(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、输入未注册过的新手机号"):
            print('输入新的手机号')
        with allure.step("3、点击send按键"):
            sms_send_response = TestCase01.sendsms_request(self)
            print('调用发送smsOTP')
        with allure.step("4、执行断言"):
            logger.info("调用短信平台响应数据：%s" % sms_send_response)
            assert 'OK' == sms_send_response['message']
            print('发送短信验证码成功')

    @pytest.mark.run(order=14)
    # 用户故事
    @allure.story('首页选择PIX渠道场景')
    # 用例等级
    @allure.severity(allure.severity_level.BLOCKER)
    # 用例描述
    @allure.description('walletApp首页选择提现渠道')
    # 测试步骤
    @allure.step('测试用户选择PIX提现渠道')
    # 用例标题
    @allure.title('walletApp-PIX Channel Selected')
    def test_channel_request(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、点击PIX渠道"):
            channel_response = TestCase01.channel_request(self)
            print('选择PIX提现渠道')
        with allure.step("3、执行断言"):
            logger.info("渠道列表响应数据：%s" % channel_response)
            assert 'success' == channel_response['message']
            print('发送短信验证码成功')

    @pytest.mark.run(order=15)
    # 用户故事
    @allure.story('提现次数统计场景')
    # 用例等级
    @allure.severity(allure.severity_level.CRITICAL)
    # 用例描述
    @allure.description('walletApp发起PIX提现渠道，验证转账次数统计限制')
    # 测试步骤
    @allure.step('测试用户选择PIX提现渠道，验证交易次数限制')
    # 用例标题
    @allure.title('walletApp-PIX Withdraw Times Collection')
    def test_paytimes_request(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、点击PIX渠道，查看交易次数限制"):
            pay_times_response = TestCase01.paytimes_request(self)
            print('查看交易次数限制')
        with allure.step("3、执行断言"):
            logger.info("每日提现次数限制统计接口响应数据：%s" % pay_times_response)
            assert 'success' == pay_times_response['message']
            print('发送短信验证码成功')

    @pytest.mark.run(order=16)
    # 用户故事
    @allure.story('用户完成PIX渠道提现场景')
    # 用例等级
    @allure.severity(allure.severity_level.BLOCKER)
    # 用例描述
    @allure.description('walletApp发起PIX提现渠道（提现金额小于0.50，报错提示）')
    # 测试步骤
    @allure.step('测试用户进行PIX渠道提现-')
    # 用例标题
    @allure.title('walletApp-PIX Withdraw Failed due to minimal withdraw amount')
    def test_pixdirect_request(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、输入提现账户"):
            print('选择EVP类型')
        with allure.step("3、输入EVP账号"):
            print('完成EVP账号输入')
        with allure.step("4、输入交易密码"):
            pix_direct_response = TestCase01.pixdirect_request(self)
            print('输入错误交易密码')
        with allure.step("5、执行断言"):
            logger.info("PIX提现响应数据：%s" % pix_direct_response)
            assert "The withdraw amount can't be lower than R$0.50" == pix_direct_response['message']
            print('发送短信验证码成功')

    @pytest.mark.run(order=17)
    @allure.story('用户重置支付密码场景')
    # 用例等级
    @allure.severity(allure.severity_level.NORMAL)
    # 用例描述
    @allure.description('walletApp-Reset payment password场景')
    # 测试步骤
    @allure.step('测试客户端重置支付密码')
    # 用例标题
    @allure.title('walletApp-Reset Wallet Payment Password')
    def test_resetwalletpwd_request(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、进入个人页"):
            print('进入个人详情页')
        with allure.step("3、点击Payment password"):
            print('进入支付密码设置页')
        with allure.step("4、设置新支付密码"):
            print('新支付密码更新完成')
        with allure.step("5、点击confirm按键"):
            reset_wallet_pwd_response = TestCase01.resetwalletpwd_request(self)
            print('提交修改申请')
        with allure.step("6、执行断言"):
            logger.info("重置支付密码响应数据：%s" % reset_wallet_pwd_response)
            assert 'success' == reset_wallet_pwd_response['message']
            print('更新支付密码成功')

    @pytest.mark.run(order=18)
    @allure.story('用户重置登录密码场景')
    # 用例等级
    @allure.severity(allure.severity_level.CRITICAL)
    # 用例描述
    @allure.description('walletApp-Reset login password场景')
    # 测试步骤
    @allure.step('测试客户端重置登录密码')
    # 用例标题
    @allure.title('walletApp-Reset Login Password')
    def test_resetuserpwd_request(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、进入个人页"):
            print('进入个人详情页')
        with allure.step("3、点击login password"):
            print('进入登录密码设置页')
        with allure.step("4、设置新登录密码"):
            print('新登录密码更新完成')
        with allure.step("5、点击confirm按键"):
            reset_login_pwd_response = TestCase01.resetuserpwd_request(self)
            print('提交修改申请')
        with allure.step("6、执行断言"):
            # 断言返回结果msg字段
            logger.info("重置登录密码响应数据：%s" % reset_login_pwd_response)
            assert 'success' == reset_login_pwd_response['message']
            print('更新登录密码成功')


if __name__ == '__main__':
    pytest.main(['--alluredir', './report'])
    os.system('allure generate  report -o ./report/html --clean')
