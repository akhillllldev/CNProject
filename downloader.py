#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.17
# In conjunction with Tcl version 8.6
#    Nov 08, 2019 10:01:55 PM IST  platform: Windows NT

import sys
import subprocess

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import downloader_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Downloader(root)
    downloader_support.init(root, top)
    root.mainloop()


w = None


def create_Downloader(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = Downloader(w)
    downloader_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Downloader():
    global w
    w.destroy()
    w = None


class Downloader:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#5b9ed8'  # Closest X11 color: 'SteelBlue3'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d8955b'  # Closest X11 color: 'LightSalmon3'
        _ana1color = '#5b5fd8'  # Closest X11 color: 'SlateBlue3'
        _ana2color = '#5bd8d4'  # Closest X11 color: '{medium turquoise}'
        font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font11 = "-family {Product Sans} -size 14 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Product Sans} -size 16 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font13 = "-family {Product Sans} -size 12 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("916x769+334+150")
        top.title("Downloader")
        top.configure(background="#fff")

        self.Label1 = Label(top)
        self.Label1.place(relx=0.0, rely=-0.013, height=156, width=922)
        self.Label1.configure(background="#00BCD4")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font12)
        self.Label1.configure(foreground="#fff")
        self.Label1.configure(text='''Downloader''')
        self.Label1.configure(width=922)

        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.284, rely=0.312, height=64, relwidth=0.627)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=574)

        self.Label2 = Label(top)
        self.Label2.place(relx=0.027, rely=0.338, height=35, width=109)
        self.Label2.configure(background="#fff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font11)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Enter URL''')

        self.Label2_1 = Label(top)
        self.Label2_1.place(relx=0.016, rely=0.533, height=35, width=189)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#fff")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font=font11)
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''Enter File Name''')
        self.Label2_1.configure(width=189)

        self.Entry1_2 = Entry(top)
        self.Entry1_2.place(relx=0.278, rely=0.514, height=64, relwidth=0.627)
        self.Entry1_2.configure(background="white")
        self.Entry1_2.configure(disabledforeground="#a3a3a3")
        self.Entry1_2.configure(font=font10)
        self.Entry1_2.configure(foreground="#000000")
        self.Entry1_2.configure(highlightbackground="#d9d9d9")
        self.Entry1_2.configure(highlightcolor="black")
        self.Entry1_2.configure(insertbackground="black")
        self.Entry1_2.configure(selectbackground="#c4c4c4")
        self.Entry1_2.configure(selectforeground="black")

        def download():
            a = self.Entry1.get()
            b = self.Entry1_2.get()
            subprocess.call(f"py -2 idm.py --name={b} {a} ")

        self.Button1 = Button(top)
        self.Button1.place(relx=0.731, rely=0.65, height=53, width=166)
        self.Button1.configure(activebackground="#5bd8d4")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#BDBDBD")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font13)
        self.Button1.configure(foreground="#fff")
        self.Button1.configure(highlightbackground="#5b9ed8")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Download''')
        self.Button1.configure(width=166)
        self.Button1.configure(command=download)

        def home():
            root.destroy()
            subprocess.call('python akhil.py')
        self.Button1_3 = Button(top)
        self.Button1_3.place(relx=0.862, rely=0.117, height=43, width=116)
        self.Button1_3.configure(activebackground="#5bd8d4")
        self.Button1_3.configure(activeforeground="#000000")
        self.Button1_3.configure(background="#B2EBF2")
        self.Button1_3.configure(disabledforeground="#a3a3a3")
        self.Button1_3.configure(font=font13)
        self.Button1_3.configure(foreground="#fff")
        self.Button1_3.configure(highlightbackground="#5b9ed8")
        self.Button1_3.configure(highlightcolor="black")
        self.Button1_3.configure(pady="0")
        self.Button1_3.configure(text='''Home''')
        self.Button1_3.configure(width=116)
        self.Button1_3.configure(command=home)


if __name__ == '__main__':
    vp_start_gui()
