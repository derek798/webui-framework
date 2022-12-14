#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import yaml
from tools.times import run_time
from config.conf import cm


@run_time
def inspect_element():
    """审查所有的元素是否正确"""
    _path1 = cm.ELEMENT_PATH
    for i in os.listdir(_path1):
        _path2 = os.path.join(_path1, i)
        if os.path.isfile(_path2):
            with open(_path2, encoding='utf-8') as f:
                data = yaml.safe_load(f)
            for k in data.values():
                pattern, value = k.split('==')
                if pattern not in cm.LOCATE_MODE:
                    raise AttributeError('【%s】路径中【%s]元素没有指定类型' % (i, k))
                if pattern == 'xpath':
                    assert '//' in value, '【%s】路径中【%s]元素xpath类型与值不配' % (
                        i, k)
                if pattern == 'css':
                    assert '//' not in value, '【%s】路径中【%s]元素css类型与值不配' % (
                        i, k)
                if pattern in ('id', 'name', 'class'):
                    assert value, '【%s】路径中【%s]元素类型与值不匹配' % (i, k)


if __name__ == '__main__':
    inspect_element()
