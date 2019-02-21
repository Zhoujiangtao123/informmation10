"""
将所有业务逻辑代码放到info这个init文件中时候，需要解决主文件的app这对象的问题？ 利用函数返回值
"""


import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session


from config import Config, config_dict


def create_app(env):  #env 是用来接收"develop"或者"product"

    app = Flask(__name__)
    app.secret_key = "!@#$%^%$#$%^&%$"


    # 注意要放在创建数据库对象之前，需要先加载配置信息，才能创建数据库对象
    # 现在解决不同环境的问题？,是通过配置类去加载的，不同的环境就需要加载不同的配置类信息

    config_classname = config_dict[env]  #是DevelopmentConfig或者ProductionConfig
    app.config.from_object(config_classname)

    # 创建数据库对象
    db = SQLAlchemy(app)

    # 创建redis仓库
    redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

    # 读取app中的session信息， 指定存储位置
    Session(app)

    return app