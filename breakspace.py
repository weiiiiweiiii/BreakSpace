#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 16:48:44 2018Created on Tue Feb 27 16:48:44 2018

@author: Yuliangze
"""
import os
import tkinter as tk
import tkinter.messagebox as tm
import tkinter.filedialog as tf
from tkinter.font import Font

class Spacebreaker:

    __root = tk.Tk()

    # default window width and height
    __winWidth = 584
    __winHeight = 406

    #components:
    #Text Area
    __textArea = tk.Text(__root, wrap = tk.NONE)

    #Vertical and Horizontal Scrollbars
    __yScrollbar = tk.Scrollbar(__root, orient = tk.VERTICAL)
    __xScrollbar = tk.Scrollbar(__root, orient = tk.HORIZONTAL)

    #sizegrip
    #__sizegrip = ttk.Sizegrip(__root)

    #High-level Menu
    __menuBar = tk.Menu(__root)
    #components
    __fileMenu = tk.Menu(__menuBar)
    __helpMenu = tk.Menu(__menuBar)

    #New,Open,Save
    __file = None

    def __init__(self,**kwargs):
        
        #get title
        self.__root.title("Untitled - Space Breaker")
        #widthXheight + x + y
        #screen sizes
        sWidth = self.__root.winfo_screenwidth()
        sHeight = self.__root.winfo_screenheight()
        #window sizes
        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass
        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass
        # pc left to win left
        left = int((sWidth / 2) - (self.__winWidth / 2))
        # pc top to win top
        top = int((sHeight / 2) - (self.__winHeight /2))
        self.__root.geometry(f'{self.__winWidth}x{self.__winHeight}+{left}+{top}')
        #resize
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)
        
        #text
        self.__textArea.grid(row = 0, column = 0, sticky = tk.N + tk.E + tk.S + tk.W)

        #yScrollbar
        #position
        self.__yScrollbar.grid(row = 0, column = 1, sticky = tk.N+tk.S)
        #connection
        self.__yScrollbar.config(command= self.__textArea.yview)
        self.__textArea.config(yscrollcommand = self.__yScrollbar.set)

        #xScrollbar
        self.__xScrollbar.grid(row = 1, columnspan = 2, sticky = tk.E+tk.W)
        self.__xScrollbar.config(command= self.__textArea.xview)
        self.__textArea.config(xscrollcommand = self.__xScrollbar.set)

        #Menu
        #high-level
        self.__root.config(menu=self.__menuBar)
        #File
        #new
        self.__fileMenu.add_command(label="New File",command=self.__newFile,accelerator="Command-n") 
        #open
        self.__fileMenu.add_command(label="Open...",command=self.__openFile,accelerator="Command-o")
        #save
        self.__fileMenu.add_command(label="Save",command=self.__saveFile,accelerator="Command-s") 
        # seperate from above    
        self.__fileMenu.add_separator()                                         
        self.__fileMenu.add_command(label="Close",command = self.__exit,accelerator="Command-w")
        self.__menuBar.add_cascade(label="File",menu=self.__fileMenu)        
        #Help
        #description
        self.__helpMenu.add_command(label="About Space Breaker",command=self.__showAbout) 
        self.__menuBar.add_cascade(label="Help",menu=self.__helpMenu)

        #key shortcuts
        #new file
        self.__root.bind("<Command-n>",self.__newFile)
        #open file
        self.__root.bind("<Command-o>",self.__openFile)
        #save file
        self.__root.bind("<Command-s>",self.__saveFile)
        #exit
        self.__root.bind("<Command-w>",self.__exit)

        #bold button
        self.__bold_btn = tk.Button(self.__root, text="Bold", command=self.__make_bold)
        self.__bold_btn.grid(row = 2,column = 0)
        self.__bold_font = Font(weight="bold")
        self.__textArea.tag_configure("BOLD", font=self.__bold_font)
        
    def __make_bold(self):
        # tk.TclError exception is raised if not text is selected
        try:
            self.__textArea.tag_add("BOLD", "sel.first", "sel.last")
        except tk.TclError:
            pass

    #need take in event for shortcut method
    def __newFile(*args):
        self = args[0]
        #change title
        self.__root.title("Untitled - Space Breaker")
        #reset __file
        self.__file = None
        #clean content
        self.__textArea.delete(1.0,tk.END)

    def __openFile(*args):
        self = args[0]
        #pop out dialog
        self.__file = tf.askopenfilename(defaultextension=".txt",
                                    filetypes=[("All Files","*.*"),
                                        ("Text Documents","*.txt"),("Python Files","*.py")])
        #open nothing
        if self.__file == "":
            #reset __file
            self.__file = None
        else:
            self.__root.title(os.path.basename(self.__file) + " - Space Breaker")
            #clean content
            self.__textArea.delete(1.0,tk.END)

            #open file
            file = open(self.__file,"r")
            #insert content
            self.__textArea.insert(1.0,file.read())
            #finish insertion
            file.close()
            
    def __saveFile(*args):
        self = args[0]
        if self.__file == None:
            # Save as new file
            self.__file = tf.asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files","*.*"),
                                                ("Text Documents","*.txt")])
            #stop saving and reset __file
            if self.__file == "":
                self.__file = None
            else:
                # open and write
                file = open(self.__file,"w")
                file.write(self.__textArea.get(1.0,tk.END))
                file.close()
                # Change title
                self.__root.title(os.path.basename(self.__file) + " - Space Breaker")
        #opened file
        else:
            file = open(self.__file,"w")
            file.write(self.__textArea.get(1.0,tk.END))
            file.close()

    def __exit(*args):
        self = args[0]
        self.__root.destroy()

    def __showAbout(self):
        tm.showinfo("Space Breaker","Bai,Dayue\nHuai,Yuqi\nWang,Baihao\nYu,Liangze")
                   
    def run(self):
        self.__root.mainloop()



if __name__ == "__main__":
    a = Spacebreaker()
    a.run()
    























        
