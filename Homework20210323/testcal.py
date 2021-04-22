'''
1、补全计算器（加法，除法）的测试用例
2、使用数据驱动完成测试用例的自动生成
3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
坑1:除数为0的情况
坑2: 自己发现
'''''
import pytest
import random

class Calculator:

    def add(self,a,b):
        return a+b

    def div(self,a,b):
        if b==0:
            print("除数不能为0")
            return ("除数不能为0")
        else:
            return a/b


class TestCal:

    def setup(self):
        print ("开始计算了")

    def teardown(self):
        print ("计算结束了")

    #random.randint(0, 1001)

    @pytest.mark.parametrize("a,b,expect",[[1,2,3],[3,4,7],[-1,2,1],[0.1,0.2,0.3]])
    def test_add(self,a,b,expect):
        clac=Calculator()
        assert clac.add(a,b) ==expect

    @pytest.mark.parametrize("a,b,expect",[[2,1,2],[8,4,2],[-1,2,-0.5],[0.1,0.2,0.5],[0.1,0,'除数不能为0']])
    def test_div(self,a,b,expect):
        clac1=Calculator()
        assert clac1.div(a,b) ==expect


