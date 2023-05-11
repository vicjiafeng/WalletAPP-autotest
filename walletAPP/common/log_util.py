# -*- coding: utf-8 -*-
import logging, time


class Logger:
    def __init__(self, level="DEBUG"):
        # 创建日志器对象
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level)

    def console_handler(self, level="DEBUG"):
        # 创建控制台的日志处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        # 处理器添加输出格式
        console_handler.setFormatter(self.get_formatter()[0])
        # 返回控制器
        return console_handler

    def file_handler(self, level="DEBUG"):
        # 创建文件的日志处理器
        file_handler = logging.FileHandler("./log/" + "walletAPP_auto_test.%s.log" % time.strftime("%Y-%m-%d"))
        file_handler.setLevel(level)
        # 处理器添加输出格式
        file_handler.setFormatter(self.get_formatter()[1])
        # 返回控制器
        return file_handler

    def get_formatter(self):
        """格式器"""
        console_fmt = logging.Formatter(fmt="%(name)s--->%(levelname)s--->%(asctime)s--->%(message)s")
        file_fmt = logging.Formatter(fmt="%(lineno)d--->%(name)s--->%(levelname)s--->%(asctime)s--->%(message)s")
        # 返回的是一个元组
        return console_fmt, file_fmt

    def get_log(self):
        # 日志器中添加控制台处理器
        self.logger.addHandler(self.console_handler())
        # 日志器中添加文件处理器
        self.logger.addHandler(self.file_handler())
        # 返回日志实例对象
        return self.logger


