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

# root = Tk()
# menubar = Menu(root)
# fmenu = Menu(menubar)
# for item in ['新建', '打开', '保存', '另存为']:
#     fmenu.add_command(label = item)
#
# emenu = Menu(menubar)
# for item in ['复制','粘贴','剪切']:
#     emenu.add_command(label = item)
#
# vmenu = Menu(menubar)
# for item in ['默认视图', '新式视图']:
#     vmenu.add_command(label = item)
#
# amenu = Menu(menubar)
# for item in ['版权信息', '其他说明']:
#     amenu.add_command(label = item)
#
# menubar.add_cascade(label="文件", menu=fmenu)
# menubar.add_cascade(label="编辑", menu=emenu)
# menubar.add_cascade(label="视图", menu=vmenu)
# menubar.add_cascade(label="关于", menu=amenu)
# root['menu'] = menubar
# root.mainloop()

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

# def xin():
#     global root
#     Label(root, text = "I love Python").pack()
#
# root = Tk()
# menubar = Menu(root)
#
# for x in ['vb', 'c', 'java', 'php']:
#     menubar.add_command(label = x)
#
# menubar.add_command(label = 'python', command = xin)
#
# def pop(event):
#     menubar.post(event.x_root, event.y_root)
#
#
# root.bind("<Button-3>", pop)
# root.mainloop()


# ************分割线*******************
# 1.有时候，一个菜单项的各个菜单可能并不是一个类型，
# 有可能是两种类型，在它们中间可以插一个分割线来界定
# 界限。
# 2.插入分割线和插入正常的菜单项操作很相似，只是使用
# 的方法是 add_separator，该方法无需参数。

# root = Tk()
# m = Menu(root)
# m2 = Menu(m)
# for item in ['python', 'perl', 'php', 'ruby']:
#     m2.add_command(label = item)
#
# m2.add_separator()
#
# for item in ['java', 'c++', 'c']:
#     m2.add_command(label = item)
#
# m.add_cascade(label = 'lan', menu = m2)
# root['menu'] = m
# root.mainloop()



# **************checkbutton 与 radiobutton********
# 1.checkbutton 原本是指“复选按钮”，radiobutton 原本
# 是指“单选按钮”。
# 辛星 2014 年度辛星 tkinter 教程第二版 tkinter
# 48 / 103
# 2.单选按钮与复选按钮是相对来说的，即在这一组中，单
# 选按钮中只能有一个是被选定的，即一个人的性别是女的，
# 就一定不是男的，但是复选按钮对应的情况则是可以有多
# 个同时被选定，比如一个人即可以喜欢篮球，也可以喜欢
# 足球，还有可能喜欢乒乓球，等等。
# 3.在菜单中，也有类似的概念，即单选菜单和复选菜单。
# 它们分别用 add_radiobutton 和 add_checkbutton 来分别
# 添加。
# 4.这两种菜单都是如果一旦被选定，那么前面会有一个类
# 似于对号的标记出现，checkbutton 可以多个同时被选定，
# 但是 radiobutton 却只能被选定一个，即这个被选定了，
# 会自动取消前一个的选定。

# root = Tk()
# m = Menu(root)
# m2 = Menu(m)
# for item in ['python', 'perl', 'php', 'ruby']:
#     m2.add_checkbutton(label = item)
#     #  多选菜单
#
# m2.add_separator()
#
# for item in ['java', 'c++', 'c']:
#     m2.add_radiobutton(label = item)
#     # 单选菜单
#
# m.add_cascade(label = 'lan', menu = m2)
# root['menu'] = m
# root.mainloop()


# 第八节：对话框和消息框
# ***********对话框****************
# 1.说到对话框，我感觉这可是个最有内容可写的话题了，
# 因为我早前在学习 MFC 的时候，基本上刚开始学习的时候
# 每次构建的应用程序都是基于对话框的，扯远了。
# 2.在 tkinter 中的对话框，一定要注意自己的版本，因为
# Python2 和 Python3 中关于对话框的变化到没有多大，但是
# 关于引用的格式差别很大，即我们的 import 的时候，
# Python2 和 Python3 有很大差别，具体请参照我第零节的文
# 件目录去导入。
# *************关于该节************
# 1.可能在别的编程语言中，对话框是一种编程模式，至少
# 在我学习的 MFC 和 Qt 中都还是蛮重要的。
# 2.但是在 tkinter 中，对话框的地位略有下降，我也不计
# 划讲的特别深，如果读者有兴趣，可以深入到源代码中研
# 究下，或者参考别的资料。
# ***********对话框************
# 1.关于对话框，tkinter 有它自己的布局，在 Python 的安
# 装目录下的 Lib 文件夹的 tkinter 子文件夹下，有个
# dialog.py，它只有 2KB，它就是我们要介绍的重点。
# 2.打开该文件，只有五十行，还包括用来测试的代码，里
# 面只有一个 Dialog 类，它继承自 Widget,它的方法也很简
# 单，基本上也就一个__init__方法有实质性内容，下面的
# _test 是用来测试的。
# 3.该类可用的属性很少，基本上真正比较好用的也就一个
# num 属性了，它用于返回用户的点击。
# 4.我们可以通过它给出的例子来模仿写出一个对话框，注
# 意它的 title 属性，text 属性，strings 属性。

