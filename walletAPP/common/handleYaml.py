#! /usr/bin/python
# -*- coding: UTF-8 -*-
import yaml, os


# 封装处理yaml文件的方法
class YamlHandler:

    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError('文件不存在')
        self._data = None

    # 读取yaml文件
    def get_yaml_data(self):
        if not self._data:
            with open(self.yamlf, 'rb') as f:
                self._data = yaml.safe_load(f)
            return self._data
    # 写入yaml文件
    # def write_yaml(self, data):
    #     with open(self.yamlf, 'w', encoding=self.encoding) as f:
    #         yaml.dump(data, stream=f, allow_unicode=True)
    #     return self._data


