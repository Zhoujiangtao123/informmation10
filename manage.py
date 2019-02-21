import logging

from flask import current_app

from info import create_app


# 利用函数返回的的值app来解决问题
app = create_app("develop")   #develop就是开发模式product就是线上模式


if __name__ == '__main__':
    app.run()