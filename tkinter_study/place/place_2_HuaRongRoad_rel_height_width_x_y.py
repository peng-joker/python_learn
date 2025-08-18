# place()的使用
# relwidth和 relheight,relx和rely
from tkinter import *
win=Tk()
win.title("华容道")     # 添加窗口标题
win.geometry("240x300")      # 设置窗口大小
txt1=Label(win,text="赵云",bg="#FF1493",relief="solid",font=14)    #华容道游戏中的滑块
txt2=Label(win,text="曹操",bg="#EEEE00",relief="solid",font=14)
txt3=Label(win,text="黄忠",bg="#FF1493",relief="solid",font=14)
txt4=Label(win,text="张飞",bg="#FF1493",relief="solid",font=14)
txt5=Label(win,text="关羽",bg="#FF1493",relief="solid",font=14)
txt6=Label(win,text="马超",bg="#FF1493",relief="solid",font=14)
txt7=Label(win,text="卒",bg="#9932CC",relief="solid",font=14)
txt8=Label(win,text="卒",bg="#9932CC",relief="solid",font=14)
txt9=Label(win,text="卒",bg="#9932CC",relief="solid",font=14)
txt0=Label(win,text="卒",bg="#9932CC",relief="solid",font=14)
# width为组件宽度，height为组件高度，x为滑块左上角定点的横坐标，y为滑块左上角的纵坐标
txt1.place(relwidth=0.25,relheight=0.4,relx=0,rely=0)
txt2.place(relwidth=0.5,relheight=0.4,relx=0.25,rely=0)
txt3.place(relwidth=0.25,relheight=0.4,relx=0.75,rely=0)
txt4.place(relwidth=0.25,relheight=0.4,relx=0,rely=0.4)
txt5.place(relwidth=0.5,relheight=0.2,relx=0.25,rely=0.4)
txt6.place(relwidth=0.25,relheight=0.4,relx=0.75,rely=0.4)
txt7.place(relwidth=0.25,relheight=0.2,relx=0.25,rely=0.6)
txt8.place(relwidth=0.25,relheight=0.2,relx=0.5,rely=0.6)
txt9.place(relwidth=0.25,relheight=0.2,relx=0,rely=0.8)
txt0.place(relwidth=0.25,relheight=0.2,relx=0.75,rely=0.8)
win.mainloop()
