# import matplotlib.pyplot as plt
# import matplotlib.patches as patches
#
# fig, ax = plt.subplots()
#
# # 绘制脸
# face = patches.Circle((0.5, 0.5), 0.4, color='yellow')
# ax.add_patch(face)
#
# # 绘制眼睛
# eye1 = patches.Ellipse((0.3, 0.6), 0.1, 0.2, color='black')
# ax.add_patch(eye1)
# eye2 = patches.Ellipse((0.7, 0.6), 0.1, 0.2, color='black')
# ax.add_patch(eye2)
#
# # 绘制鼻子
# nose = patches.Polygon([[0.5, 0.55], [0.45, 0.5], [0.55, 0.5]], color='brown')
# ax.add_patch(nose)
#
# # 绘制嘴巴
# mouth = patches.Arc((0.5, 0.4), 0.2, 0.1, theta1=0, theta2=180, color='red')
# ax.add_patch(mouth)
#
# # 设置坐标轴范围
# ax.set_xlim(0, 1)
# ax.set_ylim(0, 1)
# ax.axis('off')  # 不显示坐标轴
#
# plt.show()


# import turtle
#
# # 创建一个新的turtle对象
# t = turtle.Turtle()
#
# # 设置画笔速度
# t.speed(1)
#
# # 循环绘制正方形的四个边
# for _ in range(4):
#     t.forward(100)  # 乌龟前进100个单位
#     t.right(90)  # 乌龟右转90度
#
# # 隐藏turtle对象
# t.hideturtle()
#
# # 完成绘制后，保持窗口打开
# turtle.done()


# import turtle
#
# # 创建一个新的turtle对象
# t = turtle.Turtle()
#
# # 设置画笔速度和填充颜色
# t.speed(1)
# t.fillcolor("red")  # 设置填充颜色为红色
#
# # 开始填充图形
# t.begin_fill()
#
# # 绘制一个圆
# t.circle(50)
#
# # 结束填充图形
# t.end_fill()
#
# # 隐藏turtle对象
# t.hideturtle()
#
# # 完成绘制后，保持窗口打开
# turtle.done()

import cv2

# 加载预训练的HOG人物检测器
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# 加载图片
image = cv2.imread('path_to_your_image.jpg')

# 检测人物
(regions, _) = hog.detectMultiScale(image, winStride=(4, 4), padding=(4, 4), scale=1.05)

# 画出人物边界框
for (x, y, w, h) in regions:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

# 显示结果
cv2.imshow('Detected People', image)
cv2.waitKey(0)
cv2.destroyAllWindows()