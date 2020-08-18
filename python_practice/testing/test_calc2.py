# __author:dalanlan
# data:2020/8/18
from typing import List
import pytest
import yaml
from python_practice.py_test.calculator import calculator


def get_datas():
    with open('./data/calc1.yml', encoding='utf-8') as f:
        mydatas1 = yaml.safe_load(f)
        divdatas = mydatas1['div']['datas']
        myids = mydatas1['div']['myids']
    return [divdatas, myids]


class TestCalc1:

    def setup_class(self):
        print("开始计算")
        self.calc = calculator()

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.div
    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    def test_div(self, a, b, expect):
        '''
        测试相除
        '''
        # calc = calculator()
        result = self.calc.div(a, b)
        assert expect == result
