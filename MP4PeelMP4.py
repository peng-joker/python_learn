# 视频中合并音频
import subprocess
# import imageio
import os
from PIL import Image
def video_add_mp3(file_name, mp3_file):
    """
    视频添加音频
    :param file_name: 传入视频文件的路径
    :param mp3_file: 传入音频文件的路径
    :return:
    """
    outfile_name = file_name.split('.')[0] + '-txt.mp4'
    subprocess.call('ffmpeg -i ' + file_name + ' -i ' + mp3_file + ' -strict -2 -f mp4 ' + outfile_name, shell=True)
    print(1)

if __name__ == '__main__':
    root = "/Users/joker/Desktop/"
    video_add_mp3(root + 'notok.mp4', root + 'notok.mp3')