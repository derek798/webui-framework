# web-UI 自动化测试示例


## 框架设计

- pytest
- selenium
- POM 模型


## 目录结构

    common                 ——公共类
    page                   ——Selenium基类，对selenium方法进行深度封装
    page_elements          ——页面元素yaml文件
    page_object            ——页面对象类
    TestCase               ——测试用例
    conf.py                ——各种固定配置
    conftest.py            ——pytest胶水文件
    pytest.ini             ——pytest配置文件


## 运行

- `cd 项目目录`

* MacOS 系统或 Linux 系统

- 在命令行输入`sh run_mac.sh`即可运行

* Windows 系统

- 在命令行输入`run_mac.bat`即可运行


## allure参数说明


- allure --alluredir `result-path`
  - --clean-alluredir 清除历史生成记录

- allure generate `result-path`
  - -c 生成报告前删除上一次生成的报告
  - -o 指定生成的报告目录
- allure open `report-path`