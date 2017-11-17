from tkinter import *
import os,time

#创建日记文件夹
def initDiary():
    dir = os.getcwd()
    list = os.listdir(dir)#获取当前目录中所有文件
    haveDiary = False
    for item in list:
        if item == "diary":
            haveDiary = True
    if haveDiary == False:
        os.mkdir("diary")
    os.chdir("./diary")

#写日记
def write():
    textVar.set("")
    text.delete("0.0","end")
    label.config(text="写日记模式")
    listBox.pack_forget()
    entry.pack()
    text.pack()

#显示日记内容
def showDiary(event):
    title = listBox.get(listBox.curselection())
    showTitle = title[:-4]
    textVar.set(showTitle)
    fileObj = open(title,'r')
    content = fileObj.read()
    text.delete("0.0","end")
    text.insert("end",content)
    fileObj.close()

    listBox.pack_forget()
    deleBtn.pack(side=BOTTOM)
    entry.pack()
    text.pack()

#看日记
def read():
    listBox.delete(0,END)
    dir = os.getcwd()
    list = os.listdir(dir)
    showText = "看日记模式"
    if len(list) == 0:
        showText += "（日记本是空的）"
    label.config(text=showText)
    for item in list:
        listBox.insert(0,item)
    listBox.bind('<Double-Button-1>',showDiary)
    entry.pack_forget()
    text.pack_forget()
    deleBtn.pack_forget()
    listBox.pack()

#删除日记
def dele_file():
    title = listBox.get(listBox.curselection())
    dir = os.getcwd()
    list = os.listdir(dir)
    work = False
    for item in list:
        if item == title:
            os.remove(title)
            read()

#判断是否重名文件，有则重命名
def is_same(title):
    # 判断是否有同名文件存在，有则重命名
    dir = os.getcwd()
    list = os.listdir(dir)
    for item in list:
        samename = True
        while samename == True:
            if item == title:
                title = textVar.get() + time.strftime('%Y%m%d_%H%M%S', time.localtime()) + '.txt'
                break
            else:
                samename = False
    return title
#保存
def save():
    title = textVar.get() + '.txt'
    content = text.get("0.0","end")
    if title != ".txt":
        title = is_same(title)
        fileObj = open(title,'w')
        fileObj.write(content)
        fileObj.close()
        label.config(text="已保存")
    else:
        label.config(text="请输入标题")

#创建工作目录
initDiary()

#创建窗体
root = Tk()
root.geometry('500x400')
root.title("简洁笔记本")
#保存按钮
saveBtn = Button(root,text="保存",command=save)
saveBtn.pack(side=LEFT,anchor='sw')
#退出按钮
quitBtn = Button(root,text="退出",command=quit)
quitBtn.pack(side=RIGHT,anchor='sw')
#写日记按钮
writeBtn = Button(root,text="写日记",command=write)
writeBtn.pack(side=BOTTOM)
#看日记按钮
readBtn = Button(root,text="看日记",command=read)
readBtn.pack(side=BOTTOM)
#删除日记
deleBtn = Button(root,text="删除",command=dele_file)
# deleBtn.pack(side=BOTTOM)
#标签
label = Label(root)
label.pack()

#标题
textVar = StringVar()
entry = Entry(root,textvariable=textVar)

#日记内容
text = Text(root)

#看日记
listBox = Listbox(root,height=300)


root.mainloop()




