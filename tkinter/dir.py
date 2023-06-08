import tkinter as tk
import os

# 创建窗口
window = tk.Tk()
window.title("本地目录")
window.geometry("600x400")

# 创建左侧框架
left_frame = tk.Frame(window, width=200, height=400)
left_frame.pack(side=tk.LEFT, fill=tk.Y)

# 创建滚动条
scrollbar = tk.Scrollbar(left_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# 创建文件列表
file_list = tk.Listbox(left_frame, yscrollcommand=scrollbar.set)
file_list.pack(side=tk.LEFT, fill=tk.BOTH)

# 获取当前目录
current_path = os.getcwd()

# 获取目录下的文件列表
files = os.listdir(current_path)

# 添加文件列表到 Listbox 中
for file in files:
    file_list.insert(tk.END, file)

# 绑定滚动条和文件列表
scrollbar.config(command=file_list.yview)

# 运行窗口
window.mainloop()
