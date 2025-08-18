# 视频中提取音频
import os
import ffmpy
# from ffmpy import ffmpeg

# 获取文件名称
def getName(video_path):
    return os.path.basename(video_path).split('.')[0]

# 提取并另存为
def run_ffmpeg(video_path: str, audio_path: str, format: str):
    ff = ffmpy.FFmpeg(inputs={video_path: None},
                outputs={audio_path: '-f {} -vn'.format(format)})
    ff.run()
    return audio_path

# 参数接受处理
def extract(video_path: str, tmp_dir: str, ext: str):
    file_name = '.'.join(os.path.basename(video_path).split('.')[0:-1])
    return run_ffmpeg(video_path, os.path.join(tmp_dir, '{}.{}'.format(getName(video_path), ext)), ext)


def video2mp3(file_name):
    """
    将视频转为音频
    :param file_name: 传入视频文件的路径
    :return:
    """
    outfile_name = file_name.split('.')[0] + '-txt.mp3'
    subprocess.call('ffmpeg -i ' + file_name + ' -f mp3 ' + outfile_name, shell=True)




if __name__ == '__main__':
    root = "/Users/joker/Desktop/"
    print(video2mp3(root + 'notok.mp4'))

#     print(extract(root + 'notok.mp4', root, 'mp3'))