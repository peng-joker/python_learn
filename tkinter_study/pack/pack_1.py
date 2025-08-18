# _*_coding:UTF-8 _*_
from tkinter import *
win = Tk()
win.geometry("1200x200")
# 创建根窗口
txt1 = "暮冬时烤雪"                                      # 第一行文字
txt2 = "迟夏写长信"                                      # 第二行文字
txt3 = "早春不过一棵树"                                   # 第三行文字
txt4 = "深秋收获一颗❤️"                                   # 第四行文字
# 在pack()方法中通过side参数设置排列方式为从左向右依次排列
Label(win, text=txt1, bg="#F5DFCC").pack(side="top")

# padx 表示距离窗口左边最小 500px,相当于 pading-left 如果将窗口缩小,当距离小于这个值时,元素直接不显示  pady 也是一样的道理,相当于 padding-top
Label(win, text=txt1, bg="#F5DFCC").pack(side="top",padx=500,pady=50,fill="both")
Label(win, text=txt2, bg="#EDB584").pack(side="left")

# ipadx 表示文字距离组件的值, ipady 也是一样的道理
Label(win, text=txt2, bg="#EDB584").pack(side="left",ipadx=10,ipady=5)
Label(win, text=txt3, bg="#EF994C").pack(side="right")
Label(win, text=txt4, bg="#c94f4f").pack(side="bottom")
win.mainloop()
