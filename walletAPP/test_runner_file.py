#! /usr/bin/python
# -*- coding: UTF-8 -*-
import pytest, allure, os, logging
import traceback
from .common.utils import *
from .common.log_util import Logger

# logger函数变量
logger = Logger().get_log()

#测试用例集合
@allure.feature("巴西市场-wallet客户端登录")
class TestSuite1(object):
    # 标记用例执行顺序
    @pytest.mark.run(order=1)
    # 用例标记名
    @pytest.mark.beforeloginCase
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
    def test_brazil_logintimes_request(self):
        with allure.step("1、登录页输入手机号"):
            print('输入登录手机号')
        with allure.step("2、触发logintimes接口"):
            login_times_response = brazil_logintimes_request()
            print('调用登录统计次数接口,日志打印返回数据')
        with allure.step("3、执行断言"):
            try:
                assert 'success' == login_times_response['message']
                logger.info("巴西市场-测试用例：登录次数统计接口-断言成功，返回message为: {}".format(login_times_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("巴西市场-测试用例：登录次数统计接口-断言失败，实际返回message：{}".format(login_times_response['message']))
                raise

    @pytest.mark.run(order=2)
    @pytest.mark.beforeloginCase
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
    def test_brazil_loginpwd_request(self):
        with allure.step("1、登录界面输入账户密码"):
            print('输入登录手机号密码')
        with allure.step("2、点击登录按键"):
            loginpwd_response = brazil_loginpwd_request()
            print('调用登录接口，日志打印返回数据')
        with allure.step("3、执行断言"):
            try:
                assert 'success' == loginpwd_response['message']
                logger.info("巴西市场-测试用例：登录接口-断言成功，返回message为: {}".format(loginpwd_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("巴西市场-测试用例：登录接口-断言失败，实际返回message：{}".format(loginpwd_response['message']))
                raise


@allure.feature("巴西市场-wallet客户端数据展示")
class TestSuite2(object):
    @pytest.mark.run(order=3)
    @pytest.mark.checkInfoCase
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
            try:
                assert 'success' == profile_response['message']
                logger.info("巴西市场-测试用例：个人页接口-断言成功，返回message为: {}".format(profile_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("巴西市场-测试用例：个人页接口-断言失败，实际返回message：{}".format(profile_response['message']))
                raise
    @pytest.mark.skip('no need')
    @pytest.mark.run(order=4)
    @pytest.mark.checkInfoCase
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
            try:
                assert 'success' == good_response['message']
                logger.info("巴西市场-测试用例：商城列表接口-断言成功，返回message为: {}".format(good_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("巴西市场-测试用例：商城列表接口-断言失败，实际返回message：{}".format(good_response['message']))
                raise

    @pytest.mark.run(order=5)
    # 用户故事
    @allure.story('首页展示渠道列表页场景')
    @pytest.mark.checkInfoCase
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
            try:
                assert 'success' == channel_list_response['message']
                logger.info("巴西市场-测试用例：渠道列表接口-断言成功，返回message为: {}".format(channel_list_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("巴西市场-测试用例：渠道列表接口-断言失败，实际返回message：{}".format(channel_list_response['message']))
                raise


@allure.feature("巴西市场-wallet客户端账单相关")
class TestSuite3(object):
    @pytest.mark.run(order=6)
    @pytest.mark.transactionCase
    # 用户故事
    @allure.story('用户查询账单场景')
    # 用例等级
    @allure.severity(allure.severity_level.CRITICAL)
    # 用例描述
    @allure.description('walletApp-Transaction History List场景')
    # 测试步骤
    @allure.step('测试客户端查看账单列表')
    # 用例标题
    @allure.title('walletApp-Transaction History List')
    def test_transactionlist_request(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、进入History列表页"):
            transactionlist_response = TestCase01.transactionlist_request(self)
            print('调用账单列表接口,日志打印返回数据')
        with allure.step("3、执行断言"):
            try:
                assert 'success' == transactionlist_response['message']
                logger.info("巴西市场-测试用例：账单列表接口-断言成功，返回message为: {}".format(transactionlist_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("巴西市场-测试用例：账单列表接口-断言失败，实际返回message：{}".format(transactionlist_response['message']))
                raise
    @pytest.mark.run(order=7)
    @pytest.mark.transactionCase
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
            try:
                assert 'success' == transaction_detail_response['message']
                logger.info("巴西市场-测试用例：账单详情接口-断言成功，返回message为: {}".format(transaction_detail_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("巴西市场-测试用例：账单详情接口断言失败，实际返回message：{}".format(transaction_detail_response['message']))
                raise


@allure.feature("巴西市场wallet客户端银行账户相关")
class TestSuite4(object):
    @pytest.mark.run(order=8)
    @pytest.mark.bankInfoCase
    # 用户故事
    @allure.story('用户查看银行账户列表场景')
    # 用例等级
    @allure.severity(allure.severity_level.CRITICAL)
    # 用例描述
    @allure.description('walletApp-Bank list场景')
    # 测试步骤
    @allure.step('测试客户端查看银行账户列表记录')
    # 用例标题
    @allure.title('walletApp-BankList')
    def test_banklist_request(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、进入bank列表页"):
            bank_list_response = TestCase01.banklist_request(self)
            print('调用bank列表接口,日志打印返回数据')
        with allure.step("3、执行断言"):
            try:
                assert 'success' == bank_list_response['message']
                logger.info("巴西市场-测试用例：银行账户列表接口-断言成功，返回message为: {}".format(bank_list_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("巴西市场-测试用例：银行账户列表接口-断言失败，实际返回message：{}".format(bank_list_response['message']))
                raise

    @pytest.mark.run(order=9)
    @pytest.mark.bankInfoCase
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
            try:
                assert 'OK' == add_bank_response['message']
                logger.info("巴西市场-测试用例：进入银行账户编辑页接口-断言成功，返回message为: {}".format(add_bank_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("巴西市场-测试用例：进入银行账户编辑页接口-断言失败，实际返回message：{}".format(add_bank_response['message']))
                raise

    @pytest.mark.run(order=10)
    @pytest.mark.bankInfoCase
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
            try:
                assert 'success' == confirm_bankinfo_response['message']
                logger.info("巴西市场-测试用例：添加银行账户接口-断言成功，返回message为: {}".format(confirm_bankinfo_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("巴西市场-测试用例：添加银行账户接口-断言失败，实际返回message：{}".format(confirm_bankinfo_response['message']))
                raise

    @pytest.mark.run(order=11)
    @pytest.mark.bankInfoCase
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
            try:
                assert 'success' == delete_bankinfo_response['message']
                logger.info("巴西市场-测试用例：删除银行账户接口-断言成功，返回message为: {}".format(delete_bankinfo_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("巴西市场-测试用例：删除银行账户接口-断言失败，实际返回message：{}".format(delete_bankinfo_response['message']))
                raise


@allure.feature("巴西市场-wallet客户端维护个人信息")
class TestSuite5(object):
    @pytest.mark.run(order=12)
    @pytest.mark.personInfoCase
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
            try:
                assert 'OK' == save_profile_response['message']
                logger.info("巴西市场-测试用例：维护个人信息接口-断言成功，返回message为: {}".format(save_profile_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("巴西市场-测试用例：维护个人信息接口-断言失败，实际返回message：{}".format(save_profile_response['message']))
                raise

    @pytest.mark.run(order=13)
    @pytest.mark.personInfoCase
    # 用户故事
    @allure.story('添加用户信息场景')
    # 用例等级
    @allure.severity(allure.severity_level.CRITICAL)
    # 用例描述
    @allure.description('walletApp添加用户信息场景')
    # 测试步骤
    @allure.step('测试添加用户信息')
    # 用例标题
    @allure.title('walletApp-Add Profile')
    def test_addprofile_request(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、发起添加用户信息请求"):
            print('更新email/CEP')
        with allure.step("3、点击submit按键"):
            add_profile_response = TestCase01.addprofile_request(self)
            print('调用保存接口')
        with allure.step("4、执行断言"):
            try:
                assert 'success' == add_profile_response['message']
                logger.info("巴西市场-测试用例：添加用户信息接口-断言成功，返回message为: {}".format(
                    add_profile_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("巴西市场-测试用例：添加用户信息接口-断言失败，实际返回message：{}".format(
                    add_profile_response['message']))
                raise
    @pytest.mark.run(order=14)
    @pytest.mark.personInfoCase
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
            try:
                assert 'OK' == sms_send_response['message']
                logger.info("巴西市场-测试用例：发送smsOTP接口-断言成功，返回message为: {}".format(sms_send_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("巴西市场-测试用例：发送smsOTP接口断言失败，实际返回message：{}".format(sms_send_response['message']))
                raise

    @pytest.mark.run(order=15)
    @pytest.mark.personInfoCase
    # 用户故事
    @allure.story('用户忘记支付密码发送短信场景')
    # 用例等级
    @allure.severity(allure.severity_level.CRITICAL)
    # 用例描述
    @allure.description('walletApp忘记支付密码发送短信场景')
    # 测试步骤
    @allure.step('测试用户忘记支付密码发送短信验证码')
    # 用例标题
    @allure.title('walletApp-Send SMS')
    def test_forgotpaypwdsms_request(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、个人页-更新支付密码"):
            print('触发forgot password')
        with allure.step("3、点击forgot password按键"):
            forgotpaypwdsms_response = TestCase01.forgotpaypwdsms_request(self)
            print('调用发送smsOTP')
        with allure.step("4、执行断言"):
            try:
                assert 'The limit of verification codes sent has been reached.' == forgotpaypwdsms_response['message']
                logger.info("巴西市场-测试用例：发送smsOTP接口-断言成功，返回message为: {}".format(
                    forgotpaypwdsms_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("巴西市场-测试用例：发送smsOTP接口断言失败，实际返回message：{}".format(
                    forgotpaypwdsms_response['message']))
                raise

    @pytest.mark.run(order=16)
    @pytest.mark.personInfoCase
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
            try:
                assert 'success' == reset_login_pwd_response['message']
                logger.info("巴西市场-测试用例：重置登录密码接口-断言成功，返回message为: {}".format(reset_login_pwd_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("巴西市场-测试用例：重置登录密码接口-断言失败，实际返回message：{}".format(reset_login_pwd_response['message']))
                raise

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
            try:
                assert 'success' == reset_wallet_pwd_response['message']
                logger.info("巴西市场-测试用例：重置支付密码接口-断言成功，返回message为: {}".format(reset_wallet_pwd_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("巴西市场-测试用例：重置支付密码接口-断言失败，实际返回message：{}".format(reset_wallet_pwd_response['message']))
                raise

@allure.feature("巴西市场-wallet客户端提现")
class TestSuite6(object):
    @pytest.mark.run(order=18)
    @pytest.mark.withdrawCase
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
            try:
                assert 'success' == channel_response['message']
                logger.info("巴西市场-测试用例：选择提现渠道接口-断言成功，返回message为: {}".format(channel_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("巴西市场-测试用例：选择提现渠道接口-断言失败，实际返回message：{}".format(channel_response['message']))
                raise

    @pytest.mark.run(order=19)
    @pytest.mark.withdrawCase
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
            try:
                assert 'success' == pay_times_response['message']
                logger.info("巴西市场-测试用例：验证交易次数接口-断言成功，返回message为: {}".format(pay_times_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("巴西市场-测试用例：验证交易次数接口-断言失败，实际返回message：{}".format(pay_times_response['message']))
                raise

    @pytest.mark.run(order=20)
    @pytest.mark.withdrawCase
    # 用户故事
    @allure.story('用户完成PIX渠道提现场景')
    # 用例等级
    @allure.severity(allure.severity_level.BLOCKER)
    # 用例描述
    @allure.description('walletApp发起PIX提现渠道（输入错误交易密码）')
    # 测试步骤
    @allure.step('测试用户进行PIX渠道提现-')
    # 用例标题
    @allure.title('walletApp-PIX Withdraw Failed due to wrong payment pwd')
    def test_pixdirect_request(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、输入提现账户"):
            print('选择EVP类型')
        with allure.step("3、输入邮箱"):
            print('完成邮箱输入')
        with allure.step("4、输入交易密码"):
            pix_direct_response = TestCase01.pixdirect_request(self)
            print('输入错误交易密码')
        with allure.step("5、执行断言"):
            try:
                assert "The password or account is incorrect. Please try again." == pix_direct_response['message']
                logger.info("巴西市场-测试用例：pix提现接口-断言成功，返回message为: {}".format(pix_direct_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("巴西市场-测试用例：pix提现接口-断言失败，实际返回message：{}".format(pix_direct_response['message']))
                raise

    @pytest.mark.run(order=21)
    @pytest.mark.withdrawCase
    # 用户故事
    @allure.story('用户进行银行账户提现场景')
    # 用例等级
    @allure.severity(allure.severity_level.BLOCKER)
    # 用例描述
    @allure.description('walletApp发起银行账户渠道提现（输入错误交易密码）')
    # 测试步骤
    @allure.step('测试用户进行PIX渠道提现-')
    # 用例标题
    @allure.title('walletApp-PIX Withdraw Failed due to wrong payment pwd')
    def test_banktransfer_request(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、选择银行账户"):
            print('选择银行账户')
        with allure.step("3、输入交易密码"):
            banktransfer_response = TestCase01.banktransfer_request(self)
            print('输入错误交易密码')
        with allure.step("5、执行断言"):
            try:
                assert "The password or account is incorrect. Please try again." == banktransfer_response['message']
                logger.info(
                    "巴西市场-测试用例：银行账户提现接口-断言成功，返回message为: {}".format(banktransfer_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception(
                    "巴西市场-测试用例：银行账户提现接口-断言失败，实际返回message：{}".format(banktransfer_response['message']))
                raise

@allure.feature("墨西哥市场-wallet客户端登录")
class TestSuite7(object):

    @pytest.mark.run(order=22)
    # 用例标记名
    @pytest.mark.beforeloginCase
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
    def test_mexico_logintimes_request(self):
        with allure.step("1、登录页输入手机号"):
            print('输入登录手机号')
        with allure.step("2、触发logintimes接口"):
            login_times_response = mexico_logintimes_request()
            print('调用登录统计次数接口,日志打印返回数据')
        with allure.step("3、执行断言"):
            try:
                assert 'success' == login_times_response['message']
                logger.info(
                    "墨西哥市场-测试用例：登录次数统计接口-断言成功，返回message为: {}".format(login_times_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception(
                    "墨西哥市场-测试用例：登录次数统计接口-断言失败，实际返回message：{}".format(login_times_response['message']))
                raise

    @pytest.mark.run(order=23)
    @pytest.mark.beforeloginCase
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
    def test_mexico_loginpwd_request(self):
        with allure.step("1、登录界面输入账户密码"):
            print('输入登录手机号密码')
        with allure.step("2、点击登录按键"):
            loginpwd_response = mexico_loginpwd_request()
            print('调用登录接口，日志打印返回数据')
        with allure.step("3、执行断言"):
            try:
                assert 'success' == loginpwd_response['message']
                logger.info("墨西哥市场-测试用例：登录接口-断言成功，返回message为: {}".format(loginpwd_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("墨西哥市场-测试用例：登录接口-断言失败，实际返回message：{}".format(loginpwd_response['message']))
                raise


@allure.feature("墨西哥市场wallet客户端银行账户相关")
class TestSuite8(object):

    @pytest.mark.run(order=24)
    @pytest.mark.bankInfoCase
    # 用户故事
    @allure.story('用户查看银行账户列表场景')
    # 用例等级
    @allure.severity(allure.severity_level.CRITICAL)
    # 用例描述
    @allure.description('walletApp-Bank list场景')
    # 测试步骤
    @allure.step('测试客户端查看银行账户列表记录')
    # 用例标题
    @allure.title('walletApp-BankList')
    def test_banklist_request_mexico(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、进入bank列表页"):
            bank_list_response = TestCase02.banklist_request_mexico(self)
            print('调用bank列表接口,日志打印返回数据')
        with allure.step("3、执行断言"):
            try:
                assert 'success' == bank_list_response['message']
                logger.info(
                    "墨西哥市场-测试用例：银行账户列表接口-断言成功，返回message为: {}".format(bank_list_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception(
                    "墨西哥市场-测试用例：银行账户列表接口-断言失败，实际返回message：{}".format(bank_list_response['message']))
                raise

    @pytest.mark.run(order=25)
    @pytest.mark.bankInfoCase
    @allure.story('用户添加银行账户进入编辑页场景')
    # 用例等级
    @allure.severity(allure.severity_level.CRITICAL)
    # 用例描述
    @allure.description('walletApp-Add Bank Account场景')
    # 测试步骤
    @allure.step('测试客户端添加银行记录进入编辑页')
    # 用例标题
    @allure.title('walletApp-Add Bank Account')
    def test_addbank_request_mexico(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取login接口响应token')
        with allure.step("2、进入bank列表页"):
            print('调用bank列表接口')
        with allure.step('3、点击add bank按键'):
            add_bank_response = TestCase02.addbank_request_mexico(self)
            print('调用添加银行接口')
        with allure.step("4、执行断言"):
            try:
                assert 'OK' == add_bank_response['message']
                logger.info(
                    "墨西哥市场-测试用例：进入银行账户编辑页接口-断言成功，返回message为: {}".format(add_bank_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception(
                    "墨西哥市场-测试用例：进入银行账户编辑页接口-断言失败，实际返回message：{}".format(add_bank_response['message']))
                raise

    @pytest.mark.run(order=26)
    @pytest.mark.bankInfoCase
    @allure.story('用户新增银行账户场景')
    # 用例等级
    @allure.severity(allure.severity_level.CRITICAL)
    # 用例描述
    @allure.description('walletApp-Confirm Add Bank Account场景')
    # 测试步骤
    @allure.step('测试客户端提交添加银行记录')
    # 用例标题
    @allure.title('walletApp-Confirm Add Bank Account')
    def test_confirmbankinfo_request_mexico(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、进入bank列表页"):
            print('调用bank列表接口')
        with allure.step("3、点击add bank按键"):
            print('调用添加银行接口')
        with allure.step("4、提交申请"):
            confirm_bankinfo_response = TestCase02.confirmbankinfo_request_mexico(self)
            print('调用提交接口')
        with allure.step("5、执行断言"):
            try:
                assert 'success' == confirm_bankinfo_response['message']
                logger.info(
                    "墨西哥市场-测试用例：添加银行账户接口-断言成功，返回message为: {}".format(confirm_bankinfo_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("墨西哥市场-测试用例：添加银行账户接口-断言失败，实际返回message：{}".format(
                    confirm_bankinfo_response['message']))
                raise

    @pytest.mark.run(order=29)
    @pytest.mark.bankInfoCase
    @allure.story('用户删除银行账户场景')
    # 用例等级
    @allure.severity(allure.severity_level.CRITICAL)
    # 用例描述
    @allure.description('walletApp-Delete Bank Account场景')
    # 测试步骤
    @allure.step('测试客户端删除银行账户')
    # 用例标题
    @allure.title('walletApp-Delete Bank Account')
    def test_deletebankinfo_request_mexico(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、进入bank列表页"):
            print('调用bank列表接口')
        with allure.step("3、选中第一条银行账户"):
            print('查看银行账户详情')
        with allure.step("4、点击delete按键"):
            delete_bankinfo_response = TestCase02.deletebankinfo_request_mexico(self)
            print('调用删除账户接口')
        with allure.step("5、执行断言"):
            try:
                assert 'success' == delete_bankinfo_response['message']
                logger.info(
                    "墨西哥市场-测试用例：删除银行账户接口-断言成功，返回message为: {}".format(delete_bankinfo_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception(
                    "墨西哥市场-测试用例：删除银行账户接口-断言失败，实际返回message：{}".format(delete_bankinfo_response['message']))
                raise

@allure.feature("墨西哥市场-wallet客户端SPEI提现")
class TestSuite9(object):
    @pytest.mark.run(order=27)
    @pytest.mark.withdrawCase
    # 用户故事
    @allure.story('首页选择SPEI渠道场景')
    # 用例等级
    @allure.severity(allure.severity_level.BLOCKER)
    # 用例描述
    @allure.description('walletApp首页选择提现渠道')
    # 测试步骤
    @allure.step('测试用户选择SPEI提现渠道')
    # 用例标题
    @allure.title('walletApp-SPEI Channel Selected')
    def test_channel_request_mexico(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、点击PIX渠道"):
            channel_response = TestCase02.channel_request_mexico(self)
            print('选择PIX提现渠道')
        with allure.step("3、执行断言"):
            try:
                assert 'success' == channel_response['message']
                logger.info("墨西哥市场-测试用例：选择提现渠道接口-断言成功，返回message为: {}".format(channel_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception(
                    "墨西哥市场-测试用例：选择提现渠道接口-断言失败，实际返回message：{}".format(channel_response['message']))
                raise

    @pytest.mark.run(order=28)
    @pytest.mark.withdrawCase
    # 用户故事
    @allure.story('用户进行SPEI账户提现场景')
    # 用例等级
    @allure.severity(allure.severity_level.BLOCKER)
    # 用例描述
    @allure.description('walletApp发起SPEI账户渠道提现（输入错误交易密码）')
    # 测试步骤
    @allure.step('测试用户进行SPEI渠道提现-')
    # 用例标题
    @allure.title('walletApp-SPEI Withdraw Failed due to wrong payment pwd')
    def test_spei_withdraw_request_mexico(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、选择SPEI账户"):
            print('选择SPEI账户')
        with allure.step("3、输入交易密码"):
            spei_response = TestCase02.spei_withdraw_request_mexico(self)
            print('输入错误交易密码')
        with allure.step("5、执行断言"):
            try:
                assert "The password or account is incorrect. Please try again." == spei_response['message']
                logger.info(
                    "墨西哥市场-测试用例：SPEI账户提现接口-断言成功，返回message为: {}".format(
                        spei_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception(
                    "墨西哥市场-测试用例：SPEI账户提现接口-断言失败，实际返回message：{}".format(
                        spei_response['message']))
                raise

@allure.feature("墨西哥市场-wallet客户端维护个人信息")
class TestSuite10(object):
    @pytest.mark.run(order=30)
    @pytest.mark.personInfoCase
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
    def test_saveprofile_request_mexico(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、发起更新CEP请求"):
            print('输入新的CEP')
        with allure.step("3、点击change CEP按键"):
            save_profile_response = TestCase02.saveprofile_request_mexico(self)
            print('调用保存接口')
        with allure.step("4、执行断言"):
            try:
                assert 'OK' == save_profile_response['message']
                logger.info("墨西哥市场-测试用例：维护个人信息接口-断言成功，返回message为: {}".format(save_profile_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("墨西哥市场-测试用例：维护个人信息接口-断言失败，实际返回message：{}".format(save_profile_response['message']))
                raise

    @pytest.mark.run(order=31)
    @pytest.mark.personInfoCase
    # 用户故事
    @allure.story('添加用户信息场景')
    # 用例等级
    @allure.severity(allure.severity_level.CRITICAL)
    # 用例描述
    @allure.description('walletApp添加用户信息场景')
    # 测试步骤
    @allure.step('测试添加用户信息')
    # 用例标题
    @allure.title('walletApp-Add Profile')
    def test_addprofile_request_mexico(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、发起添加用户信息请求"):
            print('更新email/CEP')
        with allure.step("3、点击submit按键"):
            add_profile_response = TestCase02.addprofile_request_mexico(self)
            print('调用保存接口')
        with allure.step("4、执行断言"):
            try:
                assert 'success' == add_profile_response['message']
                logger.info("墨西哥市场-测试用例：添加用户信息接口-断言成功，返回message为: {}".format(
                    add_profile_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("墨西哥市场-测试用例：添加用户信息接口-断言失败，实际返回message：{}".format(
                    add_profile_response['message']))
                raise

    @pytest.mark.run(order=32)
    @pytest.mark.personInfoCase
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
    def test_sendsms_request_mexico(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、输入未注册过的新手机号"):
            print('输入新的手机号')
        with allure.step("3、点击send按键"):
            sms_send_response = TestCase02.sendsms_request_mexico(self)
            print('调用发送smsOTP')
        with allure.step("4、执行断言"):
            try:
                assert 'OK' == sms_send_response['message']
                logger.info("墨西哥市场-测试用例：发送smsOTP接口-断言成功，返回message为: {}".format(sms_send_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("墨西哥市场-测试用例：发送smsOTP接口断言失败，实际返回message：{}".format(sms_send_response['message']))
                raise

    @pytest.mark.run(order=33)
    @pytest.mark.personInfoCase
    # 用户故事
    @allure.story('用户忘记支付密码发送短信场景')
    # 用例等级
    @allure.severity(allure.severity_level.CRITICAL)
    # 用例描述
    @allure.description('walletApp忘记支付密码发送短信场景')
    # 测试步骤
    @allure.step('测试用户忘记支付密码发送短信验证码')
    # 用例标题
    @allure.title('walletApp-Send SMS')
    def test_forgotpaypwdsms_request_mexico(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、个人页-更新支付密码"):
            print('触发forgot password')
        with allure.step("3、点击forgot password按键"):
            forgotpaypwdsms_response = TestCase02.forgotpaypwdsms_request_mexico(self)
            print('调用发送smsOTP')
        with allure.step("4、执行断言"):
            try:
                assert 'success' == forgotpaypwdsms_response['message']
                logger.info("墨西哥市场-测试用例：发送smsOTP接口-断言成功，返回message为: {}".format(
                    forgotpaypwdsms_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("墨西哥市场-测试用例：发送smsOTP接口断言失败，实际返回message：{}".format(
                    forgotpaypwdsms_response['message']))
                raise

    @pytest.mark.run(order=34)
    @pytest.mark.personInfoCase
    @allure.story('用户重置登录密码场景')
    # 用例等级
    @allure.severity(allure.severity_level.CRITICAL)
    # 用例描述
    @allure.description('walletApp-Reset login password场景')
    # 测试步骤
    @allure.step('测试客户端重置登录密码')
    # 用例标题
    @allure.title('walletApp-Reset Login Password')
    def test_resetuserpwd_request_mexico(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、进入个人页"):
            print('进入个人详情页')
        with allure.step("3、点击login password"):
            print('进入登录密码设置页')
        with allure.step("4、设置新登录密码"):
            print('新登录密码更新完成')
        with allure.step("5、点击confirm按键"):
            reset_login_pwd_response = TestCase02.resetuserpwd_request_mexico(self)
            print('提交修改申请')
        with allure.step("6、执行断言"):
            try:
                assert 'success' == reset_login_pwd_response['message']
                logger.info("墨西哥市场-测试用例：重置登录密码接口-断言成功，返回message为: {}".format(reset_login_pwd_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("墨西哥市场-测试用例：重置登录密码接口-断言失败，实际返回message：{}".format(reset_login_pwd_response['message']))
                raise

    @pytest.mark.run(order=35)
    @allure.story('用户重置支付密码场景')
    # 用例等级
    @allure.severity(allure.severity_level.NORMAL)
    # 用例描述
    @allure.description('walletApp-Reset payment password场景')
    # 测试步骤
    @allure.step('测试客户端重置支付密码')
    # 用例标题
    @allure.title('walletApp-Reset Wallet Payment Password')
    def test_resetwalletpwd_request_mexico(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、进入个人页"):
            print('进入个人详情页')
        with allure.step("3、点击Payment password"):
            print('进入支付密码设置页')
        with allure.step("4、设置新支付密码"):
            print('新支付密码更新完成')
        with allure.step("5、点击confirm按键"):
            reset_wallet_pwd_response = TestCase02.resetwalletpwd_request_mexico(self)
            print('提交修改申请')
        with allure.step("6、执行断言"):
            try:
                assert 'success' == reset_wallet_pwd_response['message']
                logger.info("墨西哥市场-测试用例：重置支付密码接口-断言成功，返回message为: {}".format(reset_wallet_pwd_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("墨西哥市场-测试用例：重置支付密码接口-断言失败，实际返回message：{}".format(reset_wallet_pwd_response['message']))
                raise


@allure.feature("墨西哥市场-wallet客户端数据展示")
class TestSuite11(object):
    @pytest.mark.run(order=36)
    @pytest.mark.checkInfoCase
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
    def test_profile_request_mexico(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、进入个人页"):
            profile_response = TestCase02.profile_request_mexico(self)
            print('调用profile接口，日志打印返回数据')
        with allure.step("3、执行断言"):
            try:
                assert 'success' == profile_response['message']
                logger.info("墨西哥市场-测试用例：个人页接口-断言成功，返回message为: {}".format(profile_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("墨西哥市场-测试用例：个人页接口-断言失败，实际返回message：{}".format(profile_response['message']))
                raise

    @pytest.mark.run(order=37)
    # 用户故事
    @allure.story('首页展示渠道列表页场景')
    @pytest.mark.checkInfoCase
    # 用例等级
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('walletApp-Channel List场景')
    # 测试步骤
    @allure.step('测试客户端查询渠道列表')
    # 用例标题
    @allure.title('walletApp-Transaction Channel List')
    def test_channellist_request_mexico(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、调用渠道列表页接口"):
            channel_list_response = TestCase02.channellist_request_mexico(self)
            print('调用接口成功，日志打印返回数据')
        with allure.step("3、执行断言"):
            try:
                assert 'success' == channel_list_response['message']
                logger.info("墨西哥市场-测试用例：渠道列表接口-断言成功，返回message为: {}".format(channel_list_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception(
                    "墨西哥市场-测试用例：渠道列表接口-断言失败，实际返回message：{}".format(channel_list_response['message']))
                raise

    @pytest.mark.run(order=38)
    @pytest.mark.transactionCase
    # 用户故事
    @allure.story('用户查询账单场景')
    # 用例等级
    @allure.severity(allure.severity_level.CRITICAL)
    # 用例描述
    @allure.description('walletApp-Transaction History List场景')
    # 测试步骤
    @allure.step('测试客户端查看账单列表')
    # 用例标题
    @allure.title('walletApp-Transaction History List')
    def test_transactionList_request_mexico(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、进入History列表页"):
            transactionList_response = TestCase02.transactionList_request_mexico(self)
            print('调用账单列表接口,日志打印返回数据')
        with allure.step("3、执行断言"):
            try:
                assert 'success' == transactionList_response['message']
                logger.info("墨西哥市场-测试用例：账单列表接口-断言成功，返回message为: {}".format(transactionList_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception(
                    "墨西哥市场-测试用例：账单列表接口-断言失败，实际返回message：{}".format(transactionList_response['message']))
                raise


if __name__ == '__main__':
    pytest.main(['--alluredir', './report'])
    os.system('allure generate  report -o ./report/html --clean')
