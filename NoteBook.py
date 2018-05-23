# -*- coding:utf-8 -*-
"""

@Time    : 2018/5/22 14:49
@Author  : YeJian
@File    : NoteBook.py

"""

from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

import os

filename = ""


# 关于的函数，弹出窗口
def about():
    showinfo(title='关于', message='作者：admin')


# 右键弹出编辑功能，使用post函数
def pop(event):
    smenu.post(event.x_root, event.y_root)


# 打开  打开本地文件
def myopen():
    global filename
    filename = askopenfilename(defaultextension='.txt')
    if filename == "":
        filename = None
    else:
        # 返回path最后的文件名,若path以/或\结尾，那么就会返回空值。
        # eg:
        # path = 'D:\CSDN'
        # os.path.basename(path) = CSDN
        root.title('记事本  '+os.path.basename(filename))
        textPad.delete(1.0, END)
        f = open(filename, "r")
        textPad.insert(1.0, f.read())
        f.close()


# 新建
def new():
    global root, filename, textPad
    root.title("未命名文件")
    filename = None
    textPad.delete(1.0, END)


def save():
    global filename
    try:
        f = open(filename, 'w')
        msg = textPad.get(1.0, 'end')
        f.write(msg)
        f.close()
    except:
        saveas()


def saveas():
    # 返回文件路径
    f = asksaveasfilename(initialfile = '未命名.txt', defaultextension='.txt')
    global filename
    filename = f
    fh = open(f, 'w')
    msg = textPad.get(1.0, 'end')
    fh.write(msg)
    fh.close()
    root.title("笔记本  " + os.path.basename(f))


def cut():
    global textPad
    textPad.event_generate("<<Cut>>")


def copy():
    global textPad
    textPad.event_generate("<<Copy>>")


def paste():
    global textPad
    textPad.event_generate("<<Paste>>")


def undo():
    global textPad
    textPad.event_generate("<<Undo>>")


def redo():
    global textPad
    textPad.event_generate("<<Redo>>")


def select_all():
    global textPad
    textPad.tag_add('sel', '1.0', 'end')


def find():
    global root
    t = Toplevel(root)
    t.title("查找")
    t.geometry("260x60+200+250")
    t.transient(root)
    Label(t, text="查找：").grid(row = 0, column = 0, sticky = 'e')
    v = StringVar()
    e = Entry(t, width = 20, textvariable = v)
    e.grid(row = 0, column = 1, padx = 2, sticky = 'we')
    e.focus_set()
    c = IntVar()
    Checkbutton(t, text="不区分大小写", variable=c).grid(row = 1, column = 1, sticky = 'e')
    Button(t, text="查找所有", command = lambda:search(v.get(), c.get(), textPad, t, e)).grid(row=0, column=2, sticky='e'+'w', padx=2, pady=2)
    def close_search():
        textPad.tag_remove('match','1.0', END)
        t.destroy()
    t.protocol('WM_DELETE_WINDOW', close_search)


def search(needle, cssnstv, textPad, t, e):
    textPad.tag_remove('match', '1.0', END)
    count = 0
    if needle:
        pos = '1.0'
        while True:
            pos = textPad.search(needle, pos, nocase = cssnstv, stopindex = END)
            if not pos:break
            lastpos = pos + str(len(needle))
            textPad.tag_add('match', pos, lastpos)
            count += 1
            pos = lastpos
        textPad.tag_config('match', foreground='yellow', background='green')
        e.focus_set()
        t.title(str(count)+'个被匹配')


root = Tk()
root.geometry("500x300+500+200")
menubar = Menu(root)
fmenu = Menu(menubar)
fmenu.add_command(label='新建', command=new)
fmenu.add_command(label='打开', command=myopen)
fmenu.add_command(label='保存', command=save)
fmenu.add_command(label='另存为', command=saveas)
menubar.add_cascade(label='文件', menu=fmenu)
smenu = Menu(menubar)
smenu.add_command(label='撤销', command=undo)
smenu.add_command(label='重做', command=redo)
smenu.add_separator()
smenu.add_command(label='剪切', command=cut)
smenu.add_command(label='复制', command=copy)
smenu.add_command(label='粘贴', command=paste)
smenu.add_separator()
smenu.add_command(label='查找', accelerator="Ctrl + F", command=find)
smenu.add_command(label='全选', command=select_all)
menubar.add_cascade(label='编辑', menu=smenu)
menubar.add_command(label='关于', command=about)
root['menu'] = menubar

shortcutbar = Frame(root, height=25, bg='light sea green')
shortcutbar.pack(expand=NO, fill=X)
lnlabel = Label(root, width=2, bg='antique white')
lnlabel.pack(side=LEFT, anchor='nw', fill=Y)

textPad = Text(root, undo=True)
textPad.pack(expand=YES, fill=BOTH)
scroll = Scrollbar(textPad)
textPad.config(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side=RIGHT, fill=Y)

# 绑定右键的事件，弹出编辑菜单
textPad.bind("<Control-n>", new)
textPad.bind("<Control-o>", myopen)
textPad.bind("<Control-s>", save)
textPad.bind("<Control-a>", select_all)
textPad.bind("<Control-f>", find)
textPad.bind("<Control-F>", find)
root.bind('<Button-3>', pop)
root.mainloop()


