# 后台管理系统-内容审核页面
import time

from utils import check_channel_option, DriverUtils
from selenium.webdriver.common.by import By
from base.mis_base.base_page import BasePage, BaseHandle


# 对象库层
class MisAtcalPage(BasePage):
    def __init__(self):
        super().__init__()
        # 文章标题搜索输入框
        self.ari_title_box = (By.CSS_SELECTOR, "[placeholder*='文章']")
        # 选择频道
        # 查询结束时间去掉
        self.no_time_btn=(By.CSS_SELECTOR,".el-icon-circle-close")
        # 查询按钮
        self.query_btn = (By.XPATH, "//*[text()='查询']")
        # 通过按钮
        self.pass_btn = (By.XPATH, "//*[text()='通过']")
        # 驳回按钮
        self.reject_btn = (By.XPATH, "//*[text()='驳回']")
        # 通过/驳回确认按钮
        self.con_rej_btn = (By.CSS_SELECTOR, ".el-button--primary")

    # 文章标题搜索输入框
    def find_ari_title_box(self):
        return self.find_elt(self.ari_title_box)

    # 选择频道

    # 查询结束时间框
    def find_no_time_btn(self):
        return self.find_elt(self.no_time_btn)

    # 查询按钮
    def find_query_btn(self):
        return self.find_elt(self.query_btn)

    # 通过按钮
    def find_pass_btn(self):
        return self.find_elt(self.pass_btn)

    # 驳回按钮
    def find_reject_btn(self):
        return self.find_elt(self.reject_btn)

    # 确认按钮
    def find_con_rej_btn(self):
        return self.find_elt(self.con_rej_btn)


# 操作层
class MisAtcalHandle(BaseHandle):
    def __init__(self):
        self.mis_atcal_page = MisAtcalPage()

    # 文章标题搜索输入框输入
    def input_ari_title(self, ari_title):
        # 调用父类模拟输入的方法
        self.input_text(self.mis_atcal_page.find_ari_title_box(), ari_title)

    # 选择文章状态
    def check_ari_status(self, ari_status):
        # 调用utils中公用的下拉框选择方法
        check_channel_option(DriverUtils.get_mis_driver(), "请选择状态", ari_status)

     # 时间去除按钮点击
    def click_no_time_btn(self):
        self.mis_atcal_page.find_no_time_btn().click()

    # 查询按钮点击
    def click_query_btn(self):
        self.mis_atcal_page.find_query_btn().click()

    # 审核通过按钮点击
    def click_pass_btn(self):
        self.mis_atcal_page.find_pass_btn().click()

    # 驳回按钮点击
    def click_reject_btn(self):
        self.mis_atcal_page.find_reject_btn().click()

    # 确认按钮点击
    def click_con_rej_btn(self):
        self.mis_atcal_page.find_con_rej_btn().click()

# 业务层
class MisAtcalProxy:
    def __init__(self):
        self.mis_ati_handle=MisAtcalHandle()
    # 审核通过测试用例
    def test_pass(self,ari_title):
        # 2.输入搜索的文章名称
        self.mis_ati_handle.input_ari_title(ari_title)
        # 3.选择文章状态
        self.mis_ati_handle.check_ari_status("审核通过")
        time.sleep(2)
        # 点击时间去除叉号
        self.mis_ati_handle.click_no_time_btn()
        # 4.点击查询按钮
        self.mis_ati_handle.click_query_btn()
        time.sleep(3)
        # 5.点击通过按钮
        self.mis_ati_handle.click_pass_btn()
        time.sleep(3)
        # 6.点击提示框的确定按钮
        self.mis_ati_handle.click_con_rej_btn()
        time.sleep(3)
        # 7.选择文章状态
        self.mis_ati_handle.check_ari_status("审核通过")
        time.sleep(3)
        # 8.点击查询按钮
        self.mis_ati_handle.click_query_btn()
        time.sleep(3)

    # 审核未通过测试用例
    def test_reject(self):
        # 3.选择文章状态
        self.mis_ati_handle.check_ari_status("待审核")
        # 4.点击查询按钮
        self.mis_ati_handle.click_query_btn()
        time.sleep(3)
        # 5.点击驳回按钮
        self.mis_ati_handle.click_reject_btn()
        # 6.点击提示框的确定按钮
        self.mis_ati_handle.click_con_rej_btn()
        time.sleep(3)
        # 7.切换审核失败页面
        self.mis_ati_handle.check_ari_status("审核失败")
        # 8.点击查询按钮
        self.mis_ati_handle.click_query_btn()
        time.sleep(3)
