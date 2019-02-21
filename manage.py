from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/GitHup_project"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app.config.from_object(Config)

# 创建数据库对象
db = SQLAlchemy(app)




@app.route("/")
def index():
    return "index"


if __name__ == '__main__':
    app.run()