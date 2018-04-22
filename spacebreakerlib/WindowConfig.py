#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Liangze Yu
"""

class WindowConfig:

    # default window width and height
    __winWidth = 584
    __winHeight = 406

    def __init__(self,root):
        self.__root = root
        self.__config()

    #prepare for future changes for window size defualt settings
    def __config(self,**kwargs):
        #widthXheight + x + y
        #screen sizes
        sWidth = self.__root.winfo_screenwidth()
        sHeight = self.__root.winfo_screenheight()
        #window sizes
        try:
            self.__winWidth = kwargs['width']
        except KeyError:
            pass
        try:
            self.__winHeight = kwargs['height']
        except KeyError:
            pass
        # pc left to win left
        left = int((sWidth / 2) - (self.__winWidth / 2))
        # pc top to win top
        top = int((sHeight / 2) - (self.__winHeight /2))
        self.__root.geometry(f'{self.__winWidth}x{self.__winHeight}+{left}+{top}')
    

