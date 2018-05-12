# -*- coding:utf-8 -*-
"""

@Time    : 2018/5/12 19:19
@Author  : YeJian
@File    : test1.py

"""

from tkinter import *
# root = Tk()
# root.title("样例一")
# w1 = Label(root, text="11111111", background="green")
# w2 = Label(root, text="22222222", background="red")
# w3 = Label(root, text="33333333", background="yellow")
# w1.pack()
# w2.pack()
# w3.pack()
# root.mainloop()


# 按钮绑定函数的两种方式
# 方式一
# def NewLabel():
#     global new
#     s = Label(new, text="i love python")
#     s.pack()
#
# new = Tk()
# b1 = Button(new, text="new a text", command=NewLabel)
# b1.pack()
# new .mainloop()

# 方式二
# def xinlabel(event):
#     global xin
#     s = Label(xin, text="i love python")
#     s.pack()
#
# xin = Tk()
# b1 = Button(xin, text='new a text')
# b1.bind("<Button-1>", xinlabel)
# b1.pack()
# xin.mainloop()

# 按钮的其他属性
# xin = Tk()
# b1 = Button(xin, text="aaa")
# b1['width'] = 20
# b1['height'] = 4
# b1.pack()
# b2 = Button(xin, text="bbb")
# b2['width'] = 20
# b2['background'] = 'red'
# b2.pack()
# xin.mainloop()

# 布局的讲解
# pack就是一种布局

# grid 布局：
# grid 可以理解为网格，或者表格，它可以把
# 界面设置为几行几列的网格，我们在网格里插入我们想要
# 的元素。这种布局的好处是不管我们如何拖动窗口，相对
# 位置是不会变化的，而且这种布局也超简单。

# place 布局：
# 它直接使用死板的位置坐标来布局，这样做
# 的最大的问题在于当我们向窗口添加一个新部件的时候，
# 又得重新测一遍数据，且我们不能随便地变大或者缩小窗
# 口，否则，可能会导致混乱。



# **************pack 布局*************
# 1.我们使用 pack 函数的时候，默认先使用的放到上面，然
# 后 依次向下排，它会给我们的组件一个自认为合适的位置
# 和大小，这是默认方式，也是我们上面一直采用的方式。
# 2. pack 函数也可以接受几个参数，side 参数指定了它停
# 靠在哪个方向，可以为 LEFT,TOP,RIGHT,BOTTOM,分别代表
# 左，上，右，下，它的 fill 参数可以是 X,Y,BOTH 和 NONE,
# 即在水平方向填充，竖直方向填充，水平和竖直方向填充
# 和不填充。
# 3.它的 expand 参数可以是 YES 和 NO，它的 anchor 参数可
# 以是 N,E,S,W（这里的 NESW 分别表示北东南西，这里分别
# 表示上右下左）以及他们的组合或者是 CENTER（表示中
# 间）。
# 4.它的 ipadx 表示的是内边距的 x 方向，它的 ipady 表示
# 的是内边距的 y 方向，padx 表示的是外边距的 x 方向，
# pady 表示的是外边距的 y 方向。

# pack布局样例
# root = Tk()
# Button(root, text="A").pack(side=LEFT, expand=YES, fill=Y)
# Button(root, text="B").pack(side=TOP, expand=YES, fill=BOTH)
# Button(root, text="C").pack(side=RIGHT, expand=YES, fill=NONE, anchor=NE)
# Button(root, text="D").pack(side=LEFT, expand=NO, fill=Y)
# Button(root, text="E").pack(side=TOP, expand=NO, fill=BOTH)
# Button(root, text="F").pack(side=BOTTOM, expand=YES)
# Button(root, text="G").pack(anchor=SE)
# root.mainloop()

# **************grid 布局*************
# 1.由于我们的程序大多数都是矩形，因此特别适合于网格
# 布局，也就是 grid 布局。
# 2.使用 grid 布局的时候，我们使用 grid 函数，在里面指
# 定两个参数，用 row 表示行，用 column 表示列，其中值得
# 注意的是 row 和 column 的编号都从 0 开始。
# 3.grid 函数还有个 sticky 参数，它可以用 N，E，S，W 表
# 示上右下左，它决定了这个组件是从哪个方向开始的，下
# 面的例子可以很好的解释这一点。
# 4.grid 布局直接用后面的行和列的数字来指定了它位于哪
# 个位置，而不必使用其他参数。
# 5.grid 函数也支持诸如 ipadx，ipady，padx，pady，它们
# 的意思和 pack 函数是一样的，默认边距是 0。
# 6.它还支持参数比如 rowspan，表示跨越的行数，
# columnspan 表示跨越的列数。
# 7.它还有一些属性，可以在以后我们的 demo 中慢慢使用来
# 看出其重要性。
# **************账号登陆例子的截图*********
# Entry 表示“输入框”。
# xin = Tk()
# Label(xin, text="账号：").grid(row=0, sticky=W)
# Entry(xin).grid(row=0, column=1, sticky=E)
#
# Label(xin, text="密码：").grid(row=1, sticky=W)
# Entry(xin).grid(row=1, column=1, sticky=E)
#
# Button(xin, text="登录").grid(row=2, column=1, sticky=E)
# xin.mainloop()

