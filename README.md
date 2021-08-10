#  接口测试框架

##  testAPI

###  Config

* config.ini 用来存放邮件配置内容
* HTMLTestRunner.py 用于python单元测试框架的TestRunner.
* readConfig.py 用来读取config.ini 文件中的内容

###  Data

*  Data 目录主要是为了存放数据，比如：业务需要的测试数

  

###  Log

*  log.txt 用来存放用例执行的日志

  

###  Reports

*  Report目录用来存放用例执行的测试报告

###  Test_cases

*  Test_tasks.py用来存放具体的测试用例

  

###  Utils

*  excles.py 用来读取Data目录下的data.xls数据文件

* page.py 用来重写请求方法（get,post, delete),定义生成日志的方法。

  

###  runMain.py

*  启动程序文件