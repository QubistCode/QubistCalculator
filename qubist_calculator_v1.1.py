from tkinter import *

mainwin = Tk()
mainwin.title('Welcome Screen - QubistCalculator')
mainwin.geometry('300x300')
welcomelabel = Label(mainwin, text = 'Qubist brings you a calculator! /n Enjoy productivity with personalization and design.')
welcomelabel.pack()
mainwin.mainloop

def winadd():
    global win1
    global atxt1
    global atxt2
    win1 = Toplevel()
    win1.title("QubistCalculator - Addition")
    win1.geometry('400x300')
    menubar_add = Menu(win1)
    atxt1 = Entry(win1)
    atxt1.grid(column=0, row=0)
    atxt2 = Entry(win1)
    atxt2.grid(column=0, row=2)
    addno1 = Button(win1, text='Click to submit 1st number', command=aclicked1)
    addno1.grid(column=1, row=0)
    addno2 = Button(win1, text='Click to submit 2nd number', command=aclicked2)
    addno2.grid(column=1, row=2)
    a_submit = Button(win1, text='Submit', command=a_result)
    a_submit.grid(column=1, row=4)
    file_add = Menu(menubar_add, tearoff = 0)
    menubar_add.add_cascade(label = 'File', menu=file_add)
    file_add.add_command(label = 'Save equation')
    win1.config(menu = menubar_add)
    win1.mainloop()

def winsub():
    global stxt1
    global stxt2
    global win2
    win2 = Toplevel()
    win2.title("QubistCalculator - Subtraction")
    win2.geometry('400x300')
    stxt1 = Entry(win2)
    stxt1.grid(column=0, row=0)
    stxt2 = Entry(win2)
    stxt2.grid(column=0, row=2)
    subno1 = Button(win2, text='Click to submit 1st number', command=sclicked1)
    subno1.grid(column=1, row=0)
    subno2 = Button(win2, text='Click to submit 2nd number', command=sclicked2)
    subno2.grid(column=1, row=2)
    s_submit = Button(win2, text='Calculate', command=s_result)
    s_submit.grid(column=1, row=4)
    root.mainloop()

def winmulti():
    global mtxt1
    global mtxt2
    global win3
    win3 = Toplevel()
    win3.title("QubistCalculator - Multiplication")
    win3.geometry('400x300')
    mtxt1 = Entry(win3)
    mtxt1.grid(column=0, row=0)
    mtxt2 = Entry(win3)
    mtxt2.grid(column=0, row=2)
    multino1 = Button(win3, text='Click to submit 1st number', command=mclicked1)
    multino1.grid(column=2, row=0)
    multino2 = Button(win3, text='Click to submit 2nd number', command=mclicked2)
    multino2.grid(column=2, row=2)
    m_submit = Button(win3, text='Calculate', command=m_result)
    m_submit.grid(column=0, row=4)
    root.mainloop()

def windiv():
    global dtxt1
    global dtxt2
    global win4
    win4 = Toplevel()
    win4.title("QubistCalculator - Division")
    win4.geometry('400x300')
    dtxt1 = Entry(win4)
    dtxt1.grid(column=0, row=0)
    dtxt2 = Entry(win4)
    dtxt2.grid(column=0, row=2)
    divno1 = Button(win4, text='Click to submit 1st number', command=dclicked1)
    divno1.grid(column=2, row=0)
    divno2 = Button(win4, text='Click to submit 2nd number', command=dclicked2)
    divno2.grid(column=2, row=2)
    d_submit = Button(win4, text='Calculate', command=d_result)
    d_submit.grid(column=0, row=4)
    root.mainloop()

def aboutwin():
    win5 = Toplevel()
    win5.title('About - QubistCalculator')
    win5.geometry('400x300')
    aboutlabel = Label(win5, text=['Made by Advaith Sai \n Qubist Productions, brings to you a calculator. \n Made with Python 3.7, extends to v3.9 \n For queries and complaints, email villequantum@gmail.com \n For developers, contact me on GitHub \n The name GitHub and affilated logos are property of GitHub Inc.'])                
    aboutlabel.pack()
    root.mainloop()

#definitions for saving the numbers to a variable

def sclicked1():
    global no1
    no1 = stxt1.get()
    print(no1)
        
def sclicked2():
    global no2
    no2 = stxt2.get()

    print(no2)

def aclicked1():
    global no1
    no1 = atxt1.get()
    print(no1)
        
def aclicked2():
    global no2
    no2 = atxt2.get()
    print(no2)

def mclicked1():
    global no1
    no1 = mtxt1.get()
    print(no1)
        
def mclicked2():
    global no2
    no2 = mtxt2.get()
    print(no2)

def dclicked1():
    global no1
    no1 = dtxt1.get()
    print(no1)

def dclicked2():
    global no2
    no2 = dtxt2.get()
    print(no2)

#definitions for calculation
def a_result():
    global aans
    global aans1
    aans = float(no1) + float(no2)
    aans1 = no1, '+', no2, '=', aans
    alabel = Label(win1, text = aans1)
    alabel.grid(column=0, row=4)
    
    
def s_result():
    global sans
    global sans1
    sans = float(no1) - float(no2)
    sans1 = no1,'-', no2, '=', sans
    slabel = Label(win2, text=sans1)
    slabel.grid(column=0, row=4)

def m_result():
    global mans
    global mans1
    mans = float(no1) * float(no2)
    mans1 = no1, 'x', no2, '=', mans
    mlabel = Label(win3, text=mans1)
    mlabel.grid(column=0, row=4)
    

