
import tkinter as tk

class MessageDialog():
    response = -1
    def __init__(self, parent, title, message, *buttons):
        self.topWindow = tk.Toplevel(parent)
        self.topWindow.title("这是一条警告信息！")
        tk.Label(self.topWindow, text="你他妈没保存！存吗？确定退出吗？").pack()
        MessageDialog.response = -1
        
        for b in buttons:
            tk.Button(self.topWindow, text=b[1], command = self.setResponse(b[0])).pack(side=tk.LEFT)
            
    def setResponse(self, r):
        def f():
            MessageDialog.response = r
            self.topWindow.destroy()
        return f
    
    def run(self):
        self.topWindow.mainloop()
        
    def getResponse(self):
        return MessageDialog.response