import logging
import redis


class Config(object):
    # DEBUG = (类名.DEBUG)
    DEBUG = True
    SECRET_KEY = "!@#$%^%$#$%^&%$"
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/GitHup_project"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 对redis数据库进行配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # 配置session信息
    SESSION_TYPE = "redis"   # 存储类型
    SESSION_KEY_PREFIX = "Session:"  # 设置前缀
    SESSION_USE_SIGNER = False  # 签名存储
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 制定存储位置
    PERMANENT_SESSION_LIFETIME = 3600*24*2  # 设置session两天有效


    # 一般会有两种不同的环境
    # 开发环境(在开发环境下使用的配置)
class DevelopmentConfig(Config):
    DEBUG = True
    LOG_LV = logging.DEBUG


    # 生产(线上)模式
class ProductionConfig(Config):
    DEBUG = False
    LOG_LV = logging.ERROR

config_dict = {
    "develop": DevelopmentConfig,
    "product": ProductionConfig

}