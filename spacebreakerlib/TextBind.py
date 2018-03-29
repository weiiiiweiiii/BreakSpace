#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Liangze Yu
"""

from spacebreakerlib import ScrollbarXY as bars
from spacebreakerlib import FileControls as fc
from spacebreakerlib import MenuBar as mb

class TextBind:

    def __init__(self,textArea):
        self.__textArea = textArea

        #bind logic
        self.__functionConnections()
        #bind body
        self.__partConnections()

    def __functionConnections(self):
        fc.FileControls(self.__textArea)

    def __partConnections(self):
        bars.ScrollbarXY(self.__textArea)
        mb.MenuBar(self.__textArea)
        
