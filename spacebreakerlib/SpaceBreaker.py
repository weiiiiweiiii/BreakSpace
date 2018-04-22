#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Liangze Yu
"""

import tkinter as tk

from spacebreakerlib import WindowConfig as wc
from spacebreakerlib import TextArea as ta



class SpaceBreaker(tk.Tk):
    
    def __init__(self, file_name = None):
        tk.Tk.__init__(self)
        
        #get title
        self.title("Untitled - Space Breaker")
        
        #window set up
        wc.WindowConfig(self)
        
        #Text Area
        #   -Scrollarbars
        #   -File handler
        #   -Menu Bar
        self.__textArea = ta.TextArea(self)
        
        if file_name!=None:
            self.__textArea.textRelatedObjs['OpenWithName'](file_name)


    def run(self):
        self.mainloop()

        

        
        
            

