
import tkinter as tk

class MessageDialog():
    response = -1
    def __init__(self, parent, title, message, *buttons):
        _width = 220
        _height = 80
        self.topWindow = tk.Toplevel(parent)
        print(self.topWindow.geometry("{}x{}+{}+{}".format(_width,_height,
                                                           int(self.topWindow.winfo_screenwidth()/2-_width/2),
                                                           int(self.topWindow.winfo_screenheight()/2-_height/2))))
    
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