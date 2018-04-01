import tkinter as tk

class LineNumber(tk.Canvas):

    def __init__(self, textArea):
        tk.Canvas.__init__(self, width = 30, bg="pink")
        self.textwidget = None
        # self.__root = textArea.master
        self.__textArea = textArea
        self.attach(textArea)
        self.__showLineNumber()

    def attach(self, text_widget):
        self.textwidget = text_widget

    def __showLineNumber(self):
        self.pack(side="left", fill="y")
        self.__textArea.bind("<<Change>>", self.__onChange)
        self.__textArea.bind("<Configure>", self.__onChange)

    def __onChange(self, event):
        self.redraw()

    def redraw(self):
        '''redraw line numbers'''
        self.delete("all")
        i = self.textwidget.index("@0,0")
        while True :
            dline= self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2,y,anchor="nw", text=linenum)
            i = self.textwidget.index("%s+1line" % i)

