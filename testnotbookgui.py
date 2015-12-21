import Tkinter
from tkMessageBox import askyesno
import tkMessageBox
from passwdstrA import PasswordEncrption 
import ttk
from Tkinter import Frame, Label, Tk
from ttk import Button
import os
import pickle
import sys
import collections
from DBConnectionTest import SubmitPSW
from cStringIO import StringIO
from Tkinter import *
import bz2
import base64
import logging
from ConfigParser import SafeConfigParser
import time
from time import gmtime
import shutil
import datetime
from ExpiresOn import Expires
import logging


'''
Created on Aug 18, 2015

@author: Ryan Ruscett

This program is used to store passwords. 
'''

class DialogWidget(Tkinter.Tk):
    
    '''
# assuming loglevel is bound to the string value obtained from the
# command line argument. Convert to upper case to allow the user to
# specify --log=DEBUG or --log=debug
    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)
    logging.basicConfig(level=numeric_level, ...)
    '''   
    
    def __init__(self,parent, UnamePword):
        
        ''' This is the initialization of the pop up gui. When you click on an account from tab 2. You are given a pop up text box with information pertaning to the account.
        This class sets up that texbox to be displayed.'''
        
        Tkinter.Tk.__init__(self,parent) 
        self._uspwd = UnamePword
        Tkinter.Tk.geometry(self, "400x300+400+700")
        Tkinter.Tk.iconbitmap(self,'jack.ico')
        self.parent = parent 
        self.initialize()  
          
    def initialize(self):
        self.grid()
        self.MSGtext = Tkinter.Text(self, font=('helvetica', 12, 'bold italic'))
        self.MSGtext.grid(column=1,row=5,columnspan=4,sticky='EW')
        self.MSGtext.insert(1.0, self._uspwd)
        
        self.labelVariabletk = Tkinter.StringVar()
        self.labeltk = Tkinter.Label(self, text = "Use Control - C To Copy the Username and Password",
                                          anchor="w",fg="white",bg="black")
        self.labeltk.grid(column=0,row=0,columnspan=3,sticky='EW')
        self.labelVariabletk.set(u"self._uspwd")
        self.bind('<Control-c>', self.copy)
    
    def copy(self, event=None):
        
        ''' This will allow the user to paste text after selection an acccount from Tab 2. The data in the pop up can be copied and pasted for ease.'''
        
        self.clipboard_clear()
        text = self.MSGtext.get("sel.first", "sel.last")
        self.clipboard_append(text)
        
    def paste(self, event):
        
        ''' This will allow the user to paste text after selection an acccount from Tab 2. The data in the pop up can be copied and pasted for ease.'''
        
        text = self.selection_get(selection='CLIPBOARD')
        self.insert('insert', text)
        


