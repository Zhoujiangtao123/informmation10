"""
用来解决首页的视图函数

导入蓝图， 创建对象
用蓝图对象装饰视图函数
将蓝图对象注册到app
"""


from flask import Blueprint

# 创建蓝图对象
index_blu = Blueprint("index", __name__)


# 用蓝图对象装饰视图函数
@index_blu.route("/")
def index():
    # 测试redis
    # redis_store.set("a1", "python1")
    # print(redis_store.get("a1"))
    # 测试session, 因为需要测试session 所以需要导入flask里面的session
    # session["age"] = 25
    # print(session.get("age"))

    # 第一种测试日志方法
    # logging.debug("这是debug内容")
    # logging.info("这是info内容")
    # logging.warning("这是warning内容")
    # logging.error("这是error内容")
    #
    # # 第二种写日志的方法
    # current_app.logger.debug("----这是debug内容----")
    # current_app.logger.info("----这是info内容----")
    # current_app.logger.warning("----这是warning内容-----")
    # current_app.logger.error("----这是error内容-----")
    return "index12321"