# from tkinter.dialog import *
#
# def xin():
#     d = Dialog(None, title = "2014辛星", text = "2014年度辛星tkinter材料还满意吗？",
#                bitmap = DIALOG_ICON, default = 0, strings = ("不满意", "还可以", "很满意"))
#     print(d.num)
#
# t = Button(None, text = "辛星调查", command = xin)
# t.pack()
# b = Button(None, text = "关闭", command = t.quit)
# b.pack()
# t.mainloop()


# ***********其他对话框****************
# 1.其实我们也看到了，由于源代码中给出的关于对话框的
# 代码过于简短，真正用起来并不方便。
# 2.于是，根据使用频率，源代码又给出了几个标准对话框，
# 比如 simpledialog（简单对话框），commondialog（一般
# 对话框），filedialog（文件对话框），其实
# colorchooser 也算对话框的内容。
# 3.我看了下它们的源代码，但是考虑到我们的程序的主要
# 用途，所以就不在此节深入介绍了，具体的大家可以深入
# 源代码一探究竟，或许在后续版本中会添加对它的进一步
# 介绍。




# **************消息框****************

# from tkinter.messagebox import *
# showinfo(title="2014辛星", message="点燃梦想，就在现在")





# 第九节：常用控件介绍
# ************控件**************
# 1.在前面几节中，介绍了几个简单的控件，比如标签，比
# 如按钮，比如输入框等等。
# 2.说实话，标准的 tkinter 中给出的控件数目并不多，只
# 有 21 个，虽然后来的 ttk 中又增加了几个，但是还是跟不
# 上需要。关于 ttk 后面会介绍。
# 3.但是这里还是介绍下常用的控件把，毕竟这些控件还是
# 蛮重要的。
# ***********复选按钮******************
# 1.复选按钮就是 Checkbutton 类，它的实例化和 Button 很
# 相似。
# 2.既然是按钮，那就可以有 command 属性，该属性可以对
# 应到一个函数上去来执行某些功能。
# 3.复选框通常是用来选择信息的时候的一种选择，它前面
# 有个小正方形的方块，如果选中则有一个对号，也可以再
# 次点击以取消该对号来取消选中。
# **************复选框代码实例***************

# time1 = 0
# time2 = 0
# def xin1():
#     global l, c1, time1
#     if time1 % 2 == 0:
#         time1 += 1
#         l['text'] = "a被选中"
#     else:
#         time1 += 1
#         l['text'] = "a被取消"
#
# def xin2():
#     global l, c2, time2
#     if time2 % 2 == 0:
#         time2 += 1
#         l['text'] = "b被选中"
#     else:
#         time2 += 1
#         l['text'] = "b被取消"
#
# root = Tk()
# c1 = Checkbutton(root, text = 'a', command = xin1)
# c1.pack()
# c2 = Checkbutton(root, text = 'b', command = xin2)
# c2.pack()
# l = Label(root, text = '     ')
# l.pack()
# root.mainloop()

# ************单选框***************
# 1.单选框和复选框非常相似，只是把 Checkbutton 换成
# Radiobutton。
# 2.我就不代码示例了，因为实在是太相似且简单了。

# *************文本域*************
#
# 1.所谓文本域，也就是文本，其实它可以看做一个大型的
# 文本框，它的属性也更多一些。
# 2.该类非常庞大，包括了不少的方法，来对里面的内容来
# 做非常复杂的操作，按理来说很有东西可写，但是如果让
# 我去做一个文本编辑器，我根本不会用 tkinter 去做，所
# 以我还是没多少兴趣去了解这部分内容。


# root = Tk()
# t = Text(root, width = 50, height = 30)
# t.pack()
# root.mainloop()

# 5.由于该类的源代码实在太长了，而我本人对于这些又很
# 不感兴趣，所以，就全部跳过了，因为要写一个功能强大
# 的文本编辑器，我不太建议用 tkinter。

# **************Canvas***************

# 1.canvas 直接翻译就是“帆布”,其实可以理解为一个画布，
# 用于在上面绘制图形。

# *************Toplevel*************
# 1.一个 toplevel 可以理解为一个新的窗口，它是一个顶层
# 窗口。
# 2.新建一个 toplevel 很简单，只需要实例化该类即可，这
# 也是创建多窗口 应用的一个途径。

# root = Tk()
# root.title('我是a窗口')
# l = Label(root, text = '我属于a')
# l.pack()
# f = Toplevel(root, width = 30, height = 20)
# f.title('我是toplevel')
# lf = Label(f, text = '我是toplevel')
# lf.pack()
# root.mainloop()






