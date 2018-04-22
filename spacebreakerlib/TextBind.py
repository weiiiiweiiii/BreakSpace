#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Liangze Yu
"""

from spacebreakerlib import ScrollbarXY as bars
from spacebreakerlib import FileControls as flc
from spacebreakerlib import EditControls as edc
from spacebreakerlib import FormatControls as fmc
from spacebreakerlib import MenuBar as mb
from spacebreakerlib import LineNumber as ln

class TextBind:

    def __init__(self,textArea):
        self.__textArea = textArea

        #bind logic
        self.__functionConnections()
        #bind body
        self.__partConnections()

    def __functionConnections(self):
        flc.FileControls(self.__textArea)
        edc.EditControls(self.__textArea)
        fmc.FormatControls(self.__textArea)

    def __partConnections(self):
        bars.ScrollbarXY(self.__textArea)
        ln.LineNumber(self.__textArea)
        mb.MenuBar(self.__textArea)
        
