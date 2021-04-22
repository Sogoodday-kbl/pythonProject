import yaml
from selenium import webdriver
import time

class Open_url():
    #初始化浏览器
    def __init__(self,env):#打开壹人事网页
        # 加载文件，获取测试环境，获取环境中的测试链接，以及对应链接的账号密码数据,各个元素的路径
        with open('Test_001casedata.yaml', encoding='utf-8') as f:
            datas = yaml.safe_load(f)
            envdata = datas[env]
            buttondata = datas['buttonpath']
        # 实例化浏览器
        self.driver = webdriver.Chrome(r"C:\Users\win 10\Downloads\chromedriver_win32 (1)\chromedriver.exe")
        url = envdata['url']
        self.driver.get(url)
        time.sleep(2)
class Login(Open_url):
    def Login_Success(self, env):  # 登录壹人事网页
        # 加载文件，获取测试环境，获取环境中的测试链接，以及对应链接的账号密码数据,各个元素的路径
        with open('Test_001casedata.yaml', encoding='utf-8') as f:
            datas = yaml.safe_load(f)
            envdata = datas[env]
            buttondata = datas['buttonpath']
        self.driver.find_element_by_link_text(buttondata['Loginbypwd']).click();
        self.driver.find_element_by_id(buttondata['mobile']).send_keys(envdata['mobile']);
        self.driver.find_element_by_id(buttondata['pwd']).send_keys(envdata['pwd']);
        self.driver.find_element_by_id(buttondata['LoginButton']).click();
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/p[text()="'+envdata['companyname']+'"]').click();
        time.sleep(2)
        return self.driver

class FirstPage(Login):
    def go_to_Social_page(self):
        self.driver.find_element_by_link_text('社保代缴').click();
        # return Social_page(self.driver)

class TestDemo():
    def test_go_to_Social_page(self):
        self.ele = Login("QA").Login_Success("QA")
        self.ele.go_to_Social_page()

# if __name__ == '__main__':
#     Login("QA").Login_Success("QA")

def test_login():
    Login("QA").Login_Success("QA")



class FirstPage(Login):
    def go_to_Social_page(self):
        self.driver.find_element_by_link_text('社保代缴').click();
        #return Social_page(self.driver)

class TestDemo():
    def test_go_to_Social_page(self):
        self.ele=Login("QA").Login_Success("QA")
        self.ele.go_to_Social_page()


# class Social_page(Login):
#     def add_menber(self):
#         pass


#ele=<selenium.webdriver.chrome.webdriver.WebDriver (session="5169a0ec8d1643111d5accd1ec3ab1a9")>
#self=<ERSData.ERS_UIproject.MainPage.TestDemo object at 0x000002020015B278>
#异常(<class 'AttributeError'>, AttributeError("'TestDemo' object has no attribute 'Login'",), <traceback object at 0x000002020015D848>)