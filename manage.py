import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask import session


app = Flask(__name__)
app.secret_key = "!@#$%^%$#$%^&%$"


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/GitHup_project"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 对redis数据库进行配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # 配置session信息
    SESSION_TYPE = "redis"   # 存储类型
    SESSION_KEY_PREFIX = "Session:"  # 设置前缀
    SESSION_USE_SIGNER = True  # 签名存储
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 制定存储位置
    PERMANENT_SESSION_LIFETIME = 3600*24*2  # 设置session两天有效

# 注意要放在创建数据库对象之前，需要先加载配置信息，才能创建数据库对象
app.config.from_object(Config)

# 创建数据库对象
db = SQLAlchemy(app)

# 创建redis仓库
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 读取app中的session信息， 指定存储位置
Session(app)


@app.route("/")
def index():
    # 测试redis
    redis_store.set("a1", "python1")
    print(redis_store.get("a1"))
    # 测试session, 因为需要测试session 所以需要导入flask里面的session
    session["age"] = 25
    print(session.get("age"))

    return "index"


if __name__ == '__main__':
    app.run()