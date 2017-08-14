#! /bin/bash

# 设置一个系统环境变量FLASK_APP，将含有程序实例的模块文件名（也就是我们的flaskr.py）赋值给它。
# 这里由于我们在flaskr/__init__.py文件中导入了flaskr.py的app到包的顶层，
# 所以我们这里可以指定FLASK_APP为flaskr
export FLASK_APP=flaskr
# 调试标志`FLASK_DEBUG`启用或禁用交互式调试。
# 决不能让调试模式在生产系统中启动，因为它将允许用户在服务器上执行代码！
export FLASK_DEBUG=true
# 使用flask提供的run命令启动服务器
flask run
