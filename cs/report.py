# coding:utf-8
import unittest
import HTMLTestRunner

def all_case():

     case_dir = "D:\\test\\case"  #用例脚本存放路劲
     testcase = unittest.TestSuite()

     discover = unittest.defaultTestLoader.discover(case_dir,

                                                     pattern="test*.py",

                                                     top_level_dir=None)
     for test_suite in discover:
               for test_case in test_suite:
                  # 添加用例到testcase
                   testcase.addTests(test_case)
     print testcase
     return testcase

if __name__ == "__main__":
   #runner = unittest.TextTestRunner()
   report_path = "D:\\test\\sww\\result.html"  #测试报告路劲
   fp = open(report_path, "wb")
   runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                              title=u'这是我的自动化测试报告',
                              description=u'用例执行情况：')

   runner.run(all_case())
   fp.close()



