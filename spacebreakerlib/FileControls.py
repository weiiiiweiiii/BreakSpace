# -*- coding: utf-8 -*-
"""
@author: Liangze Yu
"""

import os
import tkinter as tk
import tkinter.filedialog as tf
from spacebreakerlib.RecentFiles import RecentFiles
from spacebreakerlib.MessageDialog import MessageDialog as md

class FileControls:

    def __init__(self,textArea):
        #text area
        self.__textArea = textArea
        #root window
        self.__root = textArea.master
        #prepare for files
        self.__textArea.textRelatedObjs['OpenedFile'] = None
        #store all functions
        self.__storeFunctions()
        #bind all short cuts
        self.__bindShortCuts()
        
        self.autosave()
        self._running = False
        
        # bind close window to self.__exit
        self.__root.protocol("WM_DELETE_WINDOW", self.__exit)

    def __storeFunctions(self):
        self.__textArea.textRelatedObjs['New'] = self.__newFile
        self.__textArea.textRelatedObjs['Open'] = self.__openFile
        self.__textArea.textRelatedObjs['Save'] = self.__saveFile
        self.__textArea.textRelatedObjs['Exit'] = self.__exit
        
        self.__textArea.textRelatedObjs['SaveAs'] = self.__saveAs
        self.__textArea.textRelatedObjs['OpenWithName'] = self.__openWithName

    def __bindShortCuts(self):
        #new file
        for key in ['<Command-n>','<Command-N>']:
            self.__root.bind(key,self.__textArea.textRelatedObjs['New'])
        #open file
        for key in ['<Command-o>','<Command-O>']:
            self.__root.bind(key,self.__textArea.textRelatedObjs['Open'])
        #save file
        for key in ['<Command-s>','<Command-S>']:
            self.__root.bind(key,self.__textArea.textRelatedObjs['Save'])
        #exit
        for key in ['<Command-w>','<Command-W>']:
            self.__root.bind(key,self.__textArea.textRelatedObjs['Exit'])
        
        #save as
        for key in ['<Command-Shift-s>']:
            self.__root.bind(key, self.__textArea.textRelatedObjs['SaveAs'])
            
    def __openWithName(self, event=None):
        self.__textArea.textRelatedObjs['OpenedFile'] = event
        self.__root.title(os.path.basename(self.__textArea.textRelatedObjs['OpenedFile']) + " - Space Breaker")
        #clean content
        self.__textArea.delete(1.0,tk.END)

        #open file
        file = open(self.__textArea.textRelatedObjs['OpenedFile'],"r")
        #insert content
        self.__textArea.insert(1.0,file.read())
        #finish insertion
        file.close()
        RecentFiles.addOpenedFile(self.__textArea.textRelatedObjs['OpenedFile'])
        self.__textArea.edit_modified(0)
        
        
        self.__textArea.edit_modified(0)
    
    def __newFile(self, event = None):
        #change title
        self.__root.title("Untitled - Space Breaker")
        #reset openedFile object
        self.__textArea.textRelatedObjs['OpenedFile'] = None
        #clean content
        self.__textArea.delete(1.0,tk.END)
        
        self.__textArea.edit_modified(0)
        

    def __openFile(self, event = None):
        #pop out dialog
        self.__textArea.textRelatedObjs['OpenedFile'] = tf.askopenfilename(defaultextension=".txt",
                                    filetypes=[("All Files","*.*"),
                                        ("Text Documents","*.txt"),("Python Files","*.py")])
        #open nothing
        if self.__textArea.textRelatedObjs['OpenedFile'] == "":
            #reset openedFile object
            self.__textArea.textRelatedObjs['OpenedFile'] = None
        else:
            self.__root.title(os.path.basename(self.__textArea.textRelatedObjs['OpenedFile']) + " - Space Breaker")
            #clean content
            self.__textArea.delete(1.0,tk.END)

            #open file
            file = open(self.__textArea.textRelatedObjs['OpenedFile'],"r")
            #insert content
            self.__textArea.insert(1.0,file.read())
            #finish insertion
            file.close()
            
            #add file name to recent
            RecentFiles.addOpenedFile(self.__textArea.textRelatedObjs['OpenedFile'])
            
            self.__textArea.edit_modified(0)
            
            
    def __saveFile(self, event = None):
        if self.__textArea.textRelatedObjs['OpenedFile'] == None:
            # Save as new file
            self.__textArea.textRelatedObjs['OpenedFile'] = tf.asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files","*.*"),
                                                ("Text Documents","*.txt")])
            #stop saving and reset openedFile object
            if self.__textArea.textRelatedObjs['OpenedFile'] == "":
                self.__textArea.textRelatedObjs['OpenedFile'] = None
            else:
                # open and write
                file = open(self.__textArea.textRelatedObjs['OpenedFile'],"w")
                file.write(self.__textArea.get(1.0,tk.END))
                file.close()
                # Change title
                self.__root.title(os.path.basename(self.__textArea.textRelatedObjs['OpenedFile']) + " - Space Breaker")
                self.__textArea.edit_modified(0)
                
                
        #opened file
        else:
            # file = open(self.__file,"w")
            file = open(self.__textArea.textRelatedObjs['OpenedFile'],"w")
            file.write(self.__textArea.get(1.0,tk.END))
            file.close()
            self.__textArea.edit_modified(0)

    def __saveAs(self, event = None):
        # Save as new file
        self.__textArea.textRelatedObjs['OpenedFile'] = tf.asksaveasfilename(initialfile='Untitled.txt',
                                        defaultextension=".txt",
                                        filetypes=[("All Files","*.*"),
                                            ("Text Documents","*.txt")])
        #stop saving and reset openedFile object
        if self.__textArea.textRelatedObjs['OpenedFile'] == "":
            self.__textArea.textRelatedObjs['OpenedFile'] = None
        else:
            # open and write
            file = open(self.__textArea.textRelatedObjs['OpenedFile'],"w")
            file.write(self.__textArea.get(1.0,tk.END))
            file.close()
            # Change title
            self.__root.title(os.path.basename(self.__textArea.textRelatedObjs['OpenedFile']) + " - Space Breaker")
            self.__textArea.edit_modified(0)
            
    
    def __exit(self, event = None):
        if self.__textArea.edit_modified() != 0:
            m = md(self.__root, "这是一条警告信息！请认真对待！", "你没保存啊！确定退出吗？？？", (0, "取消"), (1, "强行退出"), (2, "保存并退出"))
            self.__root.wait_window(m.topWindow)
            print("mdr:", md.response)
            result = m.getResponse()
            print("result is ",result)
            
            if result == -1:
                return
            elif result == 0:
                return
            elif result == 1:
                self.__root.destroy()
            elif result == 2:
                self.__saveAs()
        else:
            self.__root.destroy()
        
    def autosave(self):
        if self.__textArea.textRelatedObjs['OpenedFile'] not in [None, ""] and self._running:
            if self.__textArea.edit_modified() != 0:
                file = open(self.__textArea.textRelatedObjs['OpenedFile'],"w")
                file.write(self.__textArea.get(1.0,tk.END))
                file.close()
                print("AUTO_SAVED")
                self.__textArea.edit_modified(0)
        self.__textArea.master.after(10000, self.autosave)
    # do something you want

#         try:
#             while True:
#                 if self.__textArea.textRelatedObjs['OpenedFile'] not in [None, ""] and self._running:
#                     file = open(self.__textArea.textRelatedObjs['OpenedFile'],"w")
#                     file.write(self.__textArea.get(1.0,tk.END))
#                     file.close()
#                     print("AUTO_SAVED")
#                     self.__textArea.edit_modified(0)
#                 time.sleep(5)
#         except:
#             pass

        



        
