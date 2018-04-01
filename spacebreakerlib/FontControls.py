import tkinter as tk
from tkinter.font import Font as tkinterFont

class FontControls:
    def __init__(self, root, textArea):
        self._root = root
        self.__textArea = textArea
        self.__initialize_tags__()
        self.__add_to_dict()
        self.__bindShortCuts()
    
    def __add_to_dict(self):
        self.__textArea.textRelatedObjs['font_bold'] = self._font_bold
        self.__textArea.textRelatedObjs['font_italic'] = self._font_italic
        self.__textArea.textRelatedObjs['font_underline'] = self._font_underline
        
    def __bindShortCuts(self):
        #bold
        for key in ['<Command-b>','<Command-B>']:
            self._root.bind(key,self.__textArea.textRelatedObjs['font_bold'])
        #italic
        for key in ['<Command-i>','<Command-I>']:
            self._root.bind(key,self.__textArea.textRelatedObjs['font_italic'])
        #underline
        for key in ['<Command-u>','<Command-U>']:
            self._root.bind(key,self.__textArea.textRelatedObjs['font_underline'])
            
    def __initialize_tags__(self):
        self.__textArea.tag_configure("BOLD", font = tkinterFont(family="Arial", size=14, weight="bold"))
        self.__textArea.tag_configure("ITALIC", font= tkinterFont(family = "Helvetica", size=14, slant="italic"))
        self.__textArea.tag_configure("UNDERLINE", font=tkinterFont(family="Courrier"), underline=1)
        
#         #combination tags
#         self.__textArea.tag_configure("BOLD_ITALIC", font = tkinterFont(family="Arial", size=14, weight="bold", slant="italic"))
#         self.__textArea.tag_configure("BOLD_UNDERLINE", font = tkinterFont(family="Arial", size=14, weight="bold"), underline=1)
#         self.__textArea.tag_configure("ITALIC_UNDERLINE", font= tkinterFont(family = "Helvetica", size=14, slant="italic"), underline=1)
#         self.__textArea.tag_configure("BOLD_ITALIC_UNDERLINE", font = tkinterFont(family="Arial", size=14, weight="bold", slant="italic"), underline=1)
        
    def _font_bold(self, event=None):
        try:
            print(self.__textArea.tag_names("sel.first"))
            if 'BOLD' not in self.__textArea.tag_names("sel.first"):
                self.__textArea.tag_add("BOLD", "sel.first", "sel.last")
            else:
                self.__textArea.tag_remove("BOLD", "sel.first", "sel.last")
        except tk.TclError:
            pass
        
    def _font_italic(self, event=None):
        try:
            print(self.__textArea.tag_names("sel.first"))
            if 'ITALIC' not in self.__textArea.tag_names("sel.first"):
                self.__textArea.tag_add("ITALIC", "sel.first", "sel.last")  
            else:
                self.__textArea.tag_remove("ITALIC", "sel.first", "sel.last")   
        except tk.TclError:
            pass
        
    def _font_underline(self, event=None):
        try:
            print(self.__textArea.tag_names("sel.first"))
            if 'UNDERLINE' not in self.__textArea.tag_names("sel.first"):
                self.__textArea.tag_add("UNDERLINE", "sel.first", "sel.last")  
            else:
                self.__textArea.tag_remove("UNDERLINE", "sel.first", "sel.last")   
        except tk.TclError:
            pass
    
    
    def clear(self):
        self.__textArea.tag_remove("BOLD",  "1.0", 'end')
        self.__textArea.tag_remove("UNDERLINE",  "1.0", 'end')
        self.__textArea.tag_remove("ITALIC",  "1.0", 'end')
    