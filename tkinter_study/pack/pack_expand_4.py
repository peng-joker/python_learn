from tkinter import *
win=Tk()
win.title("tkinter的初使用")
txt1=Label(win,text="象吃狮",bg="#ba55d3",font=14)
txt1.pack(side="left",padx="10",pady="5",ipadx="6",ipady="4",fill="y",expand=1)# 不加 expand 的话所有的元素挤在窗口的最左边,加上之后所有的元素均匀分布于窗口中

txt2=Label(win,text="狮吃虎",bg="#c1ffc1",font=14)
txt2.pack(side="left",padx="10",pady="5",ipadx="6",ipady="4",fill="y",expand=1)

txt3=Label(win,text="虎吃豹",bg="#cdb5cd",font=14)
txt3.pack(side="left",padx="10",pady="5",ipadx="6",ipady="4",fill="y",expand=1)

txt4=Label(win,text="豹吃狼",bg="#ba55d3",font=14)
txt4.pack(side="left",padx="10",pady="5",ipadx="6",ipady="4",fill="y",expand=1)

txt5=Label(win,text="狼吃狗",bg="#c1ffc1",font=14)
txt5.pack(side="left",padx="10",pady="5",ipadx="6",ipady="4",fill="y",expand=1)

txt6=Label(win,text="狗吃猫",bg="#cdb5cd",font=14)
txt6.pack(side="left",padx="10",pady="5",ipadx="6",ipady="4",fill="y",expand=1)

txt7=Label(win,text="猫吃鼠",bg="#ba55d3",font=14)
txt7.pack(side="left",padx="10",pady="5",ipadx="6",ipady="4",fill="y",expand=1)

txt8=Label(win,text="鼠吃象",bg="#c1ffc1",font=14)
txt8.pack(side="left",padx="10",pady="5",ipadx="6",ipady="4",fill="y",expand=1)

win.mainloop()



