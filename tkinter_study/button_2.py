from tkinter import *                        # 导入 tkinter 模块
from tkinter import ttk                      # 导入 ttk 模块

root = Tk()                                  # 创建根窗口
root.title("这是一个 ttk 小 demo")             # 设置窗口标题

# 获取屏幕尺寸计算参数，使窗口显示在屏幕中央
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 650
height = 500
# window_size = '%dx%d+%d+%d' % (width, height, (screen_width-width)/2, (screen_height-height)/2)
window_size = f'{width}x{height}+{round((screen_width - width) / 2)}+{round((screen_height - height) / 2)}'  # round去掉小数
root.geometry(window_size)  # 窗口大小
# window.resizable(width=False,height=False) #设置窗体是否可用改变大小;默认可用改变

style = ttk.Style()                          # 创建 style 对象,便于设置样式
# 设置样式   添加标签    字号    边框样式    背景颜色
# 如此使用的好处是可以定义一套样式,多处使用
style.configure("TButton", font=14, relief="flat", background='#b75b35')
# 之前使用 btn 接收,但是 ttk.button 没有返回参数,所以去掉
# btn = ttk.Button(text="这只是一个按钮demo2 ", style="TButton").pack(pady=20)
ttk.Button(text="这只是一个按钮demo2 ", style="TButton").pack(pady=1)
ttk.Button(text="按钮套用样式1", style="TButton").pack(pady=1)
ttk.Button(text="按钮套用样式2", style="TButton").pack(pady=1)
ttk.Button(text="按钮套用样式3", style="TButton").pack(pady=1)
root.mainloop()                               # 让程序继续执行,直到窗口被关闭,该行放置在程序的最后