# pack 和 grid 不能同时用，通常对于较为复杂点的，我还是建议大家用 gird。






# 事件
# 事件的英文表述是“event”。
# **********事件及其绑定**************
# 1.其实，我们在按钮那一节就接触到了事件的绑定，使用
# 的函数是 bind。
# 2.bind 函数的调用规则：
# 窗体对象.bind(事件类型，回调函数)
# 3.所谓的“回调函数”，就是这个函数我们不用去调用它，
# 当相应的事件发生的时候，它会自动取调用。比如当我们
# 的按钮被按下的时候，它会被自动调用。
# ***************常用的事件************
# 1.我们在使用 bind 函数的时候，它的第一个参数就是事件
# 的类型了。
# 2.<Button-1>表示鼠标左键单击，其中的 1 换成 3 表示右
# 键被单击，为 2 的时候表示鼠标中键，感觉不算常用。
# 3.<KeyPress-A>表示 A 键被按下，其中的 A 可以换成其他
# 的键位。
# 4.<Control-V>表示按下的是 Ctrl 和 V 键，V 可以换成其他
# 键位。
# 5.<F1>表示按下的是 F1 键，对于 Fn 系列的，都可以随便
# 换。
# ***************再看绑定*************
# 1.事件不仅可以与 Button 绑定，我们之前看过源代码，发
# 现 bind 函数是定义在 Misc 类里面的，也就是说，这个
# bind 可以被绝大多数组件类所使用。
# 2.也就是说，我们可以让“标签”来模拟“按钮”的作用。
# 3.因为标签是 Label 类，而 Label 类继承自 Widget，而
# Widget 继承自 BaseWidget，而 Basewidget 继承自 Misc。
# 4.其实不仅是标签可以模拟 button，任何组件都可以模拟
# 它，只是那么有用。

# ********标签(Label)模拟按钮*************
# def xinlabel(event):
#     global xin
#     s = Label(xin, text="aaaa")
#     s.pack()
#
# xin = Tk()
# t = Label(xin, text="模拟按钮")
# t.bind("<Button-1>", xinlabel)
# t.pack()
#
# xin.mainloop()



# ************关于 bind 函数*************
# 1.关于 bind 函数，还有两个版本的，不能说高级低级，只
# 是使用的方面不同。
# 2.可以在全程序级别的绑定，使用 bind_all，它的参数类
# 型和 bind 一样，它通常用于全局的快捷键，比如 F1 通常
# 是用来打开帮助文档。
# 3.还可以绑定某些类别，使用 bind_class,它接受三个参数，
# 第一个参数是类名，第二个参数是事件类型，第三个参数
# 是相应的操作，比如 w.bind_class(“Entry”,
# “<Control-V>”,my_paste)。它就是绑定了所有的所有的
# 输入框的 Ctrl+V 表示粘贴。
# *************解除绑定**************
# 1.接触绑定我们使用 unbind 方法，它和 bind 的使用很相
# 似。
# 2.不过 unbind 方法只需要一个参数就可以了，它只需要解
# 除绑定的事件类型，因为它会解除该绑定事件类型的所有
# 回调函数。






# 第六节：输入框以及一个登录程序
# **************输入框的重要性***************
# 1.上面我们介绍了标签与按钮，下面我认为还比较重要点
# 的就是输入框。
# 2.应用程序要取得用户的信息，输入框是必不可少的，虽
# 然执行命令可以使用按钮，但是总不能让用户一直点击按
# 钮把
# get函数不需要任何参数，它的返回值就是该输入框的内容
# ****************密码框***********
# 1.其实密码框和输入框基本是一样的，都是向里面输入信
# 息用的。
# 2.如果要说不一样，也就一个地方不一样：密码框需要输
# 入的信息的显示字符比较单一。
# 3.比如 e 是一个输入框，我们可以设置它的 show 属性让它
# 变成一个密码框，即 e[‘show’] = ‘*’就可以了。

# *********小型登录程序*************
# 1.下面是一个小型登录程序，它的用户名是 111，密码是
# 222，如果输入正确，那么点击“登录”按钮之后，就会显
# 示“登录成功”，如果输入不符合，那么就会显示“用户
# 名或者密码错误”，并且清空两个输入框。

