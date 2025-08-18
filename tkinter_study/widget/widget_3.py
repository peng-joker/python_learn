# Widget的公共属性以及公共方法

from tkinter import *
win=Tk()
win.title("充值成功")
win.geometry("300x240")
Label(win,text="\n充值成功!",font="Times 18 bold").pack()
Label(win,text="\n恭喜获得：\n",font="16").pack(anchor=W,padx=45)

string="1、一级VIP30天\n\n" \
       "2、每天额外赠送300金币7天\n\n" \
       "3、全英雄限免30天\n"

# Label(win,text=string,font="18",fg="red",justify="right").pack() # 文字左对齐
Label(win,text=string,font="18",fg="red",justify="center").pack() # 默认居中对齐
win.mainloop()
