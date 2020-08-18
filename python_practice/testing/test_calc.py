from typing import List

import pytest
import yaml
from python_practice.py_test.calculator import calculator

'''
pytest 命名规则
文件名：以test_开头；test_*.py
类名：以Test开头
方法名：以test_开头
'''


def get_datas():
    with open('./data/calc.yml', encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        adddatas = mydatas['add']['datas']
        myids = mydatas['add']['myids']
    return [adddatas, myids]



class TestCalc:

    def setup_class(self):
        print("开始计算")
        self.calc = calculator()

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.add
    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, a, b, expect):
        '''
        测试相加
        '''
        # calc = calculator()
        result = self.calc.add(a, b)
        assert expect == result

    # @pytest.mark.parametrize('a,b,expect', [
    #     (0.1, 0.2, 0.3),
    #     # (0, 10, 10),
    # ])
    # # 使用round保留两位小数
    # def test_add_float(self, a, b, expect):
    #     '''
    #     测试相加
    #     '''
    #     # calc = calculator()
    #     result = round(self.calc.add(a, b),2)
    #     assert expect == result

    # @pytest.mark.sub
    # def test_sub(self):
    #     '''
    #     测试相减
    #     '''
    #     # calc = calculator()
    #     result = self.calc.sub(7, 1)
    #     assert 6 == result
    #
    # @pytest.mark.mul
    # def test_mul(self):
    #     '''
    #     测试相乘
    #     '''
    #     # calc = calculator()
    #     result = self.calc.mul(3, 8)
    #     assert 24 == result
    #