# def reg():
#     s1 = e1.get()
#     s2 = e2.get()
#     t1 = len(s1)
#     t2 = len(s2)
#     if s1 == '111' and s2 == '222':
#         c['text'] = "登录成功"
#     else:
#         c['text'] = "用户名或密码错误"
#         e1.delete(0,t1)
#         e2.delete(0,t2)
#
# root = Tk()
# l = Label(root, text="用户名: ")
# l.grid(row = 0, column = 0, sticky = W)
#
# e1 = Entry(root)
# e1.grid(row = 0, column = 1, sticky = E)
#
# l = Label(root, text="密码: ")
# l.grid(row = 1, column = 0, sticky = W)
#
# e2 = Entry(root)
# e2['show'] = '*'
# e2.grid(row = 1, column = 1, sticky = E)
#
# b = Button(root, text="登录", command = reg)
# b.grid(row = 2, column = 1, sticky = E)
#
# c = Label(root, text="")
# c.grid(row = 3)
# root.mainloop()



#
# 第七节：菜单
# ************菜单简介*****************
# 1.菜单的信息量是非常巨大的，由于菜单又可以有子菜单，
# 因此菜单的信息量非常大。
# 2.菜单的分类也较多，通常可以分为下拉菜单、弹出菜单
# 等等。
# **************添加顶层菜单************
# 1.我们可以使用 Menu 类来新建一个菜单，Menu 和其他的组
# 件一样，第一个是 parent，这里通常可以为窗口。
# 2.然后我们可以用 add_commmand 方法来为它添加菜单项，
# 如果该菜单是顶层菜单，则添加的菜单项依次向右添加。
# 如果该菜单时顶层菜单的一个菜单项，则它添加的是下拉
# 菜单的菜单项。
# 3.add_command 中的参数常用的有 label 属性，用来指定的
# 是菜单项的名称，command 属性用来指定被点击的时候调用
# 的方法，acceletor 属性指定的是快捷键，underline 属性
# 是是否拥有下划线。
# 3.最后可以用窗口的 menu 属性指定我们使用哪一个作为它
# 的顶层菜单。

# root = Tk()
# menubar = Menu(root)
# for item in ['文件','编辑','视图','关于']:
#     menubar.add_command(label = item)
#
# root['menu'] = menubar
# root.mainloop()

# 1.如果有子菜单，则情况稍微复杂点，这个时候，我们需
# 要使用 add_cascade，cascade 可以理解为“级联”，即它
# 的作用只是为了引出后面的菜单。
# 2.add_cascade 的一个很重要的属性就是 menu 属性，它指
# 明了要把那个菜单级联到该菜单项上，当然，还必不可少
# 的就是 label 属性，用于指定该菜单项的名称。
# 3.我们先新建一个 Menu 的实例，然后使用 add_command 来
# 添加菜单项，这样等该菜单建立完毕，我们要把它作为另
# 一个菜单项的子菜单，就需要使用 add_cascade 方法。

root = Tk()
menubar = Menu(root)
fmenu = Menu(menubar)
for item in ['新建', '打开', '保存', '另存为']:
    fmenu.add_command(label = item)

emenu = Menu(menubar)
for item in ['复制','粘贴','剪切']:
    emenu.add_command(label = item)

vmenu = Menu(menubar)
for item in ['默认视图', '新式视图']:
    vmenu.add_command(label = item)

amenu = Menu(menubar)
for item in ['版权信息', '其他说明']:
    amenu.add_command(label = item)

menubar.add_cascade(label="文件", menu=fmenu)
menubar.add_cascade(label="编辑", menu=emenu)
menubar.add_cascade(label="视图", menu=vmenu)
menubar.add_cascade(label="关于", menu=amenu)
root['menu'] = menubar
root.mainloop()

# 要注意的是我们可以先把子菜单做好，然后再去做上层菜单。


# ************弹出菜单*****************
# 1.弹出菜单又叫“上下文菜单”，也叫“右键菜单”，它
# 通常是鼠标单击右键产生的菜单，因此会有“右键菜单”
# 的说法。
# 2.其实很多界面库里面都是给出了弹出菜单的简单的制作
# 方法的，但是 tkinter 里面我们却只能使用比较原始的事
# 件绑定的方式去做。
# 3.大体思路就是：我们先新建一个菜单，然后向菜单项中
# 添加各种功能，最后我们监听鼠标右键消息，如果是鼠标
# 右键被单击，此时可以根据需要判断下鼠标位置来确定是
# 哪个弹出菜单被弹出，然后使用 Menu 类的 pop 方法来弹出
# 菜单。
# 4.大体思路就是如此，至于具体的细节，让我们到代码实
# 战中一探究竟。
# ************提前说明*************
# 1.Menu 类里面有一个 post 方法，它接收两个参数，即 x 和
# y 坐标，它会在相应的位置弹出菜单。
# 2.还记得用 bind 方法来绑定事件吗?而且要记得鼠标右键
# 是用的<Button-3>。






















