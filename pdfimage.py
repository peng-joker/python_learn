from tkinter.filedialog import askopenfilename
from pdf2image import convert_from_path
import os
import sys

def pdf2image2():
    file_path = askopenfilename()
    # fileName = "/Users/joker/Desktop/FC5-card-pic-NOCN.pdf"
    # print(fileName)
    # /Users/joker/Desktop/FC5-card-pic-NOCN.pdf
    # # 从最后一位/的下标,并截取字符
    # print(fileName.rfind("/"))
    # print(fileName[0:fileName.rfind("/")+1])
    #
    # # 查找最后一个.的下标,并截取字符串
    # print(fileName.rfind('.'))
    # print(fileName[fileName.rfind("/")+1:fileName.rfind('.')])

    # 新建目录保存图片文件
    imageDir = file_path[0:file_path.rfind("/")+1] + file_path[file_path.rfind("/")+1:file_path.rfind('.')] + '_pdf_image'

    images = convert_from_path(file_path, dpi=200)
    for image in images:
        if not os.path.exists(imageDir):
            os.makedirs(imageDir)
        imageName = imageDir + '/img_' + str(images.index(image)) + '.png'
        image.save(imageName, 'PNG')


if __name__ == '__main__':
    pdf2image2()