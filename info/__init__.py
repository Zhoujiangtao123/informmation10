"""
将所有业务逻辑代码放到info这个init文件中时候，需要解决主文件的app这对象的问题？ 利用函数返回值
"""


import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask import session

from config import Config


def create_app():
    app = Flask(__name__)
    app.secret_key = "!@#$%^%$#$%^&%$"


    # 注意要放在创建数据库对象之前，需要先加载配置信息，才能创建数据库对象
    app.config.from_object(Config)

    # 创建数据库对象
    db = SQLAlchemy(app)

    # 创建redis仓库
    redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

    # 读取app中的session信息， 指定存储位置
    Session(app)

    return app