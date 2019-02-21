import redis


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