# python机器人
1. 主要功能
    1. 获取备注
        - 基于itchat_uos包
    2. 舔狗日记
        - 基于天行api
    3. 彩虹屁
        - 基于天行api
    4. 计算表达式的值  
        - 基于python的eval()
    5. 查人
        - 基于学生信息表格
    6. 向chatgpt提问
        - 基于python的openai包
    7. 成语接龙
        - 基于天行api

2. 用了什么
    1. pandas 用于学生表格的读取和查询筛选
    2. itchat_uos 安装这个包时要注意 需要按照requirements中版本安装
    3. openai 像chatgpt提问

3. 服务器环境  
    - 美国服务器
    - Windows server 2012

4. 各个文件的意义
    - t.xlsx: 实验高中名单
    - t1.xlsx: 美高名单
    - 舔狗日记.txt: 舔狗日记的本地文件
    - list.pkl: 彩虹屁文件
    - run.bat: 运行文件
    
5. 使用方式
    1. 修改`chengyu/__init__.py`中的api key 修改`gpt/__init__.py`中的openai.api_key并去掉注释
        - 注意 不要在国内将openai.api_key赋值 否则将会封号 亲测！！！一定注意！！！
    2. 安装依赖  
        `pip install -r requirement.txt`
    3. 使用run.bat 或者使用  
    `python main.py`
    4. 按照提示扫码登陆
    5. 和机器人玩耍吧!

6. 其他碎碎念
    1. 仅供学习 不要恶意骚扰他人等！
    2. 关于chatgpt的openai.api_key一定不要在国内使用 否则封号！
    3. 其他接口使用天行api 天行api链接：[天行api](https://www.tianapi.com/)
    4. 其中两个表格t.xlsx和t1.xlsx分别为两个学校的学生信息 已删除真实信息并填充了一条虚假信息
    5. 作者微信:zjxyyds0307
