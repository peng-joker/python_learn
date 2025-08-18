from pydub import AudioSegment
from tkinter.filedialog import askdirectory
import os

def trans_flac_to_other(filepath, hz):
    song = AudioSegment.from_file(filepath)
    save_dir = os.path.split(filepath)[0]
    file_name = fileName(filepath)
    song.export(save_dir + '/' + file_name + "." + str(hz), format=str(hz))
    print(save_dir + '/' + file_name + "." + str(hz))

def selectFile():
    # 弹出目录选择窗口
    filePath = askdirectory()
    for root, dirs, files in os.walk(filePath):
        for file in files:
            info = file.split('.')
            if info[len(info)-1]=="flac":
                trans_flac_to_other(os.path.join(root, file),"mp3")

def fileName(filepath):
    li = os.path.split(filepath)
    return li[len(li)-1].split(".flac")[0]

if __name__ == '__main__':
    selectFile()
