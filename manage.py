
from info import create_app


# 利用函数返回的的值app来解决问题
app = create_app("develop")   #develop就是开发模式product就是线上模式


@app.route("/")
def index():
    # 测试redis
    # redis_store.set("a1", "python1")
    # print(redis_store.get("a1"))
    # 测试session, 因为需要测试session 所以需要导入flask里面的session
    # session["age"] = 25
    # print(session.get("age"))

    return "index"


if __name__ == '__main__':
    app.run()