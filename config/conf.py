#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
from selenium.webdriver.common.by import By
from tools.times import datetime_strftime


class ConfigManager(object):
    # 项目目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 日志目录
    LOG_PATH = os.path.join(BASE_DIR, 'logs')

    # 报告目录
    REPORT_PATH = os.path.join(BASE_DIR, 'report', 'report.html')

    ELEMENT_PATH = os.path.join(BASE_DIR, 'page_element')

    # 元素定位的类型
    LOCATE_MODE = {
        'css': By.CSS_SELECTOR,
        'xpath': By.XPATH,
        'name': By.NAME,
        'id': By.ID,
        'class': By.CLASS_NAME
    }

    # 邮件信息
    EMAIL_INFO = {
        'username': '1084502012@qq.com',  # 切换成你自己的地址
        'password': 'QQ邮箱授权码',
        'smtp_host': 'smtp.qq.com',
        'smtp_port': 465
    }

    # 收件人
    ADDRESSEE = [
        '1084502012@qq.com',
    ]

    @property
    def ini_file(self):
        # 配置文件
        _file = os.path.join(self.BASE_DIR, 'config', 'config.ini')
        if not os.path.exists(_file):
            raise FileNotFoundError("配置文件%s不存在！" % _file)
        return _file

    def element_file(self, name):
        """页面元素文件"""
        element_path = os.path.join(self.ELEMENT_PATH, '%s.yaml' % name)
        if not os.path.exists(element_path):
            raise FileNotFoundError("%s 文件不存在！" % element_path)
        return element_path

    @property
    def log_path(self):
        log_path = os.path.join(self.BASE_DIR, 'logs')
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        return os.path.join(log_path, "%s.log" % datetime_strftime())

    @property
    def screen_file(self):
        now_time = datetime_strftime("%Y%m%d%H%M%S")
        # 截图目录
        screenshot_dir = os.path.join(self.BASE_DIR, 'screen_capture')
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screen_path = os.path.join(screenshot_dir, "{}.png".format(now_time))
        return now_time, screen_path


cm = ConfigManager()
if __name__ == '__main__':
    print(cm.BASE_DIR)
