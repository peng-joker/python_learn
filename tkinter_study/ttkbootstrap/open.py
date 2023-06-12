import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter.filedialog import askopenfilename
root = ttk.Window()
def open_file():
    path = askopenfilename()
    # print(path)
    if not path:
        return
ttk.Button(root, text="打开文件", command=open_file).pack(fill=X, padx=10, pady=10)
root.mainloop()