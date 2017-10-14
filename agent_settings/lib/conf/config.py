import os
import importlib
from lib.conf import global_settings

"""
该文件用于导入系统配置文件和用户自定义文件，
"""


class Settings(object):
    def __init__(self):
        """
        先加载系统默认的配置文件，然后加载用户自定义的配置文件，
        如果用户自定义的配置文件中和系统配置文件重复，会覆盖系统的配置文件
        """

        # ###### 加载系统默认的配置文件 ######

        """
        通过dir获取配置文件中的所有内容，把大写的配置文件找出来
        通过反射的方式把对应配置文件的值取出来
        最后把配置文件中的内容通过setattr 设置到self中
        """
        for name in dir(global_settings):
            if name.isupper():
                value = getattr(global_settings, name)
                setattr(self, name, value)

        # ###### 加载用户自定义的配置文件 ######

        """
        从系统的环境变量中，通过字符串导入模块
        """
        settings_module = os.environ.get('USER_SETTINGS')
        if not settings_module:
            return
        m = importlib.import_module(settings_module)  # 通过字符串的方式导入模块
        for name in dir(m):
            value = getattr(m, name)
            setattr(self, name, value)


settings = Settings()  # 实例化的对象setting 中包含了系统默认配置和用户自定义的配置
