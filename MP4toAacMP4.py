# 将视频中音频的 audio mp3 格式转为 acc 格式
from tkinter.filedialog import askdirectory
import tkinter.messagebox as msgbox
import subprocess
import os
import sys

def video2mp3(file_path,mp4_name,new_dir,new_mp4_dir):
    """
    将视频转为音频
    :param file_path: 传入视频文件的路径
    :param mp4_name: 传入视频文件名
    :param new_dir: 生成的新的mp3文件的目录
    :param new_mp4_dir: 生成的新的视频文件的目录
    :return:
    """
    mp3_name = new_dir + '/' + mp4_name.split('.')[0] + '-txt.mp3'
    print(mp3_name)
    compress = 'ffmpeg -i ' + file_path + '/' + mp4_name + ' -f mp3 ' + mp3_name
    # print(filePath)
    print(compress)
    os.system(compress)
    # subprocess.call('ffmpeg -i ' + mp4_name + ' -f mp3 ' + mp3_name, shell=True)

    video_add_mp3(file_path,mp4_name,mp3_name,new_mp4_dir)

def video_add_mp3(file_path,mp4_name,mp3_name,new_mp4_dir):
    """
    视频添加音频
    :param file_path: 传入视频文件的路径
    :param mp4_name: 传入视频文件名
    :param mp3_name: 传入音频文件的路径
    :param new_mp4_dir: 生成的新的视频文件的目录
    :return:
    """
    new_mp4_name = new_mp4_dir + '/' + mp4_name.split('.')[0] + '.mp4'
    subprocess.call('ffmpeg -i ' + file_path + '/' +  mp4_name + ' -i ' + mp3_name + ' -strict -2 -f mp4 ' + new_mp4_name, shell=True)


def selectDir():
    file_path = askdirectory()
    new_dir = file_path + '/MP3'
    new_mp4_dir = file_path + '/aac'
    if sys.platform.startswith('win'):
        new_dir = new_dir.replace("/","\\\\")
        new_mp4_dir = new_mp4_dir.replace("/","\\\\")
    elif sys.platform.startswith('darwin'):
        print('当前操作系统是Mac OS')
    # elif sys.platform.startswith('linux'):
        # print('当前操作系统是Linux')
    # 判断目录是否存在,如不存在创建目录;
    if os.path.exists(new_dir) == False:
        build = "mkdir " + new_dir
        os.system(build)

    if os.path.exists(new_mp4_dir) == False:
        build = "mkdir " + new_mp4_dir
        os.system(build)

    for root, dirs, files in os.walk(file_path):
        for file_name in files:
            print(file_name)
            video2mp3(file_path,file_name,new_dir,new_mp4_dir)


def check():
    file_path = askdirectory()
    for root, dirs, files in os.walk(file_path):
        for file_name in files:
            compress = 'ffmpeg -i ' + file_path + '/' + file_name
            print(os.system(compress))

if __name__ == '__main__':
    selectDir()
    # pyinstaller -F pythonFileName.py


