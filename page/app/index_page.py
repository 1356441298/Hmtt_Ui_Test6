"""黑马头条首页-手机端"""
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from base.app_base.base_page import BasePage
from utils import DriverUtils


# 对象库层
class IndexPage(BasePage):
    def __init__(self):
        super().__init__()
        # 频道元素对象
        self.channel_option = (By.XPATH, "//*[contains(@text,'{}')]")
        # 频道区域对象
        self.channel_area = (By.XPATH, "//*[@class='android.widget.HorizontalScrollView']")
        # 第一条文章的元素对象
        self.first_article = (By.XPATH, "//*[contains(@text,'评论')]")

    # 找频道元素对象
    def find_channel_option(self, channel_name):
        # return self.find_elt(self.channel_option)
        return DriverUtils.get_app_driver().find_element(self.channel_option[0],
                                                         self.channel_option[1].format(channel_name))
        # 找频道区域对象

    def find_channel_area(self):
        return self.find_elt(self.channel_area)

    # 找第一条文章的元素对象
    def find_first_article(self):
        return self.find_elt(self.first_article)


# 操作层
class IndexHandle:

    def __init__(self):
        self.index_page = IndexPage()

    # 选择频道
    def check_channel_option(self, channel_name):
        # 获取区域元素的位置
        area_element = self.index_page.find_channel_area()
        x = area_element.location["x"]
        y = area_element.location["y"]
        # 获取区域元素的大小
        w = area_element.size["width"]
        h = area_element.size["height"]
        # 计算起始按住的滑动点坐标
        start_y = y + h * 0.5
        start_x = x + w * 0.8
        # 计算目标位置的坐标
        end_y = start_y
        end_x = x + w * 0.2

        while True:
            # 滑动前先获取一次界面信息
            page_old = DriverUtils.get_app_driver().page_source
            # 在当前区域内查找我们想选择的频道元素对象
            try:
                # 如果能找到则点击
                self.index_page.find_channel_option(channel_name).click()
                break
            # 如果找不到则继续滑动页面
            except Exception as e:
                DriverUtils.get_app_driver().swipe(start_x, start_y, end_x, end_y, 3000)
                # 再获取一次界面信息和滑动前相等
                page_new = DriverUtils.get_app_driver().page_source
                # 如果滑动后的页面信息和滑动之前的相等则抛出异常没找到目标选项
                if page_new == page_old:
                    raise NoSuchElementException("没有找到{}的频道")

    # 点击第一条文章
    def click_first_article(self):
        self.index_page.find_first_article().click()


# 业务层
class IndexProxy:
    def __init__(self):
        self.index_handle = IndexHandle()

    # 根据频道查询文章方法
    def test_qari_by_channel(self, channel_name):
        # 选择频道
        self.index_handle.check_channel_option(channel_name)
        # 点击第一条文章
        self.index_handle.click_first_article()
