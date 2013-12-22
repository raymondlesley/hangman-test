'''
Created on 20 Dec 2013

@author: L14202
'''

from tkinter import Tk, Frame

class Window(Frame):
    '''
    classdocs
    '''

    def __init__(self, name="", width=100, height=100, master=None):
        Frame.__init__(self, width=width, height=height, master=master)
        '''
        Constructor
        '''
        self._name = name

    def open(self):
        self.grid()
        self.master.title(self._name)
        self.mainloop()
