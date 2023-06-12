from tkinter import *
def Mysel():
      dic = {0:'替换',1:'前缀',2:'后缀'}
      s = "您选了" + dic.get(var.get()) + "项"
      lb.config(text = s)

root = Tk()
root.title('单选按钮')
root.geometry('200x100') # 这里的乘号不是 * ，而是小写英文字母 x
lb = Label(root)
lb.pack()

var = IntVar()
rd1 = Radiobutton(root,text="替换",variable=var,value=0,command=Mysel)
rd1.pack(side=LEFT,fill=X)

rd2 = Radiobutton(root,text="前缀",variable=var,value=1,command=Mysel)
rd2.pack(side=LEFT,fill=X)

rd3 = Radiobutton(root,text="后缀",variable=var,value=2,command=Mysel)
rd3.pack(side=LEFT,fill=X)

root.mainloop()