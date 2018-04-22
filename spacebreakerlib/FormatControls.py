# -*- coding: utf-8 -*-
"""
@author: Liangze Yu
"""

import tkinter as tk

class FormatControls:

    __tabWidth = 8
    #we can customize it for indent using tab or not
    __usetabs = True

    def __init__(self,textArea):
        self.__textArea = textArea
        self.__root = textArea.master

        #can be customized
        self.__textArea.textRelatedObjs['Language']  = 'c++'
        self.__textArea.textRelatedObjs['Language']  = 'python'
        self.__language = self.__textArea.textRelatedObjs['Language']

        self.__storeFunctions()
        self.__bindShortCuts()

    def __storeFunctions(self):
        self.__textArea.textRelatedObjs['IndentLines'] = self.__indentLines
        self.__textArea.textRelatedObjs['DedentLines'] = self.__dedentLines
        self.__textArea.textRelatedObjs['CommentLines'] = self.__commentLines
        self.__textArea.textRelatedObjs['UncommentLines'] = self.__uncommentLines

    def __bindShortCuts(self):
        self.__root.bind('<Command-]>',self.__textArea.textRelatedObjs['IndentLines'])
        self.__root.bind('<Command-[>',self.__textArea.textRelatedObjs['DedentLines'])
        self.__root.bind('<Command-;>',self.__textArea.textRelatedObjs['CommentLines'])
        self.__root.bind('<Command-\'>',self.__textArea.textRelatedObjs['UncommentLines'])

    def __indentLines(self, event = None):
        head, tail, chars, lines = self.__getRegion()
        for pos in range(len(lines)):
            line = lines[pos]
            if line:
                rawChars, effectiveChars = self.__detectWhiteSpace(line)
                effectiveChars = effectiveChars + self.__tabWidth
                lines[pos] = self.__makeIndent(effectiveChars) + line[rawChars:]
        self.__setRegion(head, tail, chars, lines)
        return 'break'

    def __dedentLines(self, event = None):
        head, tail, chars, lines = self.__getRegion()
        for pos in range(len(lines)):
            line = lines[pos]
            if line:
                rawChars, effectiveChars = self.__detectWhiteSpace(line)
                effectiveChars = max(effectiveChars - self.__tabWidth, 0)
                lines[pos] = self.__makeIndent(effectiveChars) + line[rawChars:]
        self.__setRegion(head, tail, chars, lines)
        return 'break'

    def __commentLines(self, event = None):
        head, tail, chars, lines = self.__getRegion()
        for pos in range(len(lines)):
            line = lines[pos]
            if self.__language == 'c++':
                lines[pos] = '//' + line
            elif self.__language == 'python':
                lines[pos] = '##' + line
        self.__setRegion(head, tail, chars, lines)

    def __uncommentLines(self, event = None):
        head, tail, chars, lines = self.__getRegion()
        for pos in range(len(lines)):
            line = lines[pos]
            if not line:
                continue
            if self.__language == 'c++':
                if line[:2] == '//':
                    line = line[2:]
            elif self.__language == 'python':
                if line[:2] == '##':
                    line = line[2:]
                elif line[:1] == '#':
                    line = line[1:]
            lines[pos] = line
        self.__setRegion(head, tail, chars, lines)

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
        #read out all the text
        chars = self.__textArea.get(head, tail)
        #split all lines into a list
        lines = chars.split("\n")
        return head, tail, chars, lines

    def __setRegion(self, head, tail, chars, lines):
        newchars = "\n".join(lines)
        #stop selection in order to processing
        self.__textArea.tag_remove("sel", 1.0, tk.END)
        self.__textArea.delete(head, tail)
        self.__textArea.insert(head, newchars)
        #select it again to do another performance about indent
        #tag 'sel' represents the selection from head to
        #insert cursor's current position
        self.__textArea.tag_add("sel", head, tk.INSERT)

    def __getIndex(self):
        #if no lines are selected
        #we give it to none so we can process further
        try:
            begin = self.__textArea.index('sel.first')
            end = self.__textArea.index('sel.last')
            return begin,end
        except tk.TclError:
            return None,None

    def __makeIndent(self, effectiveChars):
        #consider tabs or space only
        if self.__usetabs:
            ntabs, nspaces = divmod(effectiveChars, self.__tabWidth)
            return '\t' * ntabs + ' ' * nspaces
        else:
            return ' ' * n

    def __detectWhiteSpace(self,line):
        rawChars = effectiveChars = 0
        for ws in line:
            if ws == ' ':
                rawChars += 1
                effectiveChars += 1
            elif ws == '\t':
                rawChars +=  1
                effectiveChars = (effectiveChars // self.__tabWidth + 1) * self.__tabWidth
            else:
                break
        return rawChars, effectiveChars
