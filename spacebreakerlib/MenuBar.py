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
        EditMenu(self,self.__textArea)
        FormatMenu(self,self.__textArea)
        FontMenu(self,self.__textArea)
        HelpMenu(self,self.__textArea)


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
        
        self.add_command(label="Open in new window", command = self.__textArea.textRelatedObjs['OpenInNewWindow'])
        
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
    
class EditMenu(tk.Menu):

    def __init__(self,masterMenu,textArea):
        tk.Menu.__init__(self,masterMenu)

        self.__textArea = textArea
        self.__root = textArea.master

        self.__commands()
        self.__cascade()

    def __commands(self):
        self.add_command(label = 'Undo', command = self.__textArea.textRelatedObjs['Undo'],accelerator="Command-z")
        self.add_command(label = 'Redo', command = self.__textArea.textRelatedObjs['Redo'],accelerator="Command-Shift-z")
        self.add_separator()
        self.add_command(label = 'Copy', command = self.__textArea.textRelatedObjs['Copy'],accelerator="Command-c")
        self.add_command(label = 'Cut', command = self.__textArea.textRelatedObjs['Cut'],accelerator="Command-x")
        self.add_command(label = 'Paste', command = self.__textArea.textRelatedObjs['Paste'],accelerator="Command-v")
        self.add_command(label = 'SelectAll', command = self.__textArea.textRelatedObjs['SelectAll'],accelerator="Command-a")
        self.add_separator()
        self.add_command(label = 'Find', command = self.__textArea.textRelatedObjs['Find'],accelerator='Command-f')
        self.add_separator()
        self.add_command(label = 'Jump To Line Start', command = self.__textArea.textRelatedObjs['JumpToLineStart'],accelerator="Control-,")
        self.add_command(label = 'Jump To Line End', command = self.__textArea.textRelatedObjs['JumpToLineEnd'],accelerator="Control-.")
        self.add_command(label = 'Jump To File Start', command = self.__textArea.textRelatedObjs['JumpToFileStart'],accelerator="Control-0")
        self.add_command(label = 'Jump To File End', command = self.__textArea.textRelatedObjs['JumpToFileEnd'],accelerator="Control-9")
        self.add_separator()
        self.add_command(label = 'Delete Line', command = self.__textArea.textRelatedObjs['DeleteLine'],accelerator='Command-d')
        self.add_command(label = 'Delete To Line Start', command = self.__textArea.textRelatedObjs['DeleteToLineStart'],accelerator='Command-Left')
        self.add_command(label = 'Delete To Line End', command = self.__textArea.textRelatedObjs['DeleteToLineEnd'],accelerator='Command-Right')
        self.add_command(label = 'Delete Line Above', command = self.__textArea.textRelatedObjs['DeleteUpOneLine'],accelerator='Command-Up')
        self.add_command(label = 'Delete Line Below', command = self.__textArea.textRelatedObjs['DeleteDownOneLine'],accelerator='Command-Down')
        
    def __cascade(self):
        self.master.add_cascade(label = 'Edit', menu = self)
       
 class FormatMenu(tk.Menu):

    def __init__(self,masterMenu,textArea):
        tk.Menu.__init__(self,masterMenu)

        self.__textArea = textArea
        self.__root = textArea.master

        self.__commands()
        self.__cascade()

    def __commands(self):
        self.add_command(label = 'Indent Lines', command = self.__textArea.textRelatedObjs['IndentLines'],accelerator="Command-]")
        self.add_command(label = 'Dedent Lines', command = self.__textArea.textRelatedObjs['DedentLines'],accelerator="Command-[")
        self.add_separator()
        self.add_command(label = 'Comment Lines', command = self.__textArea.textRelatedObjs['CommentLines'],accelerator="Command-;")
        self.add_command(label = 'Ucomment Lines', command = self.__textArea.textRelatedObjs['UncommentLines'],accelerator="Command-'")
    def __cascade(self):
        self.master.add_cascade(label = 'Format', menu = self)


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
    

        
