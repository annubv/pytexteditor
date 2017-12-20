from tkinter import *
import tkinter as tk
import tkinter.scrolledtext as tkst  # because only tkinter doesn't give scrollable text

root = tk.Tk()
pad = tkst.ScrolledText(root, width=100, height=80)  # this is the text area where we write the document

#All the menu's commands
def openc():
    file=filedialog.askopenfile(parent=root, mode='rb',title='Select a text file', filetypes = (("text files","*.txt"),("all files","*.*")))
    if file:
        pad.delete('1.0', END)
        elem=file.read()
        pad.insert('1.0',elem) #in 1.0 , 1 denotes first line and 0 denotes first column of the document

def saveasc():
    file1=filedialog.asksaveasfile(mode='w',defaultextension=".txt", filetypes = (("text files","*.txt"),("all files","*.*")))
    if file1:
        elem=pad.get('1.0', END+'-1c') #deleted last character b/c there's an extra return
        file1.write(elem)
        file1.close()

def exitc():
    if messagebox.askokcancel("Quit", "Are you sure?"):
        root.destroy()

def aboutc():
    label=messagebox.showinfo("About","PytextEditor \n Version 1 \n Developed by Anubhav Singh")

# to create toplevel menu
menubar = Menu(root)
filemenu = Menu(menubar)  # created pulldown menu 'filemenu' and added to menubar
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=openc)
filemenu.add_command(label="Save As", command=saveasc)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exitc)
menubar.add_command(label="About", command=aboutc)
root.config(menu=menubar) #to display menubar

pad.pack()
root.mainloop()
