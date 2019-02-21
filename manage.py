
from info import create_app, db, models   #导入models是因为有了模型类才能创建数据表
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


# 利用函数返回的的值app来解决问题
app = create_app("develop")   #develop就是开发模式product就是线上模式
# 创建Manager对象
manager = Manager(app)
# 创建Migrate对象
Migrate(app, db)
# 添加db命令
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()