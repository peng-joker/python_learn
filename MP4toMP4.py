from tkinter.filedialog import askdirectory
import tkinter.messagebox as msgbox
import os
import sys

def selectDir():
    filePath = askdirectory()
    newDir = filePath + '/m3u8'
    if sys.platform.startswith('win'):
        newDir = newDir.replace("/","\\\\")
    # elif sys.platform.startswith('darwin'):
        # print('当前操作系统是Mac OS')
    # elif sys.platform.startswith('linux'):
        # print('当前操作系统是Linux')

    # print(newDir)
    # exit()
    # 判断目录是否存在,如不存在创建目录;
    if os.path.exists(newDir) == False:
        build = "mkdir " + newDir
        os.system(build)

    for root, dirs, files in os.walk(filePath):
        for fileName in files:
            # print(os.path.splitext(fileName))
            file_name = os.path.splitext(fileName)[0]
            # print(os.path.splitext(fileName)[1])
            fileType = os.path.splitext(fileName)[1]

            # 新的文件名
            newFile = filePath + '/m3u8/' + file_name + fileType
            if os.path.exists(newFile):
                continue
            if fileType == '.mp4':
                compress = 'ffmpeg -i ' + filePath + '/' + file_name + fileType + ' -c copy ' + newFile
                # print(filePath)
                print(compress)
                os.system(compress)
    msgbox.showinfo("任务完成，请确认！")


if __name__ == '__main__':
    selectDir()