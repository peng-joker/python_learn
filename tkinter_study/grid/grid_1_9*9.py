# grid()的使用
# row表示行，column表示列
# 九九乘法表

from tkinter import *
win=Tk()     #创建根窗口
win.title("九九乘法表")    # 添加标题
# grid(row=0,column=0,padx=10)设置组件位于第0行第0列，与其他组件的水平间距为10
Label(win,text="1*1=1",bg="#3d3223").grid(row=0,column=0,padx=10)
Label(win,text="1*2=3",bg="#3d3223").grid(row=1,column=0,padx=10)
Label(win,text="1*3=3",bg="#3d3223").grid(row=2,column=0,padx=10)
Label(win,text="1*4=4",bg="#3d3223").grid(row=3,column=0,padx=10)
Label(win,text="1*5=5",bg="#3d3223").grid(row=4,column=0,padx=10)
Label(win,text="1*6=6",bg="#3d3223").grid(row=5,column=0,padx=10)
Label(win,text="1*7=7",bg="#3d3223").grid(row=6,column=0,padx=10)
Label(win,text="1*8=8",bg="#3d3223").grid(row=7,column=0,padx=10)
Label(win,text="1*9=9",bg="#3d3223").grid(row=8,column=0,padx=10)

Label(win,text="2*2=4",bg="#EEA9B8").grid(row=1,column=1,padx=10)
Label(win,text="2*3=6",bg="#EEA9B8").grid(row=2,column=1,padx=10)
Label(win,text="2*4=8",bg="#EEA9B8").grid(row=3,column=1,padx=10)
Label(win,text="2*5=10",bg="#EEA9B8").grid(row=4,column=1,padx=10)
Label(win,text="2*6=12",bg="#EEA9B8").grid(row=5,column=1,padx=10)
Label(win,text="2*7=14",bg="#EEA9B8").grid(row=6,column=1,padx=10)
Label(win,text="2*8=16",bg="#EEA9B8").grid(row=7,column=1,padx=10)
Label(win,text="2*9=18",bg="#EEA9B8").grid(row=8,column=1,padx=10)

Label(win,text="3*3=9 ",bg="#F08080").grid(row=2,column=2,padx=10)
Label(win,text="3*4=12",bg="#F08080").grid(row=3,column=2,padx=10)
Label(win,text="3*5=15",bg="#F08080").grid(row=4,column=2,padx=10)
Label(win,text="3*6=18",bg="#F08080").grid(row=5,column=2,padx=10)
Label(win,text="3*7=21",bg="#F08080").grid(row=6,column=2,padx=10)
Label(win,text="3*8=24",bg="#F08080").grid(row=7,column=2,padx=10)
Label(win,text="3*9=27",bg="#F08080").grid(row=8,column=2,padx=10)

Label(win,text="4*4=16",bg="#FFE1FF").grid(row=3,column=3,padx=10)
Label(win,text="4*5=20",bg="#FFE1FF").grid(row=4,column=3,padx=10)
Label(win,text="4*6=24",bg="#FFE1FF").grid(row=5,column=3,padx=10)
Label(win,text="4*7=28",bg="#FFE1FF").grid(row=6,column=3,padx=10)
Label(win,text="4*8=32",bg="#FFE1FF").grid(row=7,column=3,padx=10)
Label(win,text="4*9=36",bg="#FFE1FF").grid(row=8,column=3,padx=10)

Label(win,text="5*5=25",bg="#20363a").grid(row=4,column=4,padx=10)
Label(win,text="5*6=30",bg="#20363a").grid(row=5,column=4,padx=10)
Label(win,text="5*7=35",bg="#20363a").grid(row=6,column=4,padx=10)
Label(win,text="5*8=40",bg="#20363a").grid(row=7,column=4,padx=10)
Label(win,text="5*9=45",bg="#20363a").grid(row=8,column=4,padx=10)

Label(win,text="6*6=36",bg="#f5eea3").grid(row=5,column=5,padx=10)
Label(win,text="6*7=42",bg="#f5eea3").grid(row=6,column=5,padx=10)
Label(win,text="6*8=48",bg="#f5eea3").grid(row=7,column=5,padx=10)
Label(win,text="6*9=54",bg="#f5eea3").grid(row=8,column=5,padx=10)

Label(win,text="7*7=49",bg="#e15941").grid(row=6,column=6,padx=10)
Label(win,text="7*8=56",bg="#e15941").grid(row=7,column=6,padx=10)
Label(win,text="7*9=63",bg="#e15941").grid(row=8,column=6,padx=10)

Label(win,text="8*8=64",bg="#eba13a").grid(row=7,column=7,padx=10)
Label(win,text="8*9=72",bg="#eba13a").grid(row=8,column=7,padx=10)

Label(win,text="9*9=81",bg="#888b8b").grid(row=8,column=8,padx=10)

win.mainloop()
