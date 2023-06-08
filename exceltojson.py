import pandas as pd
from tkinter.filedialog import askopenfilename
import tkinter.messagebox as msgbox
import numpy as np
import re
import json

def createExcel():
    data = [['周', '王', '李'], [18, 19, 16], ['男', '男', '女']]
    dfData = {  # 用字典设置DataFrame所需数据
        '姓名': data[0],
        '年龄': data[1],
        '性别': data[2]
    }
    df = pd.DataFrame(dfData)  # 创建DataFrame
    df.to_excel('text.xlsx', index=False)  # 存表，去除原始索引列（0,1,2...）

def selectExcelFile():
    # print("运行成功")
    fileName = askopenfilename()
    # 打开文件,读取文件指定列的内容
    df0 = pd.read_excel(fileName,usecols=[0])
    df1 = pd.read_excel(fileName,usecols=[2])
    df3 = pd.read_excel(fileName,usecols=[4])
    # print(df)
    df_arr0 = np.asarray(df0.stack())
    info_list0 = df_arr0.tolist()
    # print(info_list4)

    df_arr1 = np.asarray(df1.stack())
    info_list1 = df_arr1.tolist()
    # print(info_list1)

    df_arr3 = np.asarray(df3.stack())
    info_list3 = df_arr3.tolist()
    # print(info_list3)
    newList = {}
    keys = []
    for index, info in enumerate(info_list1):
        value = info + info_list3[index]
        # print(value)
        # print(newList.keys)
        # 判断数组中是否存在该 key,如果存在,那么对应的 key 加入一个元素,如果不存在,那么原数组增加一个 key
        if info_list0[index] in keys:
            # newList[info_list0[index]] = newList[info_list0[index]].append(value)
            newList[info_list0[index]].append(value)
            # print(newList)
            # exit()
        else:
            newList[info_list0[index]] = [value]
            keys.append(info_list0[index])


# 需要的数据格式
#     {
#         'key':[1,3,4,5,6],
#         'key2':[1,2,3,4,5,6]
#     }
    print(json.dumps(newList))

if __name__ == '__main__':
    selectExcelFile()