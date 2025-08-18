# label组件的使用
# 加载jpg 格式图片
from tkinter import *
win=Tk()
win.configure(bg='#c9ede8')
win.maxsize(500,500)
couple = "上联：足不出户一台电脑打天下下联：我宅在家一双巧手定乾坤横批：量我风采"
Label(win,text=couple,wraplength=190,justify="left",font=14).pack(padx=20,pady=20)
win.mainloop()