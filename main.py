from tkinter.filedialog import askdirectory
import tkinter.messagebox as msgbox
import os

def selectDir():
    filePath = askdirectory()
    txt = filePath + "/file_name.txt"
    file_list = ""
    if os.path.exists(txt):
        os.remove(txt)
    for root, dirs, files in os.walk(filePath):
        for fileName in files:
            f = open(txt, 'a')  # 以追加方式打开文件
            fileName = os.path.splitext(fileName)[0] + '\n'  # 分割，不带后缀名
            f.write(fileName)
            file_list += fileName + "\n"
            f.close()

    msgbox.showinfo("墨智科技-获取目录："+filePath+" 下面的文件",file_list)

if __name__ == '__main__':
    selectDir()