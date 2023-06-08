# 书写Bright Phonics Starter pp.2-5,书写Copybook Aa-Ff*4,预习-听、读 Bright Talk Starter - Unit 1 pp.6-7,预习-听、读 Bright Phonics Starter pp.6-9
# 需求来源:邓小锐,线下任务,根据","换行,并且标记 序列号从 1 开始,序列号顺序:"1."  "2." "3."
import pandas as pd
from tkinter.filedialog import askopenfilename
import tkinter.messagebox as msgbox
import numpy as np
import re

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
    df = pd.read_excel(fileName,usecols=[4])
    # print(df)

    dr = pd.read_excel(fileName, header=[0, ])  # 取第二行的数据作为索引，我这里的索引在第二行
    col_name = dr.columns.tolist()  # 获取表头
    col_name.append('内容汇总(已排序)')
    # print(col_name)
    # 新的表头
    dr = dr.reindex(columns=col_name)


    df_arr = np.asarray(df.stack())
    info_list = df_arr.tolist()
    # print(info_list)
    # print(df.head(2))
    for index,info in enumerate(info_list):
        # print(info_list[index])
        # 根据字符中的','出现的次数,将数据转化为 list
        # print(info.split(','))
        info = info.split(',')

        list = []
        for index1,info1 in enumerate(info):
            # 去除元素首尾的空格
            info1 = info1.strip()
            if index1>0:
                last = list[len(list)-1]
            if bool(re.match('^[1234567890-]+$', info1)):
                list[len(list) - 1] = last + ','+info1
            else:
                list.append(info1)

        info = list
        # if index == 14:
        #     print(info)
        #     print(list)
        #     exit()
        for indexNew,infoNew in enumerate(info):
            # 判断是否是纯数字,如果是,弹窗提示
            if infoNew.isnumeric():
                print(infoNew, "：是数字"+",元数据序号为" + str(index))
            info[indexNew] = str(indexNew+1) + '.' + infoNew
        info = "；\r\n".join(info)
        # print(info)
        info_list[index] = info
        # print(info_list[index])
        # exit()

    dr["内容汇总(已排序)"] = info_list
    # 修改 excel 中对应列的数据
    dr.to_excel(fileName,index=False)
    msgbox.showinfo("任务完成，请确认！")

if __name__ == '__main__':
    selectExcelFile()