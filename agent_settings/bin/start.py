import os

"""
启动文件，文件开始执行后把config.settings 写入系统环境变量，(参考Django的manage.py).
系统的环境变量是字典的形式
之后从系统环境变量中通过反射的方式导入模块
"""

os.environ['USER_SETTINGS'] = "config.settings"  # 把用户自定义的配置文件的路径以字符串的方式添加到系统环境变量中

from lib.conf.config import settings

"""
下面是测试：
通过settings就可以点出USER PWD EMAIL
"""
print(settings.USER)
print(settings.PWD)
print(settings.EMAIL)