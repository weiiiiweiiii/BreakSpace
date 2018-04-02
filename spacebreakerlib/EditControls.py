# -*- coding: utf-8 -*-
"""
@author: Liangze Yu
@author: BaiDa Yue
@author: Michael Wang
"""

import tkinter as tk
import tkinter.filedialog as tf

class EditControls:

    def __init__(self, textArea):
        self.__textArea = textArea
        self.__root = textArea.master

        self.__storeFunctions()
        self.__bindShortCuts()

    def __storeFunctions(self):
        self.__textArea.textRelatedObjs['Undo']    =  self.__undo
        self.__textArea.textRelatedObjs['Redo']    =  self.__redo
        self.__textArea.textRelatedObjs['Copy']    =  self.__copy
        self.__textArea.textRelatedObjs['Cut']     =  self.__cut
        self.__textArea.textRelatedObjs['Paste']   =  self.__paste
        self.__textArea.textRelatedObjs['SelectAll']=self.__selectAll

        self.__textArea.textRelatedObjs['Find'] = self.__find
        
##        self.__textArea.textRelatedObjs['StopSelectAll']=self.__stopSelectAll
        
        self.__textArea.textRelatedObjs['JumpToFileStart'] = self.__jumpToFileStart
        self.__textArea.textRelatedObjs['JumpToFileEnd'] = self.__jumpToFileEnd
        self.__textArea.textRelatedObjs['JumpToLineStart'] = self.__jumpToLineStart
        self.__textArea.textRelatedObjs['JumpToLineEnd'] = self.__jumpToLineEnd
        
        self.__textArea.textRelatedObjs['DeleteLine'] = self.__deleteLine
        self.__textArea.textRelatedObjs['DeleteToLineStart'] = self.__deleteToLineStart
        self.__textArea.textRelatedObjs['DeleteToLineEnd'] = self.__deleteToLineEnd
        self.__textArea.textRelatedObjs['DeleteUpOneLine'] = self.__deleteUpOneLine
        self.__textArea.textRelatedObjs['DeleteDownOneLine'] = self.__deleteDownOneLine

    def __bindShortCuts(self):
        for key in ["<Command-z>","<Command-Z>"]:
            self.__root.bind(key, self.__undo)
        for key in ["<Command-Shift-z>","<Command-Shift-Z>"]:
            self.__root.bind(key, self.__redo)
        for key in ["<Command-a>","<Command-A>"]:
            self.__root.bind(key, self.__selectAll)
            
##        for key in ["<Button-1>","<Return>"]:
##            self.__root.bind(key, self.__stopSelectAll)
            
        self.__root.bind('<Control-0>',self.__textArea.textRelatedObjs['JumpToFileStart'])
        self.__root.bind('<Control-9>',self.__textArea.textRelatedObjs['JumpToFileEnd'])
        self.__root.bind('<Control-,>',self.__textArea.textRelatedObjs['JumpToLineStart'])
        self.__root.bind('<Control-.>',self.__textArea.textRelatedObjs['JumpToLineEnd'])

        for key in ['<Command-f>', "<Command-F>"]:
            self.__root.bind(key, self.__textArea.textRelatedObjs['Find'])
        
        for key in ['<Command-d>','<Command-D>']:
            self.__root.bind(key, self.__textArea.textRelatedObjs['DeleteLine'])
        self.__root.bind('<Command-Left>', self.__textArea.textRelatedObjs['DeleteToLineStart'])
        self.__root.bind('<Command-Right>', self.__textArea.textRelatedObjs['DeleteToLineEnd'])
        self.__root.bind('<Command-Up>', self.__textArea.textRelatedObjs['DeleteUpOneLine'])
        self.__root.bind('<Command-Down>', self.__textArea.textRelatedObjs['DeleteDownOneLine'])

    def __undo(self, event=None):
        self.__textArea.event_generate("<<Undo>>")
        return 'break'

    def __redo(self, event=None):
        self.__textArea.event_generate("<<Redo>>")
        return 'break'

    def __copy(self,event = None):
        self.__textArea.event_generate('<<Copy>>')
        return 'break'
    
    def __cut(self, event = None):
        self.__textArea.event_generate('<<Cut>>')
        return 'break'

    def __paste(self, event = None):
        self.__textArea.event_generate('<<Paste>>')
        return 'break'
    
    def __selectAll(self,event = None):
        self.__textArea.tag_add('sel', '1.0', tk.END)
        self.__textArea.mark_set(tk.INSERT, '1.0')
        self.__textArea.see(tk.INSERT)
        return 'break'

