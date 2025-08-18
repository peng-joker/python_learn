from tkinter import *
win=Tk()
win.title("tkinter的窗口的位置")              # 窗口的标题
win.configure(bg="#a7ea90")                 # 窗口的背景颜色
win_w = 300                                 # 窗口的宽度
win_h = 220                                 # 窗口的高度
scr_w = win.winfo_screenwidth()             # 屏幕的宽度
scr_h = win.winfo_screenheight()            # 屏幕的高度
x = (scr_w-win_w)/2                         # 窗口的水平位置
y = (scr_h-win_h)/2                         # 窗口的垂直位置
win.geometry("%dx%d+%d+%d" %(win_w,win_h,x,y))            # 设置窗口位置
string = "\n\n程序员鄙视链\n\n一等码农搞算法，吃香喝辣调调参\n\n二等码农搞架构，高并低延能吹牛\n\n三等码农搞工程，怼天怼地怼PM\n\n四等码农搞前端，浮层像素老黄牛"
Label(win,text=string,bg="#a7ea90").pack()
win.mainloop()
