# 常用插件集合

## 1 配置文件

### 1.1 功能介绍

- 配置文件包含系统默认配置文件和自定义配置文件，这里参考Django源码中的配置文件，实现了通过一个Settings类的settingsd对象调用所有的配置文件中的内容。注意：用户自定的配置文件的优先级高于系统配置文件。
- 参考Django的中间件在配置文件中定义了 

### 1.2 用到的技术

- 反射
- 通过字符串导入模块
- 系统环境变量
- dir()获取配置文件中的内容

### 1.2 使用方法  

- 启动文件：`agent_settings/bin/start.py`
- from lib.conf.config import settings 导入的是settings对象，settings对象中能够调用配置文件中的任意方法


