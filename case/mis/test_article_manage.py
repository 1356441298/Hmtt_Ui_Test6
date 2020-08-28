import pytest

import config
from page.mis.mis_aritical_page import MisAtcalProxy
from page.mis.mis_home_page import MisHomePage
from page.mis.mis_login_page import MisLoginProxy
from utils import DriverUtils, is_element_exist

@pytest.mark.run(order=103)
class TestArticalMana:
    # 类级别初始化方法
    def setup_class(self):
        # 打开浏览器
        self.driver = DriverUtils.get_mis_driver()
        # 创建登录页面业务层对象
        self.login_page = MisLoginProxy()
        # 创建首页层对象
        self.home_page = MisHomePage()
        # 创建文章审核页面对象
        self.ad_page = MisAtcalProxy()

    # def setup(self):
    #     self.driver.get("http://ttmis.research.itcast.cn/#/home")

    # 测试审核文章的测试用例
    def test_pass(self):
        # 定义测试数据
        ari_title = config.PUB_ARTICLE_TITLE
        # 调用进入审核文章页面的业务方法
        self.home_page.to_article_page()
        # 调用审核文章的业务方法
        self.ad_page.test_pass(ari_title)
        # 断言
        assert is_element_exist(self.driver, "驳回")

    #     # 测试驳回文章的测试用例
    # @pytest.mark.run(order=3)
    # def test_reject(self):
    #     # 调用进入审核文章页面的业务方法
    #     self.home_page.to_article_page()
    #     # 调用驳回的业务方法
    #     self.ad_page.test_reject()
    #     # 断言
    #     assert is_element_exist(self.driver, "查看")

    # 关闭浏览器
    def teardown_class(self):
        DriverUtils.quit_mis_driver()
