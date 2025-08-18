# label组件的使用
# 加载图片

from tkinter import *
win=Tk()
win.title("欢乐写数字")
win.configure(bg="#EEF3C3")   #设置窗口的背景颜色
img=PhotoImage(file="game.png")  #创建图片对象
#在Label中添加图片和文字，compound表示图片在文字下方
game=Label(win,image=img,text="欢乐写数字",compound="bottom",font="楷体 20 bold",fg="#D25EED",bg="#EEF3C3")
game.grid(row=2,column=0,columnspan=2)
# 添加文字
Label(win,text="输入兑奖码领取稀有道具",bg="#EEF3C3",fg="#1e1f22").grid(row=3,column=0,columnspan=2)
Label(win,text="兑奖码：",font=14,bg="#EEF3C3",fg="#1e1f22").grid(row=4,column=0,sticky=E,pady=10)
Label(win,width=15,bg="#fff",relief="groove").grid(row=4,column=1,pady=10)
Label(win,text="确认兑换",width=20,relief="groove",bg="#0996ED").grid(row=5,column=0,columnspan=2,pady=5)
win.mainloop()
