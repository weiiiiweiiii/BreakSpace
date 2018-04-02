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
    
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)
        
        self.__bindEverything()

        self.__pack()

    def __bindEverything(self):
        f.FontControls(self.master, self)
        tb.TextBind(self)

    def __pack(self):
        self.pack(expand = True, fill = 'both')
        
    def _proxy(self, *args):
        # let the actual widget perform the requested action
        cmd = (self._orig,) + args
        result = self.tk.call(cmd)

        # generate an event if something was added or deleted,
        # or the cursor position changed
        if (args[0] in ("insert", "replace", "delete") or
            args[0:3] == ("mark", "set", "insert") or
            args[0:2] == ("xview", "moveto") or
            args[0:2] == ("xview", "scroll") or
            args[0:2] == ("yview", "moveto") or
            args[0:2] == ("yview", "scroll")
        ):
            self.event_generate("<<Change>>", when="tail")

        # return what the actual widget returned
        return result 
        
        

