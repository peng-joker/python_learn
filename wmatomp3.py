# change *.wma files to *.mp3 at current folder
import os
import subprocess
def wma2mp3(wma_path, mp3_path=None):
    path, name = os.path.split(wma_path)
    if name.split('.')[-1] != 'wma':
        print('not a wma file')
        return 0
    if mp3_path is None or mp3_path.split('.')[-1] != 'mp3':
        mp3_path = os.path.join(path, name.split('.')[0] + '.mp3')
    error = subprocess.call(['ffmpeg', '-i', wma_path, mp3_path])
    print(wma_path, ' was changed to .MP3')
    if error:
        return 0
        # print('NOT success')
    print('success')
    # return mp3_path


if __name__ == '__main__':
    for d, sd, files in os.walk('.'):
        for f in files:
            wma_path = os.path.join(d, f)
            (prefix, sep, suffix) = wma_path.rpartition('.')
            if suffix != 'wma':
                continue
            mp3_path = prefix + '.mp3'
            wma2mp3(wma_path)
