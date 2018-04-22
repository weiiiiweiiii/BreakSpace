import tkinter as tk

class ExitDialog(tk.Toplevel):
    response = -1
    __width = 220
    __height = 80
    def __init__(self, parent, title, message, *buttons):
        tk.Toplevel.__init__(self,parent)
        self.geometry("{}x{}+{}+{}".format(self.__width,self.__height,
                                           int(self.winfo_screenwidth()/2-self.__width/2),
                                           int(self.winfo_screenheight()/2-self.__height/2)))
    
        self.title(title)
        tk.Label(self, text="你他妈没保存！存吗？确定退出吗？").pack()
        self.response = -1
        
        for b in buttons:
            tk.Button(self, text=b[1], command = self.__setResponse(b[0])).pack(side=tk.LEFT)

        self.grab_set()
            
    def __setResponse(self, r):
        def f():
            self.response = r
            self.__close()
        return f

    def __close(self,event = None):
        self.grab_release()
        self.destroy()
        
    def getResponse(self):
        return self.response
