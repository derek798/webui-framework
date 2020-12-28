#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import yaml
from config.conf import cm


class Element:
    """获取元素"""

    def __init__(self, name):
        self.name = name
        self.element_path = cm.element_file(self.name)
        with open(self.element_path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getitem__(self, item):
        """获取属性"""
        data = self.data.get(item)
        if data:
            name, value = data.split('==')
            return name, value
        raise ArithmeticError("{}.yaml中不存在关键字：{}".format(self.name, item))


if __name__ == '__main__':
    search = Element('search')
    print(search['搜索框'])
