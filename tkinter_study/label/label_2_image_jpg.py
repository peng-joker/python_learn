# label组件的使用
# 加载jpg 格式图片
from tkinter import *
from PIL import Image,ImageTk
win=Tk()
win.title("JPG 格式图片的加载")
image_file=Image.open('jpg_image.jpg')
# 创建图片对象
img=ImageTk.PhotoImage(image_file)
# 在Label中添加图片
Label(win,image=img).pack()
win.mainloop()
