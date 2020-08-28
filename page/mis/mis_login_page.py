from selenium.webdriver.common.by import By
from base.mis_base.base_page import BasePage, BaseHandle
from utils import DriverUtils

"""后台管理系统的登录界面"""


# 对象库层:管理维护页面的所有元素对象
class MisLoginPage(BasePage):
    # 在初始化方法中定义实例属性来管理元素对象的定位方式及对应的表达式
    def __init__(self):
        super().__init__()
        # 用户名输入框
        self.username = (By.NAME, "username")
        # 密码输入框
        self.password = (By.NAME, "password")
        # 登录按钮
        self.login_btn = (By.ID, "inp1")

    # 定义实例方法来找到的具体的元素对象
    # 找到用户名输入框
    def find_username(self):
        return self.find_elt(self.username)

    # 找到密码输入框
    def find_password(self):
        return self.find_elt(self.password)

    # 找到登录按钮
    def find_login_btn(self):
        return self.find_elt(self.login_btn)


# 操作层:专门封装元素对象的操作方法
class MisHandle(BaseHandle):
    def __init__(self):
        self.mis_login_page = MisLoginPage()

    # 输入用户名
    def input_username(self, username):
        self.input_text(self.mis_login_page.find_username(), username)

    # 输入密码
    def input_password(self, password):
        self.input_text(self.mis_login_page.find_password(), password)

    # 登录按钮的点击
    def click_login_btn(self):
        # 1.删除登录按钮元素对象的disabled属性
        js_str = "document.getElementById('inp1').removeAttribute('disabled')"
        DriverUtils.get_mis_driver().execute_script(js_str)
        # 2.点击登录按钮
        self.mis_login_page.find_login_btn().click()


# 业务层:连续调用多个操作层操作方法形成手工测试用例中的测试步骤部分操作
class MisLoginProxy:
    def __init__(self):
        self.mis_login_handle = MisHandle()

    # 定义登录方法
    def test_mis_login(self, username, password):
        # 输入用户名
        self.mis_login_handle.input_username(username)
        # 输入密码
        self.mis_login_handle.input_password(password)
        # 点击登录
        self.mis_login_handle.click_login_btn()
