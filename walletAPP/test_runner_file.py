#! /usr/bin/python
# -*- coding: UTF-8 -*-
import pytest, allure, os, logging
import traceback
from .common.utils import *
from .common.log_util import Logger

# logger函数变量
logger = Logger().get_log()

#测试用例集合
@allure.feature("wallet客户端登录")
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
    def test_logintimes_request(self):
        with allure.step("1、登录页输入手机号"):
            print('输入登录手机号')
        with allure.step("2、触发logintimes接口"):
            login_times_response = logintimes_request()
            print('调用登录统计次数接口,日志打印返回数据')
        with allure.step("3、执行断言"):
            try:
                assert 'success' == login_times_response['message']
                logger.info("断言成功，返回message为: {}".format(login_times_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("断言失败，实际返回message：{}".format(login_times_response['message']))
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
    def test_login_request(self):
        with allure.step("1、登录界面输入账户密码"):
            print('输入登录手机号密码')
        with allure.step("2、点击登录按键"):
            login_response = login_request()
            print('调用登录接口，日志打印返回数据')
        with allure.step("3、执行断言"):
            try:
                assert 'success' == login_response['message']
                logger.info("断言成功，返回message为: {}".format(login_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("断言失败，实际返回message：{}".format(login_response['message']))
                raise

@allure.feature("wallet客户端数据展示")
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
                logger.info("断言成功，返回message为: {}".format(profile_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("断言失败，实际返回message：{}".format(profile_response['message']))
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
                logger.info("断言成功，返回message为: {}".format(good_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("断言失败，实际返回message：{}".format(good_response['message']))
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
                logger.info("断言成功，返回message为: {}".format(channel_list_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("断言失败，实际返回message：{}".format(channel_list_response['message']))
                raise

@allure.feature("wallet客户端账单相关")
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
    def test_history_request(self):
        with allure.step("1、获取请求头Authorization"):
            print('获取请求头Authorization')
        with allure.step("2、进入History列表页"):
            history_response = TestCase01.history_request(self)
            print('调用账单列表接口,日志打印返回数据')
        with allure.step("3、执行断言"):
            try:
                assert 'success' == history_response['message']
                logger.info("断言成功，返回message为: {}".format(history_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("断言失败，实际返回message：{}".format(history_response['message']))
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
                logger.info("断言成功，返回message为: {}".format(transaction_detail_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("断言失败，实际返回message：{}".format(transaction_detail_response['message']))
                raise

@allure.feature("wallet客户端银行账户相关")
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
            try:
                assert 'success' == bank_list_response['message']
                logger.info("断言成功，返回message为: {}".format(bank_list_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("断言失败，实际返回message：{}".format(bank_list_response['message']))
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
                logger.info("断言成功，返回message为: {}".format(add_bank_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("断言失败，实际返回message：{}".format(add_bank_response['message']))
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
                logger.info("断言成功，返回message为: {}".format(confirm_bankinfo_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("断言失败，实际返回message：{}".format(confirm_bankinfo_response['message']))
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
                logger.info("断言成功，返回message为: {}".format(delete_bankinfo_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("断言失败，实际返回message：{}".format(delete_bankinfo_response['message']))
                raise

@allure.feature("wallet客户端维护个人信息")
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
                logger.info("断言成功，返回message为: {}".format(save_profile_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("断言失败，实际返回message：{}".format(save_profile_response['message']))
                raise

    @pytest.mark.run(order=13)
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
                logger.info("断言成功，返回message为: {}".format(sms_send_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("断言失败，实际返回message：{}".format(sms_send_response['message']))
                raise

    @pytest.mark.run(order=14)
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
                logger.info("断言成功，返回message为: {}".format(reset_login_pwd_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("断言失败，实际返回message：{}".format(reset_login_pwd_response['message']))
                raise

    @pytest.mark.run(order=15)
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
                logger.info("断言成功，返回message为: {}".format(reset_wallet_pwd_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("断言失败，实际返回message：{}".format(reset_wallet_pwd_response['message']))
                raise

@allure.feature("wallet客户端提现")
class TestSuite6(object):
    @pytest.mark.run(order=16)
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
                logger.info("断言成功，返回message为: {}".format(channel_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("断言失败，实际返回message：{}".format(channel_response['message']))
                raise

    @pytest.mark.run(order=17)
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
                logger.info("断言成功，返回message为: {}".format(pay_times_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("断言失败，实际返回message：{}".format(pay_times_response['message']))
                raise

    @pytest.mark.run(order=18)
    @pytest.mark.withdrawCase
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
            try:
                assert "The withdraw amount can't be lower than R$0.50" == pix_direct_response['message']
                logger.info("断言成功，返回message为: {}".format(pix_direct_response['message']))
            except Exception as e:
                s = traceback.format_exc()
                logger.info("使用traceback输出异常: {}".format(s))
                logger.exception("断言失败，实际返回message：{}".format(pix_direct_response['message']))
                raise


if __name__ == '__main__':
    pytest.main(['--alluredir', './report'])
    os.system('allure generate  report -o ./report/html --clean')
