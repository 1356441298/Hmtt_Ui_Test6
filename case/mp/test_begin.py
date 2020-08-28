import pytest
from utils import DriverUtils

@pytest.mark.run(order=1)
class TestBegin:
    def test_begin(self):
        # 将关闭浏览器驱动的开关关闭
        DriverUtils.change_mp_key(False)