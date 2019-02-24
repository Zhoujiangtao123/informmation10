"""
用来解决首页的视图函数

导入蓝图， 创建对象
用蓝图对象装饰视图函数
将蓝图对象注册到app
"""
from flask import Blueprint

# 创建蓝图对象
index_blu = Blueprint("index", __name__)
from . import views