##    def __stopSelectAll(self, event = None):
##        try:
##            last = self.__textArea.index('sel.last')
##            print(2)
##            self.__textArea.mark_set(tk.INSERT, last)
##            self.__textArea.see(tk.INSERT)
##        except tk.TclError:
##            print(1)
##            return 'break'
##        finally:
##            self.__textArea.tag_remove('sel', '1.0', tk.END)
        

    def __jumpToFileStart(self, event = None):
        self.__textArea.mark_set(tk.INSERT, '1.0')
        self.__textArea.see(tk.INSERT)
        return 'break'

    def __jumpToFileEnd(self, event = None):
        self.__textArea.mark_set(tk.INSERT, tk.END)
        self.__textArea.see(tk.INSERT)
        return 'break'
    
    def __jumpToLineStart(self, event=None):
        head, tail = self.__getRegion()
        self.__textArea.tag_remove("sel", 1.0, tk.END)
        self.__textArea.mark_set(tk.INSERT,head)
        self.__textArea.see(tk.INSERT)
        return 'break'

    def __jumpToLineEnd(self, event=None):
        head, tail = self.__getRegion()
        self.__textArea.tag_remove("sel", 1.0, tk.END)
        self.__textArea.mark_set(tk.INSERT,tail)
        self.__textArea.see(tk.INSERT)
        return 'break'

    def __deleteLine(self, event=None):
        head = self.__textArea.index("insert linestart")
        #+1c to remove the linefeed
        tail = self.__textArea.index("insert lineend +1c")
        self.__textArea.tag_remove("sel", 1.0, tk.END)
        self.__textArea.delete(head,tail)
        return 'break'

    def __deleteToLineStart(self, event = None):
        head = self.__textArea.index('insert linestart')
        tail = self.__textArea.index('insert +1c')
        self.__textArea.tag_remove("sel", 1.0, tk.END)
        self.__textArea.delete(head,tail)
        return 'break'

    def __deleteToLineEnd(self, event = None):
        head = self.__textArea.index('insert -1c')
        tail = self.__textArea.index('insert lineend')
        self.__textArea.tag_remove("sel", 1.0, tk.END)
        self.__textArea.delete(head,tail)
        return 'break'

    def __deleteUpOneLine(self, event=None):
        #command up will shit down first
        self.__deleteLine(event)
        return 'break'

    def __deleteDownOneLine(self,event = None):
        #command down will shift down first
        self.__deleteLine(event)
        return 'break'

    #come from Format Controls
    def __getIndex(self):
        #if no lines are selected
        #we give it to none so we can process further
        try:
            begin = self.__textArea.index('sel.first')
            end = self.__textArea.index('sel.last')
            return begin,end
        except tk.TclError:
            return None,None

    #modified to suite Edit Controls
    def __getRegion(self):
        begin, end = self.__getIndex()
        #if select region
        #to get the whole lines of the region
        if begin and end:
            head = self.__textArea.index(begin + " linestart")
            tail = self.__textArea.index(end + "-1c lineend")
        #if no selection
        #get the whole lines of selection
        else:
            #give out the current line of cursor line start
            head = self.__textArea.index("insert linestart")
            #give out the current line of cursor line ned
            tail = self.__textArea.index("insert lineend")
        return head, tail

    def _search_(self, word):
        if word:
            countvar = tk.StringVar()
            f = self.__textArea.search(word, "1.0", count=countvar)
            starting_index = f
            ending_index = "{}+{}c".format(starting_index, countvar.get())
            self.__textArea.tag_add("search", starting_index, ending_index)
            self.__textArea.tag_configure("search", background="skyblue", foreground="red")
            return True
        else:
            return None

    def __find(self, event = None):
        t = FindAsk(self.__root, "Find")
        if t['submit']:
            self._search_(t['Find'])
        return


def FindAsk(parent, *args):
    root = tk.Toplevel(parent)
    root.title("Find And Replace")
    root.transient(parent)
    root.focus_force()
    root.resizable(width=0, height=0)
    root['padx'] = 20
    fields = {}
    field = {}
    for r, label in enumerate(args):
        store_label = tk.Label(root, text=label)
        store_label.grid(row=r, column=0, ipady=5, ipadx=20)
        store_entry = tk.Entry(root)
        store_entry.grid(row=r, column=1)
        field[label] = store_entry
    fields['submit'] = False

    def sub():
        for l, t in field.items():
            fields[l] = t.get()
        fields['submit'] = True
        root.destroy()
        return

    submit = tk.Button(root, text="Ok", command=sub)
    submit.grid(row=r + 1, column=2)
    root.wait_window()
    return fields




