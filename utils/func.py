from tkinter import *
from tkinter import filedialog
import os
import sys


def browseFiles():
    filepath = filedialog.askopenfilename(initialdir = os.getcwd()+"/assets/", title = "Select a File to perform compression",filetypes = (("all files", "*.*"), ("all files","*.*")))
    if filepath=="":
        sys.exit("\nNo file selected from opened pop up window")
    filename = os.path.basename(filepath).split("/")[-1]
    xt = filename.split(".")
    for i in xt:
      if i in ['gz','tar']:
         ext = "."+filename.split(".")[1]
      elif i in ['pdf','txt','docx','csv','tsv','xls']:
         ext = "."+filename.split(".")[-1]
      else:
       ext = "."+filename.split(".")[-1]

    print("\nChoosen Input File Path : " + filepath)
    print("\t--> Choosen Input File Name : " + filename)
    print("\t--> Original File Format : "+ ext,end="\n\n")
    return filepath,filename,ext
window = Tk()
button_explore = Button(window,text = "Browse Files", command = browseFiles)
window.withdraw()    