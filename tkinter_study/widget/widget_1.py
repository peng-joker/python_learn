from tkinter import *

win = Tk()
win.geometry("300x200")
Label(win, text="1.小扣柴扉久不开--和 2 一样", foreground="red", background="#C3DEEF").pack()
Label(win, text="2.小扣柴扉久不开--和 1 一样", fg="red", bg="#C3DEEF").pack()
Label(win, text="3.小扣柴扉久不开", fg="red", bg="pink",width=20,height=3,anchor='center').pack()
Label(win, text="4.小扣柴扉久不开", fg="red", bg="white",width=20,height=3,anchor='nw').pack() # anchor 设置文字在组件中的位置, center默认中间 东(e) 西(w) 南(s) 北(n) 南东(se) 南西(sw) 北东(ne) 北西(nw)
Label(win, text="5.小扣柴扉久不开", fg="red", bg="white",width=20,height=3).pack(anchor='nw') # anchor 设置文字在组件中的位置, center默认中间 东(e) 西(w) 南(s) 北(n) 南东(se) 南西(sw) 北东(ne) 北西(nw)

win.mainloop()