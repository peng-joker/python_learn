from tkinter import *
win=Tk()                      #创建根窗口
win.geometry("350x150")       #设置窗口大小
win.title("tkinter的初使用")  #设置窗口标题
txt1=Label(win,text="确定退出本窗口吗？")
txt2=Label(win,text="果断退出txt2",bg="#c1ffc1")
txt3=Label(win,text="我再想想txt3",bg="#cdb5cd")
txt1.pack(fill="x",pady="20")      #fill='x'设置组件始终水平居中显示
# side和anchor组合实现组件有窗口右下角显示
## 此处的前面和后面相对于 side 而言,即在前面的更靠近 side值 那一边,比如:side 为 right,那么在前面的更靠近右边
# txt2.pack(side="right",padx="10",ipadx="6",pady="20",anchor="s")
# txt3.pack(side="right",padx="10",ipadx="6",pady="20",anchor="s")

txt2.pack(side="right",padx="10",ipadx="6",pady="20",anchor="s")
txt3.pack(side="right",padx="10",ipadx="6",pady="20",anchor="s",after=txt2) # after 表示txt3 在txt2 后面,默认 txt3 在txt2 后面

# txt2.pack(side="right",padx="10",ipadx="6",pady="20",anchor="s")
# txt3.pack(side="right",padx="10",ipadx="6",pady="20",anchor="s",before=txt2)# before 表示txt3 在txt2 前面,默认 txt2 在txt3 前面

win.mainloop()
