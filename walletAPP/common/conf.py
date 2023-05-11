#! /usr/bin/python
# -*- coding: UTF-8 -*-
import os
from .handleYaml import YamlHandler

# 获取当前项目绝对路径
current = os.path.abspath(__file__)
base_dir = os.path.dirname(os.path.dirname(current))
# 定义config目录的路径
_config_path = base_dir+os.sep+"config"
# 定义conf.yml文件的路径
_config_file = _config_path+os.sep+"config.yml"


# 获取文件路径函数
def get_config_path():
    return _config_path


# 获取文件函数
def get_config_file():
    return _config_file


# 读取配置文件
class ConfigYaml:
    def __init__(self):
        self.config = YamlHandler(get_config_file()).get_yaml_data()

    # 获取请求url
    def get_conf_url(self):
        return self.config['urls']['prod_url']

    # 获取请求路径
    def get_conf_path(self):
        return self.config['paths']

    # 获取请求头
    def get_conf_headers(self):
        return self.config['head']['headers']

    # 获取请求体
    def get_conf_data(self):
        return self.config['data']

