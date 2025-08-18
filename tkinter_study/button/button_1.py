from tkinter import *                       # 导入 tkinter 模块
win = Tk()                                  # 实例化窗口
win.title("这是一个 ttk 小 demo")             # 添加窗口标题
# 添加按钮组件   文字    字号    边框样式    背景颜色    包装按钮(目的让按钮显示在窗口)
Button(win, text="这只是一个按钮demo1", font=14, relief="flat", bg="#b75b35").pack(pady=20)
win.mainloop()                              # 让程序继续执行,直到窗口被关闭,该行放置在程序的最后
