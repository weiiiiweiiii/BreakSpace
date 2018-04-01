#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Liangze Yu
"""

import tkinter as tk

from spacebreakerlib import TextBind as tb
from spacebreakerlib import FontControls as f

class TextArea(tk.Text):

    #stored objects like functions and files
    # textRelatedObjs = {}
    
    def __init__(self,root):
        tk.Text.__init__(self,root, wrap = tk.NONE, undo = True)
        self.textRelatedObjs = {}
        
        self.__bindEverything()

        self.__pack()

    def __bindEverything(self):
        f.FontControls(self.master, self)
        tb.TextBind(self)

    def __pack(self):
        self.pack(expand = True, fill = 'both')
        
        