def d_result():
    global dans
    dans = float(no1) / float(no2)
    print(dans)

def changelog_v1():
    win_v1 = Toplevel()
    win_v1.title('QubistCalculator - Changelog v1')
    win_v1.geometry('500x500')
    
    labelframe_v1 = LabelFrame(win_v1, text = 'version 1.0') 
    labelframe_v1.pack(expand = 'yes', fill = 'both') 
    label1 = Label(labelframe_v1, text = '+ A basic tkinter module calculator with arithmetic functionality.') 
    label1.place(x = 0, y = 10) 
    label2 = Label(labelframe_v1, text = '+ Menubar shortcuts and coloured GUI profile.') 
    label2.place(x = 0, y = 30) 
    label3 = Label(labelframe_v1, text = '+ About page with extra info') 
    label3.place(x = 0, y = 50)

    labelframe_v1_1 = LabelFrame(win_v1, text = 'version 1.1')
    labelframe_v1_1.pack(expand = 'true', fill = 'both')
    label1 = Label(labelframe_v1_1, text = '')
    label1.place(x = 0, y = 5)
    win_v1.mainloop()
    


def colorwindo():
    global root
    root = Toplevel()  
    root.title("QubistCalculator") 
    root.geometry('500x500')
    menubar = Menu(root)

    #add
    btn = Button(root, text = 'Addition' , bg='blue', fg='white', command=winadd)
    btn.pack(side = TOP, expand = True, fill = BOTH)
    #subtract
    btn2 = Button(root, text = 'Subtraction',bg='green', fg='white', command=winsub)
    btn2.pack(side = TOP, expand = True, fill = BOTH)
    #multiplication
    btn3 = Button(root, text = 'Multiplication',bg='red', fg='white', command=winmulti)
    btn3.pack(side = TOP, expand = True, fill = BOTH)
    #division
    btn4 = Button(root, text = 'Division', bg='black', fg='white', command=windiv)
    btn4.pack(side = TOP, expand = True, fill = BOTH)
    #about
    btn5 = Button(root, text = 'About', bg='white', fg='black', command=aboutwin)
    btn5.pack(side = TOP, expand = True, fill = BOTH)

    #menubar.....im god
    file = Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='File', menu = file) 
    file.add_command(label ='Addition', command = winadd) 
    file.add_command(label ='Subtraction', command = winsub) 
    file.add_command(label ='Multiplication', command = winmulti)
    file.add_command(label ='Division', command = windiv) 
    # menubar - edit bar
    edit = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = 'Edit', menu = edit)
    edit.add_command(label = 'Coming soon')
    # changelog menubar
    log = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = 'Changelog', menu = log)
    log.add_command(label = 'v1', command=changelog_v1)
    log.add_separator()
    log.add_command(label = 'Full update log')
    #color profiles menubar
    color = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = 'Colors', menu = color)
    color.add_command(label= 'Colorful')
    color.add_command(label='Grayscale', command = graywindo)

    # exit app menubar
    ex = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = 'Exit', menu = ex)
    ex.add_command(label = 'Exit App', command=mainwin.destroy)


    root.config(menu = menubar) 
    root.mainloop()



def graywindo():
    global graywin
    graywin = Toplevel()
    graywin.title("QubistCalculator")
    graywin.geometry('500x500')
    menubar1 = Menu(graywin)

    #add
    btn = Button(graywin, text = 'Addition' , bg='gray', fg='black', command=winadd)
    btn.pack(side = TOP, expand = True, fill = BOTH)
    #subtract
    btn2 = Button(graywin, text = 'Subtraction',bg='gray', fg='black', command=winsub)
    btn2.pack(side = TOP, expand = True, fill = BOTH)
    #multiplication
    btn3 = Button(graywin, text = 'Multiplication',bg='gray', fg='black', command=winmulti)
    btn3.pack(side = TOP, expand = True, fill = BOTH)
    #division
    btn4 = Button(graywin, text = 'Division', bg='gray', fg='black', command=windiv)
    btn4.pack(side = TOP, expand = True, fill = BOTH)
    #about
    btn5 = Button(graywin, text = 'About', bg='gray', fg='black', command=aboutwin)
    btn5.pack(side = TOP, expand = True, fill = BOTH)


    #menubar
    file = Menu(menubar1, tearoff = 0) 
    menubar1.add_cascade(label ='File', menu = file) 
    file.add_command(label ='Addition', command = winadd) 
    file.add_command(label ='Subtraction', command = winsub) 
    file.add_command(label ='Multiplication', command = winmulti)
    file.add_command(label ='Division', command = windiv) 
    # menubar - edit bar
    edit = Menu(menubar1, tearoff = 0)
    menubar1.add_cascade(label = 'Edit', menu = edit)
    edit.add_command(label = 'Coming soon')
    # changelog menubar
    log = Menu(menubar1, tearoff = 0)
    menubar1.add_cascade(label = 'Changelog', menu = log)
    log.add_command(label = 'v1', command=changelog_v1)
    log.add_separator()
    log.add_command(label = 'Full update log')
    #color profiles menubar
    color = Menu(menubar1, tearoff = 0)
    menubar1.add_cascade(label = 'Colors', menu = color)
    color.add_command(label= 'Colorful', command=colorwindo)

    # exit app menubar
    ex = Menu(menubar1, tearoff = 0)
    menubar1.add_cascade(label = 'Exit', menu = ex)
    ex.add_command(label = 'Exit App', command=mainwin.destroy)
    graywin.config(menu = menubar1)
    graywin.mainloop()
    
colorwindo()
