'''
Created on Feb 23, 2015

@author: Ryan Ruscett
'''
import pickle
import bz2
import os
import re
import base64
import MySQLdb
from FTP import SubmitPSW
from FTP import connectGetVersion
from FTP import SubmitPSW
import datetime

class PasswordEncrption() :
    
    '''This class is used when you hit the submit button in the gui. It takes all the fields and adds them to a file. Based on the Date and time to expire, it also stores the value with 
    either 90 days extended to it and or 360 days extended to it. '''
    
    def __init__(self, ids, usr, pwd, dsc, expire, timeTilExpire) :
        self.id = ids
        self.pwd = pwd
        self.usr = usr
        self.dsc = dsc
        self.cnt = expire
        self.TTE = timeTilExpire
         
    def encpsword(self) :
        
        '''Encyrpts the password'''
        
        nPsw = base64.b64decode(self.pwd)
        plainPSW = bz2.decompress(nPsw)
        return plainPSW
    
    def reverseDESC(self):
        
        '''Reverses the encryption but a seperate file is used for that unlockPassword.py in the event of a failure. This should not be used '''
        
        plainDESC = self.pwd
        return plainDESC    
        
    def encrypt(self): 
        
        '''Second part of the encryption process is here. As well as the conversion of the date and storage to a file.'''
        
        plainPSW = bz2.compress(self.pwd)
        nPsw = base64.b64encode(plainPSW)
        print (self.dsc)
        
        submitDate = datetime.datetime.strptime(self.TTE, "%m/%d/%y")
        if self.cnt.lower() == "yes" :
            submitDate = submitDate + datetime.timedelta(days=90)
            submitDate = str(submitDate).split(" ")
            self.TTE = submitDate[0]
        else:
            submitDate = submitDate + datetime.timedelta(days=360)
            submitDate = str(submitDate).split(" ")
            self.TTE = submitDate[0]
            
        if os.path.exists(".passwd.dat"):     
            BackPack = []
            data = open(".passwd.dat", 'rb+')
            BackPack = pickle.load(data)
            data.close()
            print self.id + "a"
            if " " in self.id :
                self.id.replace(" ", "_")
                print self.id + "b"
            UserDictionary = {"ONE" : self.id.replace(" ","_"), "Two": self.usr, "Three": nPsw, "Four": self.dsc, "Five": self.cnt, "Six":self.TTE}
            BackPack.append(UserDictionary)
            datat2 = open(".passwd.dat", 'wb+')
            done = pickle.dump(BackPack, datat2)
            datat2.close() 
               
        else:
            plainPSW = bz2.compress(self.pwd)
            BackPack = []
            data = open(".passwd.dat", 'wb+')
            UserDictionary = {"ONE" : self.id, "Two": self.usr, "Three": nPsw, "Four": self.dsc }
            BackPack.append(UserDictionary)
            done = pickle.dump(BackPack, data)
            data.close()     
        
    def search(self, name):
        
        '''This method is for seraching, not currently implemented in the program at this time '''
        
        BackPack = []
        data3 = open(".passwd.dat", 'rb+')
        BackPack = pickle.load(data3)
        data3.close()
        for p in BackPack:
            if p['One'] == name:
                return p  
   
    
    
    
    