class PSWUI(Tkinter.Tk, Text): # I call Tkinter.tk as the master since it's inherited in this class
    
    '''This is the master class that the program builds off off'''

    
    def __init__(self,parent): 
        Tkinter.Tk.__init__(self,parent) 
        Tkinter.Tk.geometry(self, "820x400+900+900")
        Tkinter.Tk.config(self, bg="white")
        Tkinter.Tk.iconbitmap(self, 'jack.ico') 
        self.testVariable = False    
        self.parent = parent
        s = ttk.Style()
        #A = s.theme_names()
        #K = s.theme_use()
        s.theme_use('xpnative')
        self.replaceSpace = ""
        self.initialize()
      
        
    def initialize(self):
        
        '''This will set up the notebook framework inside the tkinter window. It sets up and configures tab 1, 2 and 3.'''
        
        self.grid()   # set grid to display items on main window
        self.note = ttk.Notebook() #create a notebook with 3 tabs below. All with an action bound to them to track change events.
        
        self.note.config(height=475) 
        self.note.config(width=600)
        self.note.enable_traversal()
        
        # This is for Tab 1
        self.tab1 = Frame(self.note)
        self.tab1.config(relief=RAISED,borderwidth=1)
        self.tab1.bind_all('<Button-1>', self.onTabChange)
        self.note.bind_all('<Button-1>', self.onTabChange)
        self.note.bind_all('<Control-c>', self.copy)
        self.note.bind_all('<Control-z>', self.copy)
        self.tab1.bind('<Control-c>', self.copy)
       
        # This is for tab 2
        self.tab2 = Frame(self.note)
        self.tab2.config(relief=RAISED,borderwidth=1)
         
        #This is for tab 3         
        self.tab3 = Frame(self.note)
        self.tab3.config(relief=RAISED,borderwidth=1)
        self.tab3.bind_all('<Button-1>', self.onTabChange)
        
        # This builds the tabs and gives them titles. 
        self.note.add(self.tab1, text = "Create New ID")
        self.note.add(self.tab2, text = "See Entire List of ID's")
        self.note.add(self.tab3, text = "PSW Expires?")
        self.note.grid(column=0,row=0, columnspan=1, rowspan=5)
        
 
        
        # This is Tab1 configuration and varaibles
        self.labelVariable10 = Tkinter.StringVar()
        self.label20 = Tkinter.Label(self.tab1, width=20, text="Helvetica", font=("Helvetica", 16),textvariable=self.labelVariable10,
                              anchor="w",fg="white",bg="black")
        self.label20.grid(column=0,row=0,sticky='W')
        self.labelVariable10.set("Enter a Name")
        
        self.labelVariable11 = Tkinter.StringVar()
        self.label21 = Tkinter.Label(self.tab1, width=20, text="Helvetica", font=("Helvetica", 16), textvariable=self.labelVariable11,
                              anchor="w",fg="white",bg="black")
        self.label21.grid(column=0,row=1,sticky='W')
        self.labelVariable11.set("Enter a UserName")
        
        self.labelVariable12 = Tkinter.StringVar()
        self.label22 = Tkinter.Label(self.tab1, width = 20, text="Helvetica", font=("Helvetica", 16),textvariable=self.labelVariable12,
                              anchor="w",fg="white",bg="black")
        self.label22.grid(column=0,row=2,  sticky='W')
        self.labelVariable12.set("Enter a Password")
        
        self.labelVariable14 = Tkinter.StringVar()
        self.label23 = Tkinter.Label(self.tab1, width=20, text="Helvetica", font=("Helvetica", 16),textvariable=self.labelVariable14,
                              anchor="w",fg="white",bg="black")
        self.label23.grid(column=0,row=5,sticky='W')
        self.labelVariable14.set("Enter A Counter")
        
        self.labelVariable15 = Tkinter.StringVar()
        self.label24 = Tkinter.Label(self.tab1, width=20, text="Helvetica", font=("Helvetica", 16),textvariable=self.labelVariable15,
                              anchor="w",fg="white",bg="black")
        self.label24.grid(column=0,row=4,sticky='W')
        self.labelVariable15.set("PSW Expires? ")
        
        lst1 = ['Yes','No']
        self.var1 = Tkinter.StringVar()
        drop = Tkinter.OptionMenu(self.tab1 ,self.var1, *lst1)
        drop.grid(column=1, row=4, columnspan = 2, sticky='EW')
        self.var1.set("Choose Yes/No")
        
        self.entryVariable14 = Tkinter.StringVar()
        self.entry14 = Tkinter.Entry(self.tab1, width = 28, text="Helvetica", font=("Helvetica", 16), textvariable=self.entryVariable14)
        self.entry14.grid(column=1, row=5,columnspan = 2, sticky='EW')
        self.entryVariable14.set(time.strftime("%x"))
        self.note.add(self.tab1)
        
        self.entryVariable10 = Tkinter.StringVar()
        self.entry10 = Tkinter.Entry(self.tab1,text="Helvetica", font=("Helvetica", 16), textvariable=self.entryVariable10)
        self.entry10.grid(column=1,row=0, columnspan = 2, sticky='EW')
        self.entryVariable10.set("Enter a Name (ID)") 
        self.note.add(self.tab1)
        
        self.entryVariable11 = Tkinter.StringVar()
        self.entry11 = Tkinter.Entry(self.tab1, text="Helvetica", font=("Helvetica", 16), textvariable=self.entryVariable11)
        self.entry11.grid(column=1,row=1, columnspan = 2, sticky='EW')
        self.entryVariable11.set("Enter a UserName")  
        
        self.entryVariable12 = Tkinter.StringVar()
        self.entry12 = Tkinter.Entry(self.tab1, text="Helvetica", font=("Helvetica", 16), textvariable=self.entryVariable12)
        self.entry12.grid(column=1,row=2,columnspan = 3, sticky='EW')   
        self.entryVariable12.set("Enter a Password")  
        
        self.labelVariable13 = Tkinter.StringVar()
        self.label13 = Tkinter.Label(self.tab1,text="Helvetica", font=("Helvetica", 16), textvariable=self.labelVariable13,
                               anchor="w",fg="black",bg="LightSkyBlue1", borderwidth=1)
        self.label13.grid(column=0,row=6, sticky='EW')
        self.labelVariable13.set(u"Description: ")
        
        self.Dtext = Tkinter.Text(self.tab1, width=73)
        self.Dtext.grid(column=0,row=6,columnspan=3,sticky='EW')
        self.Dtext.insert(1.0, "Description")
        
    
        # This is Tab2 configuration and varaibles
        self.labelVariable20 = Tkinter.StringVar()
        self.labelmessage = Tkinter.Label(self.tab2, text="Helvetica", font=("Helvetica", 16),textvariable=self.labelVariable20,
                              anchor="w",fg="white",bg="black")
        self.labelmessage.grid(column=0,row=0,rowspan=2,sticky='W')
        self.labelVariable20.set(u'''Double click on the Name to access the       
         the account details!''')
    
        self.scroll = Scrollbar(self.tab2, orient=Tkinter.VERTICAL)
        self.scroll.grid(row=0, column=1, rowspan=1)
        self.listvariable1 = Tkinter.StringVar()
        self.userListBox = Tkinter.Listbox(self.tab2, yscrollcommand=self.scroll.set, listvariable=self.listvariable1)
        self.scroll.config(command=self.userListBox.yview)
        self.userListBox.bind('<<ListboxSelect>>', self.onselect)
        self.userListBox.config(font=('helvetica', 12, 'bold underline'))
        self.userListBox.bind("<Double-1>", self.onselect2)
        self.userListBox.grid(column=0, row=2, sticky='EW')
        self.listvariable1.set(self.listPrint())
        self.text = Tkinter.Text(self.tab2)
        
        if os.path.exists("C:\PASSWD.dat"): 
            self.refresh()
            
            
        # This is Tab3 configuration and variables
        self.labelVariable300 = Tkinter.StringVar()
        self.labelmessage = Tkinter.Label(self.tab3, text="Helvetica", font=("Helvetica", 16),textvariable=self.labelVariable300,
                              anchor="w",fg="white",bg="black")
        self.labelmessage.grid(column=0,row=0,sticky='W')
        self.labelVariable300.set(u'''                       List of Passwords to Expire                          ''')  
        
        self.listvariableExpire = Tkinter.StringVar()
        self.userListBoxtab3 = Tkinter.Listbox(self.tab3, activestyle='underline', font=("Helvetica", 16), listvariable=self.listvariableExpire)
        self.userListBoxtab3.grid(column=0, row=1, columnspan=2, sticky='EW')
        #self.resultsExpire = Expires()
        #self.listvariableExpire.set(self.resultsExpire)
        
        # This sets the size of the window and if you can change it or not.
        self.grid_columnconfigure(0,weight=1) 
        self.grid_rowconfigure(0, weight=1)
        self.resizable(False,False)
        self.resizable(False,False)   
              
        # These are buttons on the mainn window with call backs. Sets up some imagines. 
        self.logo = PhotoImage(file="lowes1.gif")
        self.w1 = Tkinter.Label(self, image=self.logo)
        self.w1.config(bd=1)
        self.w1.grid(column=6, row=2, columnspan=2, sticky='n')
        
        # This is for the Database Option. You can only see this when the DBConfig.ini is filled out with values other than default. 
        parser = SafeConfigParser()
        parser.read('C:\Program Files (x86)\PassWordKreeper\DBConConfig.ini')
        A = parser.get('Database_Information', 'username')
        if A == "default" :      
            self.button4 = Tkinter.Button(self, text="Database Sync",
                                    command=self.DBSub)
            self.button4.config(state="disable")
            self.button4.config(padx=0, pady=0, bg='orange', fg='black', bd=10)
            self.button4.config(bd=8, relief=RAISED)
            self.button4.config(font=('helvetica', 12, 'bold italic'))
            self.button4.config(cursor='spider')
            self.button4.grid_forget()
            
        else :
            self.button4 = Tkinter.Button(self, text="Database Sync",
                                    command=self.DBSub)
            self.button4.config(stat="normal")
            self.button4.config(padx=0, pady=0, bg='orange', fg='black', bd=10)
            self.button4.config(bd=8, relief=RAISED)
            self.button4.config(font=('helvetica', 12, 'bold italic'))
            self.button4.config(cursor='spider')
            self.button4.grid(column=7, row=1, sticky='s')
            
        
        #These are all the buttons you see on the main UI. Copy, Delete, Exit and Submit.    
        self.button3 = Tkinter.Button(self, text=u"  Copy  ",
                                     command=self.copyList) 
        self.button3.config(padx=1, pady=1, bg='LightSkyBlue1', fg='black', bd=20)
        self.button3.config(bd=8, relief=RAISED)
        self.button3.config(font=('helvetica', 12, 'bold italic'))
        self.button3.config(cursor='spider')
        self.button3.grid(column=7,row=0, sticky='')   
        self.button3.config(state="disable")
         
        self.button2 = Tkinter.Button(self,text=u" Delete ",
                                      command=self.OnButtonClickDel)
        self.button2.config(padx=1, pady=1, bg='LightSkyBlue1', fg='black', bd=20)
        self.button2.config(bd=8, relief=RAISED)
        self.button2.config(font=('helvetica', 12, 'bold italic'))
        self.button2.config(cursor='spider')
        self.button2.grid(column=7,row=0,sticky="n")
        self.button2.config(state="disable")  
        
        
        self.button1 = Tkinter.Button(self,text=u" Exit ",
                                      command=sys.exit)
        self.button1.config(padx=11, pady=1, bg='LightSkyBlue1', fg='black', bd=20)
        self.button1.config(bd=8, relief=RAISED)
        self.button1.config(font=('helvetica', 12, 'bold italic'))
        self.button1.config(cursor='spider')
        self.button1.grid(column=6,row=0, sticky="")
        
        self.button = Tkinter.Button(self,text=u"Submit", 
                                command=self.OnButtonClick)
        self.button.config(padx=1, pady=1, bg='LightSkyBlue1', fg='black', bd=20)
        self.button.config(bd=8, relief=RAISED)
        self.button.config(font=('helvetica', 12, 'bold italic'))
        self.button.config(cursor='spider')
        self.button.grid(column=6,row=0,sticky="n")
    
        self.grid_columnconfigure(0,weight=1)
        
        self.resizable(False,False)
        

    def DBSub(self):
        
        '''This is to test whether or not the database button should be displayed based on if the DBconfig having values other than the default.'''
        
        if self.testVariable == False :
            self.testVariable = True
            self.button4.config(state="normal")
            self.button4.config(text="DB On")
        else :
           
            self.testVariable = False
            self.button4.config(text="DB Off")
            
    # This is for when I click Submit button. 
    def OnButtonClick(self):   
        
        '''This is for when you hit the submit button. Which I then Take all the information located in the frame and load it into a stream and put it into a file
        This method works very closely with passwdstrA. Which does a lot of date handling and striping of spaces etc.'''
        
        testVariable = True
        if self.entryVariable10.get() == "" :
            tkMessageBox.showinfo("Error", "Please enter a valid Name for the account.")
            testVariable = False
        else :
            self.labelVariable10.set( self.entryVariable10.get())
            self.entry10.selection_range(0, Tkinter.END)
        
        if self.entryVariable11.get() == "":
            tkMessageBox.showinfo("Error", "Please enter a valid UserName")
            testVariable = False
        else :
            self.labelVariable11.set( self.entryVariable11.get())
            self.entry11.selection_range(0, Tkinter.END)           
        
        if self.entryVariable12.get() == "" :
            tkMessageBox.showinfo("Error", "Please enter a valid Password")
            testVariable = False
        else :
            self.labelVariable12.set( self.entryVariable12.get())
            self.entry12.selection_range(0, Tkinter.END)
        if self.var1.get() == "Choose Yes/No":
            tkMessageBox.showinfo("Error", "Does your password expire?")
            testVariable = False
        else :
            pass
        stringVerOfDate = str(self.entryVariable14.get())
        print stringVerOfDate
        if len(stringVerOfDate) != 8 :
            tkMessageBox.showinfo("Error", "Please enter an 8 character valid date xx/xx/xx!")
            testVariable = False
        else :
            pass
             
            
        
        #This dialog box creates a yes or no option using the tkmessagebox yesno and has built in yes no values.
        if testVariable == True : 
            if tkMessageBox.askyesno("Correct?", "Are the Values in Black Correct?" + "\n" + "Please Ensure your password meets the Lowe's minimum requirements" + "\n" +
                                     "1. A minimum of 8 Characters?" + "\n" +
                                     "2. Must contain numbers" + "\n" +
                                     "3. Must contain special Characters Ex: !@#$%^&*" + "\n" +
                                     "4. Must not contain more than 3 characters from the old password." "\n") :
            
                Name = self.entryVariable10.get()
                if " " in Name :
                    Name.replace(" ", "_")

                #This is where I get the values from the GUI and feed them into the passwdstrA module.
                UserName = self.entryVariable11.get()
                PassWord = self.entryVariable12.get()
                Description = self.Dtext.get("0.0", "end")
                Expires = self.var1.get()
                TimeToExpire = self.entryVariable14.get()
                
            Results = PasswordEncrption(Name, UserName, PassWord, Description, Expires, TimeToExpire)
            Results.encrypt()
    
            if self.testVariable == True :
                SubmitPSW(self.entryVariable11.get(), self.entryVariable12.get())
                
        
    def onTabChange(self,event) :
        
        '''This looks for events, events are associated with the tabs. When a tab is selected, code runs in the background to product updates or widgets on the screen'''
        
        A = self.note.index(self.note.select()) 
        print A # Gets tab by 1, 0 or 2 depending on tab selected.
        if A == 1 :
            self.button2.config(state="normal")
            self.button3.config(state='normal')
            self.entryVariable12.set("Enter a Password")
            self.entryVariable11.set("Enter a UserName")
            self.entryVariable10.set("Enter a Name (ID)")
            self.Dtext.insert(1.0, "")
            self.entryVariable14.set(time.strftime("%x"))
            self.refresh()
        elif A == 2 :
            self.resultsExpire = Expires()
            self.listvariableExpire.set(self.resultsExpire)
            self.entryVariable12.set("Enter a Password")
            self.entryVariable11.set("Enter a UserName")
            self.entryVariable10.set("Enter a Name (ID)")
            self.Dtext.insert(1.0, "")
            self.entryVariable14.set(time.strftime("%x"))    
        elif A == 0 :
            self.button2.config(state="disable")
            self.button3.config(state='disable')
            

    def copyList(self):
        
        '''This is a backup option. What this does is allow me to copy the list. It creates a folder in the program directory called
        backUpPswFile. I provide an executable called unlockPassword.py which in the event something goes wrong. You have a copy of your psw file.
        You can open it up and feed in the encrypted passwords and get back out the plain text password'''
        
        if os.path.exists(".passwd.dat"):
            srcfile = '.passwd.dat'
            recordTime = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())   
            recordTimeFormat = recordTime.replace(" ", "_")
            recordTimeFormat = recordTimeFormat.replace(":", "_")
            recordTimeFormat = recordTimeFormat.replace("+", "_")
            os.makedirs("./backUpPswFile/" + recordTimeFormat)
            cPathFolder = "./backUpPswFile/" + recordTimeFormat
            shutil.copy(srcfile, cPathFolder)
        else :
            print "No File Exists in the Path"
            
    def refresh(self):
        
        '''This method will refresh the screen. When an account is added or removed. The list view will refresh by calling this method.'''
        
        self.listvariable1.set(self.listPrint())
          
    def listPrint(self):
        
        ''' This will redirect system output in order to create the actual list of accounts on tab 2'''
        
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        if os.path.exists(".passwd.dat"): 
            data8 = open(".passwd.dat", "rb+")
            e = pickle.load(data8)
            data8.close()
            for element in e:
                if element['ONE'] != "" :
                    print (element["ONE"])
            sys.stdout = old_stdout
            result_string = result.getvalue()
            return result_string
        
        
    def onselect(self, evt):
        
        '''This watches for an event and gives it a number based on cursor selection. This is the index I use to pull up the record to display 
        once a value has been double clicked inside the list on tab 2. '''
        
        w = evt.widget
        index = int(w.curselection()[0])
        self._ValueEvent = w.get(index)
        print ('You selected item %d: "%s"' % (index, self._ValueEvent))
        return self._ValueEvent
        
        
    def onselect2(self, evt):
        
        '''This method takes the onselected() event and uses the account selected on tab 2, to pull up it's associated information stored in a file.'''
        
        data7 = open(".passwd.dat", "rb+")
        e = pickle.load(data7)
        data7.close()
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        for element in e:
            if element['ONE'] == value :
                B = (element["Two"])
                C = (element["Three"])
                E = (element["Four"])
                F = (element["Five"])
                G = (element["Six"])
                DD = base64.b64decode(C)
                D = bz2.decompress(DD)
                Z = "USERNAME: " + B + "\n" + "PASSWORD: " + D + '\n\n' + 'DESCRIPTION:' + E + '\n' + "Expiring:" + F + "\n" + "Date Expired:" + G +"\n"
        DialogWidget(None, Z)
        
           
    def OnButtonClickDel(self):
        
        ''' This will delete items from the list. This is the method that is called when you click delete. '''
        
        indexs = int(self.userListBox.curselection()[0])
        values = self.userListBox.get(indexs)
        data10 = open(".passwd.dat", "rb+")
        e = pickle.load(data10)
        data10.close()
        [element for element in e if element['ONE'] == values]
        e.pop(indexs)
        data11 =  open(".passwd.dat", "wb+")
        pickle.dump(e, data11)
        data11.close() 
        self.refresh()              
       
            
    def copy(self, event=None):
        
        '''A copy clipboard method. Ensures it captures the start and end of your selection'''
        
        self.clipboard_clear()
        text = self.entry10.get("sel.first", "sel.last")
        self.clipboard_append(text)
        
    def paste(self, event):
        
        '''This is a paste method. Just takes from the clipboard and inserts text'''
        
        text = self.selection_get(selection='CLIPBOARD')
        self.insert('insert', text)

#This is the main part of the program. It runs the GUI class and gives the application a title and puts it in the mainloop()  
if __name__ == "__main__":
    app = PSWUI(None)
    app.title('Store your passwords with ease!')
    app.mainloop()
    
    
