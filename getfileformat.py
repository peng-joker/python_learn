import os
import filetype

def GuessFileType(path_file):
    print('GuessFileType %s ...' % path_file)
    kind = filetype.guess(path_file)
    print('File name: %s' % os.path.basename(path_file))
    print('File extension: %s' % kind.extension)
    print('File MIME type: %s' % kind.mime)

if __name__ == '__main__':
    pathfile = r"/Users/joker/Music/网易云音乐/Taylor Swift - All Too Well (10 Minute Version) (Taylor's Version) (From The Vault).ncm"
    GuessFileType(pathfile)
    # os.remove(filename) # 删除文件
    # os.renames(filename, mainName + "." + getExt) # 重新命名文件