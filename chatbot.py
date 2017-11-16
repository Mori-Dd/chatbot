import os,time

#更新时间 2017/11/16 19:04
#修复指令错误BUG
speakdict={}

print('你好，我是Python')
time.sleep(0.5)
flog='c' #机器人默认聊天模式

#判断字典文件是否存在
def is_file():
    os_path = os.getcwd() + '\\' + 'potbase.txt'
    if os.path.exists(os_path) == False:
        f = open(os_path, 'w')
        f.close()

#读取字典库
def readbase():
    f = open('potbase.txt', 'r')
    for line in f.readlines():
        line = line.strip()
        if not len(line):
            continue
        speakdict[line.split(':')[0]] = line.split(':')[1]
    f.close()
#    print(speakdict)

#写入字典库
def writebase():
    file = open('potbase.txt','w')
    for i in speakdict:
        word = str(i)+ ':' + speakdict[i] +'\n'
        file.write(word)
    file.close()

#搜索模式
def nowtime():
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

#训练模式
def train():
    print("------------------训练模式------------------")
    work = True
    while work == True:
        key = input("请输入您的问题（输入完请按回车键确认）：" + '\n')
        value = input("请输入您的答案（输入完请按回车键确认）：" + '\n')
        speakdict[key] = value
        writebase()
        print("问题已保存,我现在会%d个问题了！"%len(speakdict))
        flog = input("继续添加请按：t ，进入聊天模式请按：c ,结束请按：l "+'\n')
        if flog == 't':
            work = True
        elif flog == 'c':
            chat()
        elif flog == 'l':
            leave()

#聊天模式
def chat():
    print("------------------聊天模式------------------")
    readbase()
    work = True
    print("您好，我是小P，有啥可以帮到您的？")
    while work == True:
        if len(speakdict) == 0:
            print('\n' + "我还不会任何问题，请先训练我哦！" + '\n')
            train()
            break
        key = input()
        for k in speakdict.keys():
            if key in k:
                print(speakdict[k])
                work = True
                break
            if key in "时间几点":
                nowtime()
            else:
                work = False
    while work == False:
        flog = input("我还不会这个问题，还有其他要问的不？(添加此问题请按：t ,退出请按：l )" + '\n')
        if flog == 'l':
            leave()
        elif flog == 't':
            train()
        else:
            print("输入命令错误，请重新输入")
def leave():
    print("------------------谢谢您的使用，再见！------------------")
    time.sleep(1)
    os._exit(0)

while flog=='c':
    is_file()
    flog=input("您现在可以选择跟我聊天(c)、训练我(t)、或者让我离开(l),请选择："+'\n')
    if flog == 't':
        train()
        continue
    elif flog =='c':
        chat()
        continue
    elif flog == 'l':
        leave()
        continue
    else:
        print("输入命令错误，请重新输入")
        flog = 'c'
