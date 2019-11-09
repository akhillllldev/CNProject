#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.17
# In conjunction with Tcl version 8.6
#    Nov 08, 2019 09:01:46 PM IST  platform: Windows NT
import subprocess
import sys

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

import about_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel(root)
    about_support.init(root, top)
    root.mainloop()


w = None


def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = New_Toplevel(w)
    about_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#5b9ed8'  # Closest X11 color: 'SteelBlue3'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d8955b'  # Closest X11 color: 'LightSalmon3'
        _ana1color = '#5b5fd8'  # Closest X11 color: 'SlateBlue3'
        _ana2color = '#5bd8d4'  # Closest X11 color: '{medium turquoise}'
        font11 = "-family {Product Sans} -size 14 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Product Sans} -size 12 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("834x744+358+118")
        top.title("New Toplevel")
        top.configure(background="#fff")

        self.Label1 = Label(top)
        self.Label1.place(relx=0.0, rely=-0.027, height=136, width=842)
        self.Label1.configure(background="#aaa0a9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''About''')
        self.Label1.configure(width=842)

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.036, rely=0.188,
                          relheight=0.773, relwidth=0.929)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d8d8d8")
        self.Frame1.configure(width=775)

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.258, rely=0.139, height=26, width=392)
        self.Label2.configure(background="#d8d8d8")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font11)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Made By Akhil Surendran''')
        self.Label2.configure(width=392)

        self.Label2_1 = Label(self.Frame1)
        self.Label2_1.place(relx=0.258, rely=0.296, height=26, width=392)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#d8d8d8")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font=font11)
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''Reg. No: 17BCE7087''')

        self.Label2_2 = Label(self.Frame1)
        self.Label2_2.place(relx=0.258, rely=0.435, height=26, width=392)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(background="#d8d8d8")
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(font=font11)
        self.Label2_2.configure(foreground="#000000")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text='''Guide: Dr. Nagaraju Devarakonda''')

        def home():
            root.destroy()
            subprocess.call('python akhil.py')

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.387, rely=0.887, height=42, width=201)
        self.Button1.configure(activebackground="#5bd8d4")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#fff")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font12)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#fff")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Home''')
        self.Button1.configure(width=201)
        self.Button1.configure(command=home)


if __name__ == '__main__':
    vp_start_gui()
