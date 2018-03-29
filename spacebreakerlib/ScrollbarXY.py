#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Liangze Yu
"""

import tkinter as tk

class ScrollbarXY:

    def __init__(self,textArea):
        #pack with Window
        self.__root = textArea.master
        #function aligned to Text
        self.__textArea = textArea
        self.__xScrollbar()
        self.__yScrollbar()

    def __xScrollbar(self):
        self.__xBar = tk.Scrollbar(self.__root,command= self.__textArea.xview, orient = tk.HORIZONTAL)
        self.__textArea.config(xscrollcommand = self.__xBar.set)
        self.__xBar.pack(side = 'bottom', fill  = 'x')        

    def __yScrollbar(self):
        self.__yBar = tk.Scrollbar(self.__root,command= self.__textArea.yview, orient = tk.VERTICAL)
        self.__textArea.config(yscrollcommand = self.__yBar.set)
        self.__yBar.pack(side = 'right', fill  = 'y')