# 第十节：手绘图形
# ****************窗口重绘****************
# 1.第一次认识到手绘图形的重要性还是在学习 MFC 的时候，
# 因为 MFC 自带的绘图功能实在过于丑陋，我们可以重绘标
# 题栏、菜单栏、最小化按钮、最大化按钮、关闭按钮等窗
# 口组件来让窗口得到美化，除了这些，还可以手绘按钮，
# 后来出了一门技术，叫做“Direct UI”，也是这种思想的
# 进一步发扬光大把。
# 2.但是 tkinter 没有这些方面的接口，我也深感遗憾。但
# 是 tkinter 有一个绘图功能的组件，即 Canvas，翻译成汉
# 语即“帆布”，可以理解为“画布”，即用于绘制图形。


# ****************canvas*************
# *************建议的绘制**************
# 1.我们第一个示例随便绘制了，先把背景用 rgb 格式刷成
# 蓝色，然后画一条线，然后写几个字。

# root = Tk()
# root.title('简易绘图')
# can = Canvas(root, width = 400, height = 300, bg = '#00FFFF')
# can.create_line((0, 0), (200, 200), width = 8)
# can.create_text(300, 30, text = "对长亭晚")
# can.pack()
# root.mainloop()






#
# 第十一节：窗口的一些美化
# ****************美化**************
# 1.GUI 编程自从出现的那一天开始，就凸显除了强劲的魅
# 力 ，因为它对用户来说实在是太方便了。
# 2.但是 GUI 编程尤其的繁琐且啰嗦，因为界面编写确实令
# 人头疼，可能初学者对于写界面会很兴奋，但是写一段时
# 间就会感觉很烦了。
# 3.但是如果你致力于创造更加简洁大方的界面，那么还是
# 努力吧，毕竟，清爽的界面谁都喜欢用。



# ************窗口的一些控制***********
# 1.我们可以用 title 函数来修改窗口的默认标题，该参数
# 直接接收一个字符串参数。
# 2.我们还可以用 geometry 函数来控制窗口大小，它接受一
# 个字符串类型的参数，但是它的格式很严格，是这样的
# ‘width x height + xoffset + yoffset’,比如我写成
# '300x280+150+200' 就是一个合格的参数，注意的是这里
# 的 x 就是 xyz 的 x，不要擅自改成*。
# 3.如果想去除边框，还可以用 overrideredirect 方法，只
# 需要把参数设置为 1 即可。
# 4.如果想修改标题栏的默认图标，可以用 iconbitmap 方法
# 或者是 wm_iconbitmap 方法，它接受一个 ico 文件的文件
# 名。
# ***********一些效果图**************
# 1.更改图标之后的效果（由于我当时正在做 pygame 的游戏
# 开发，就顺手取了一个 pygame 的图标）：
# 注意左上角的图标，不是红色的 tk 字样，而是黄色的图片：

# root = Tk()
# root.geometry('300x280+150+200')
# root.title("2014辛星")
# root.overrideredirect(1)    # 去除边框
# # root.iconbitmap('pygame.ico')   # 修改图标
# root.mainloop()



#
# 第十二节：ttk 以及第一部分的总结
# *************ttk 的产生***************
# 1.ttk 可以理解为“Tk tookit”，在 tkinter 的目录里可
# 以找到，它是最后一个文件，大小有 56KB，还算一个比较
# 大的文件的，毕竟我们的 tkinter 的__init__.py 也只有
# 158KB。
# 2.ttk 的出现和大家对 tkinter 的不满有关，因为 tkinter
# 是一个跨平台的界面库，但是，这也就意味着它丧失了平
# 台优势。为了让它在 Windows 平台下运行更像 Windows，其
# 实是让它支持不同的风格，于是出现了这么一个文件，用
# 于弥补 tkinter 的不足。
# 3.它应该是在 8.5 版本中被引入的，就是我们当前使用的
# 这个版本。
# ******************ttk 的变动*************
# 1.很重要的一点就是对标准组件的支持，ttk 支持原来的
# 21 个组件中的 11 个，并且，它引入了六个新的组件：
# combobox,notebook,progressbar,separator,sizegrip,tr
# eeview。
# 2.怎么说呢，我预计 ttk 在以后的版本中还会有所变动，
# 因此也不是很建议大家投入太多精力去研究。
# *************效果对比**************
# 1.下面是同样的一个按钮，效果图如下(左边为导入了 ttf，
# 右边没有导入 ttf，我的平台是 Win7)：

# root = Tk()
# b = Button(root, text = '晶体')
# b.pack()
# root.mainloop()
# from tkinter.ttk import *
# root = Tk()
# b = Button(root, text = '晶体')
# b.pack()
# root.mainloop()

# 4.其实大家也可以看到，其实很简单，使用 ttf 只需要在
# 前面加一行代码即可了“from tkint.ttk import *”即可。
# 5.虽然只是差了一行代码，但是效果差别还是蛮大的。




















