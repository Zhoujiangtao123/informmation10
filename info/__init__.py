"""
将所有业务逻辑代码放到info这个init文件中时候，需要解决主文件的app这对象的问题？ 利用函数返回值
"""
from logging.handlers import RotatingFileHandler

import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

import logging
from config import Config, config_dict


def create_app(env):  #env 是用来接收"develop"或者"product"

    app = Flask(__name__)
    app.secret_key = "!@#$%^%$#$%^&%$"


    # 注意要放在创建数据库对象之前，需要先加载配置信息，才能创建数据库对象
    # 现在解决不同环境的问题？,是通过配置类去加载的，不同的环境就需要加载不同的配置类信息

    config_classname = config_dict[env]  #是DevelopmentConfig或者ProductionConfig
    app.config.from_object(config_classname)

    # log_file(类名.LOG_LV)  #结果就是logging.DEBUG或者logging.ERROR
    # 两种不同环境的不同日志等级，开发模式就是logging.DEBUG等级 线上模式就是logging.ERROR等级
    log_file(config_classname.LOG_LV)


    # 创建数据库对象
    db = SQLAlchemy(app)

    # 创建redis仓库
    redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

    # 读取app中的session信息， 指定存储位置
    Session(app)

    return app


def log_file(LV):

    """记录日志信息"""

    # 设置哪些日志信息等级要被记录
    logging.basicConfig(level=LV)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)
