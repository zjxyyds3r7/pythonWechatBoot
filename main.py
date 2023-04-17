import itchat, time
from itchat.content import *
import random
import datetime
import rainbow
import peo_search
from math import *
import gpt
import chengyu

peo_help_str = "输入help获取帮助~\n" \
               "输入1 获取我给你的备注\n" \
               "输入2 获取一条舔狗日记\n" \
               "输入3 获取一条彩虹屁\n" \
               "输入count加表达式 计算表达式的值 例子:count 1+1 此条帮助请输入helpcount\n" \
               "输入search加名字 查询这个人的信息 例子:search周景鑫\n" \
               "输入gpt加问题 尝试向chatgpt提问 例如:gpt写五个有关春天的诗句" \
               "输入成语接龙加成语 开始玩成语接龙"\
               "更多功能正在开发..."

group_help_str = "艾特我并输入help获取帮助~\n" \
                 "艾特我并输入2 获取一条舔狗日记\n" \
                 "艾特我并输入3 获取一条彩虹屁\n"\
                 "艾特我并输入表达式 计算表达式的值 例子:@A.周景鑫 count 1+1 此条帮助请艾特我并输入helpcount\n" \
                 "艾特我并输入search加名字 查询这个人的信息 例子:@A.周景鑫 search周景鑫\n" \
                 "艾特我并输入gpt加问题 尝试向chatgpt提问 例如:@A.周景鑫 gpt写五个有关春天的诗句" \
                 "艾特我并输入成语接龙加成语 开始玩成语接龙" \
                 "更多功能正在开发..."

count_help_str = "计算表达式操作:可以使用加(+)减(-)乘(*)除(/)求余(%)乘方(**)以及括号()\n" \
                 "还有简单的三角函数sin(pi)等\n 三角函数均为弧度制\n" \
                 "例子: 2**(3+1)%3 等于2的3+1次方再对三取余\n" \
                 "例子: sin(pi/2) 等于sin(90度) 等于1.0\n" \
                 "例子: sin(30度) 可以使用'度'"
mess_list = []
with open('舔狗日记.txt', 'r', encoding='utf-8') as f:
    mess_list = [i.replace(' ', '').replace('\n', '')
                 for i in f.readlines()
                 if i.replace(' ', '').replace('\n', '') != '']


def evalFormat(s):
    replaceList = [["（", '('], ['）', ')'], ['–', '-'], [' ', '']]
    for r in replaceList:
        s = s.replace(r[0], r[1])
    return s


def getUserRemarkName(msg):
    t = None
    try:
        t = msg.user.RemarkName
    except:
        pass
    t = "无备注" if t == "" else t
    t = "文件传输助手" if t is None else t
    return t


def getResult(msg):
    if msg.text.lower() == "help":
        return peo_help_str
    if msg.text.lower() == "helpcount" or msg.text.lower() == "counthelp":
        return count_help_str

    # q = msg.text[7:]
    q = msg.text
    if q[:3].lower() == 'gpt':
        return gpt.questionToGpt(q[3:])

    if q[:5].lower() == 'count':
        question = q[5:]
        try:
            newquestion = question.replace('度', '*pi/180')
            print(question)
            return "在python中运行 " + question + "的结果是:" + \
                   str(eval(evalFormat(newquestion)))
        except Exception as e:
            print(e)
            # return "在python中运行 " + question + "时出错:" + \
            #        str(e)

    if q.startswith('成语接龙'):
        word = evalFormat(q.replace('成语接龙',''))
        userId = msg['FromUserName']
        return chengyu.getchengyures(word=word,userId=userId)
    
    if q[:6].lower() == 'search':
        name = evalFormat(q[6:])
        print(name)
        r = peo_search.search(name=name)
        if len(r) == 0:
            return '本地数据库内没查到叫' + name + '的人'
        if len(r) > 100:
            return '要显示的人太多了 缩小范围后再查询吧 最多只支持100个人'

        res = "查名字为" + name + "的人的结果为:\n"
        for i in r:
            res += "{0} {1}年{2:2}班 {3:4} 性别:{4} 出生于:{5}年{6:2}月{7:2}日\n".format(*i)
        return res
    v = -1
    try:
        v = int(q)
    except:
        pass
    if v == 1:
        return "我给你的备注是:" + getUserRemarkName(msg)
    if v == 2:
        return "当前时间:" + datetime.datetime.now().strftime('%H:%M:%S') + "\n" + random.choice(mess_list)
    if v == 3:
        return "当前时间:" + datetime.datetime.now().strftime('%H:%M:%S') + "\n彩虹屁来咯:\n\n"+rainbow.getRainbow()
    else:
        question = q
        try:
            newquestion = question.replace('度', '*pi/180')
            print(question)
            return "在python中运行 " + question + "的结果是:" + \
                   str(eval(evalFormat(newquestion)))
        except Exception as e:
            print(e)
        return "不要对我说一些奇奇怪怪的话啦!比如" + q


@itchat.msg_register([TEXT])
def text_reply(msg):
    if msg.type == 'Text':
        q = msg.text
        res = getResult(msg)
        print(getUserRemarkName(msg))
        if getUserRemarkName(msg) == "文件传输助手":
            msg.user.send('%s: \n%s' % ('回复:' + q, res))
        else:
            return '%s: \n%s' % ('回复:' + q, res)


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply_group(msg):
    if msg.isAt:
        # print(msg)
        q = msg.text.split(" ")
        if len(q) == 2 and q[1] == '':
            return '你好,我是zjxbot,有什么可以帮到你 如需帮助请艾特我后输入help'
        if len(q) != 2:
            return

        question = q[1]
        if '-'*8 in question:
            return
        if question[:3].lower() == 'gpt':
            return gpt.questionToGpt(question[3:])
        if question == 'help':
            return group_help_str
        if question == 'helpcount':
            return count_help_str

        if question == '2':
            return "当前时间:" + datetime.datetime.now().strftime('%H:%M:%S') + "\n" + random.choice(mess_list)
        if question == '3':
            return "当前时间:" + datetime.datetime.now().strftime('%H:%M:%S') + "\n彩虹屁来咯:\n\n"+rainbow.getRainbow()
        print(question)
        if question[:6] == "search":
            name = question[6:].replace(' ', '')
            print(name)
            r = peo_search.search(name=name)
            if len(r) == 0:
                return '本地数据库内没查到叫'+name+'的人'
            if len(r) > 100:
                return '要显示的人太多了 缩小范围后再查询吧 最多只支持100个人'

            res = "名字为" + name + "的人的结果为:\n"
            for i in r:
                res += "{0} {1}年{2:2}班 {3:4} 性别:{4} 出生于:{5}年{6:2}月{7:2}日\n".format(*i)
            return res
        if question.startswith('成语接龙'):
            word = evalFormat(question.replace('成语接龙',''))
            userId = msg['ActualUserName'] + 'ingroup'
            return chengyu.getchengyures(word=word,userId=userId)
        try:
            newquestion = question.replace('度', '*pi/180').replace('count', '')
            print(newquestion)
            return "在python中运行 " + question.replace('count', '') + "的结果是:" + \
                   str(eval(evalFormat(newquestion)))
        except Exception as e:
            print(e)

        return 'Error 好像没理解你的意思~'


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send(peo_help_str)


itchat.auto_login(hotReload=False)
itchat.run(True)
