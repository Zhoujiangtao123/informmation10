from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis

app = Flask(__name__)


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/GitHup_project"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 对redis数据库进行配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379


# 注意要放在创建数据库对象之前，需要先加载配置信息，才能创建数据库对象
app.config.from_object(Config)

# 创建数据库对象
db = SQLAlchemy(app)

# 创建redis仓库
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)


@app.route("/")
def index():
    # 测试redis
    redis_store.set("a1", "python1")

    return "index"


if __name__ == '__main__':
    app.run()