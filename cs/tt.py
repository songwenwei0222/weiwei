# coding:utf-8
import unittest
import requests
import HTMLTestRunner
# 禁用安全请求警告
#from requests.packages.urllib3.exceptions import InsecureRequestWarning
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Sjzx_login(unittest.TestCase):

     def login(self,username,pwd,type="2",UCD002="BK002" ):

          url="http://192.168.168.163:8888/user/pwdlogin4sso"
          h={
              "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
              "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
              "Accept-Language": "zh-CN",
              "Accept-Encoding":"gzip, deflate" ,
              "Accept": "*/*",
              "Connection":"Keep-Alive",
              "Cookie":"_accountcompany=18671539041; _passwordcompany=123456; _LastLoginTypeCompany=1; _accountperson=18671539041; _passwordperson=123456; _ LastLoginTypePerson=1"
              }

          d={
              "from": "",
               "DLID":username,
               "UCC002":pwd,
               "type":type,
               "UCD002":UCD002
              }

          res=requests.post(url,headers=h,data=d)
          result1 = res.content    # 字节输出
          print result1
          print  res.json()
          return res.json()        # 返回json


     def test_login1(self):

          username="18671539041"
          pwd="E10ADC3949BA59ABBE56E057F20F883E"
          result = self.login(username,pwd)

          self.assertEqual(result["IsOK"], True)

     def test_login2(self):
        #测试登录：正确账号，错误密码
        username="18671539041"
        pwd="E10ADC3949BA59ABBE56E057F20F88"
        result = self.login(username,pwd)
        self.assertEqual(result["IsOK"], False)



