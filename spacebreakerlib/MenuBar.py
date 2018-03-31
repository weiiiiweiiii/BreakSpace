#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Liangze Yu
"""
import tkinter as tk
from spacebreakerlib.RecentFiles import RecentFiles

class MenuBar(tk.Menu):

    def __init__(self, textArea):

        self.__textArea = textArea
        self.__root = textArea.master
        
        #high-level
        tk.Menu.__init__(self,self.__root)

        #subMenu
        self.__subMenu()

        self.__root.config(menu = self)

    def __subMenu(self):
        FileMenu(self,self.__textArea)
        HelpMenu(self,self.__textArea)
        FontMenu(self,self.__textArea)

class FileMenu(tk.Menu):

    def __init__(self,masterMenu,textArea):
        tk.Menu.__init__(self,masterMenu)

        #binds
        self.__textArea = textArea
        self.__root = textArea.master

        #lists
        self.__commands()
        self.__cascade()

    def __commands(self):
        #new
        self.add_command(label="New File",command=self.__textArea.textRelatedObjs['New'],accelerator="Command-n") 
        #open
        self.add_command(label="Open...",command=self.__textArea.textRelatedObjs['Open'],accelerator="Command-o")
        #save
        self.add_command(label="Save",command=self.__textArea.textRelatedObjs['Save'],accelerator="Command-s")
        # seperate from above    
        self.add_separator()
        #close
        self.add_command(label="Close",command = self.__textArea.textRelatedObjs['Exit'],accelerator="Command-w")
        
        # added
        self.add_command(label="Save As", command = self.__textArea.textRelatedObjs['SaveAs'], accelerator="Command-Shift-s")
        
        
        recentMenu = tk.Menu(self)
        self.add_cascade(label="Open Recent", menu=recentMenu)
        
        _file_names = RecentFiles.getRecentFiles()
        if len(_file_names) > 0:
            for name in _file_names:
                recentMenu.add_command(label=name, command=self.__openWithNameHelper(name))
        else:
            recentMenu.add_command(label="No Recent File", state=tk.DISABLED)
        
    def __cascade(self):
        self.master.add_cascade(label="File", menu = self) 
    
    def __openWithNameHelper(self, f_name):
        def f():
            self.__textArea.textRelatedObjs['OpenWithName'](f_name)
        return f


class HelpMenu(tk.Menu):

    def __init__(self,masterMenu,textArea):
        tk.Menu.__init__(self,masterMenu)

        #binds
        self.__textArea = textArea
        self.__root = textArea.master

        #lists
        self.__commands()
        self.__cascade()
        
    def __commands(self):
        #about
        self.add_command(label="About Space Breaker",command= self.__showAbout) 

    def __cascade(self):
        self.master.add_cascade(label="Help", menu = self)

    def __showAbout(self):
        import tkinter.messagebox as tm
        tm.showinfo("Space Breaker","Bai,Dayue\nHuai,Yuqi\nWang,Baihao\nYu,Liangze")

# FONTS FUNCTIONALITY
class FontMenu(tk.Menu):

    def __init__(self,masterMenu,textArea):
        tk.Menu.__init__(self,masterMenu)

        #binds
        self.__textArea = textArea
        self.__root = textArea.master
        
        #lists
        self.__commands()
        self.__cascade()

    def __commands(self):
        #bold
        self.add_command(label="Bold",command=self.__textArea.textRelatedObjs['font_bold'],accelerator="Command-b") 
        #italic
        self.add_command(label="Italic",command=self.__textArea.textRelatedObjs['font_italic'],accelerator="Command-i")
        #underline
        self.add_command(label="Underline",command=self.__textArea.textRelatedObjs['font_underline'],accelerator="Command-u")
        
#         # seperate from above    
#         self.add_separator()
#         #close
#         self.add_command(label="Close",command = self.__textArea.textRelatedObjs['Exit'],accelerator="Command-w")
        pass
    
    def __cascade(self):
        self.master.add_cascade(label="Font", menu = self) 
    

        