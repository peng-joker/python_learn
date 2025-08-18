# sticky 的使用: N上对齐 S下对齐 W左对齐 E右对齐
# columnspan的使用
from tkinter import *
win=Tk()
win.title("sticky的使用")
Label(win,text="春花秋月何时了,往事知多少",bg="#3d3223",relief="groove").grid(row=0,column=0)
Label(win,text="小楼昨夜又东风,故国不堪回首月明中",bg="#EEA9B8",relief="groove").grid(row=1,column=0)

Label(win,text="",relief="groove").grid(row=2,column=0)

Label(win,text="春花秋月何时了,往事知多少",bg="#F08080",relief="groove").grid(row=3,column=0,sticky=W)
Label(win,text="小楼昨夜又东风,故国不堪回首月明中",bg="#FFE1FF",relief="groove").grid(row=4,column=0)

Label(win,text="",relief="groove").grid(row=5,column=0,sticky=N)

Label(win,text="春花秋月何时了,往事知多少",bg="#F08080",relief="groove").grid(row=6,column=0,sticky=E)
Label(win,text="小楼昨夜又东风,故国不堪回首月明中",bg="#FFE1FF",relief="groove").grid(row=7,column=0)

Label(win,text="",relief="groove").grid(row=8,column=0,sticky=N)

Label(win,text="春花秋月何时了,往事知多少",bg="#F08080",relief="groove").grid(row=9,column=0,sticky=E+W)
Label(win,text="小楼昨夜又东风,故国不堪回首月明中",bg="#FFE1FF",relief="groove").grid(row=10,column=0)

Label(win,text="",relief="groove").grid(row=11,column=0,sticky=N)

Label(win,text="春花秋月何时了,往事知多少",bg="#F08080",relief="groove").grid(row=12,column=0,columnspan=2,sticky=E)
Label(win,text="小楼昨夜又东风,故国不堪回首月明中",bg="#FFE1FF",relief="groove").grid(row=13,column=0,columnspan=2,sticky=E+W)
Label(win,text="雕栏玉砌应犹在,只是朱颜改。问君能有几多愁？恰似一江春水向东流",bg="#EEA9B8",relief="groove").grid(row=13,column=2,columnspan=4,sticky=E+W)

Label(win,width=10,height=1,bg="#FFE1FF",relief="groove").grid(row=14,column=0)
Label(win,width=10,height=1,bg="#FFE1FF",relief="groove").grid(row=14,column=1)

Label(win,width=5,height=1,bg="#FFE1FF",relief="groove").grid(row=14,column=2,sticky=E+W)
Label(win,width=10,height=1,bg="#FFE1FF",relief="groove").grid(row=14,column=3,sticky=E+W)
Label(win,width=15,bg="#FFE1FF",relief="groove").grid(row=14,column=4,sticky=E+W)
Label(win,width=20,bg="#FFE1FF",relief="groove").grid(row=14,column=5,rowspan=2,sticky=E+W+S+N)

Label(win,width=20,bg="#FFE1FF",relief="groove").grid(row=15,column=0)


win.mainloop()