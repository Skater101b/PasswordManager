'''
Created on Aug 18, 2015

@author: Ryan Ruscett
'''

import pickle
import os
import datetime 
import time
import sys
import StringIO

def Expires():
    
    '''This method takes the date for the password. Get's today's date. Then it compares today's date to the expire date and determines if the account is within 10 day so expiring. 
    If it is, than tab 3 within the progrma will display the name and date of the account and a message indicating if it is going to expire or already has. I do nothing for passwords 
    that are in good standing. '''
    
    if os.path.exists(".passwd.dat"):     
        data = open(".passwd.dat", 'rb+')
        dataStack = pickle.load(data)
        data.close()
        tenDays = ""
        for element in dataStack:
            if element['Six'] != "" :
                prepTime = element['Six']
                prepTime = prepTime[2:]
                timeObject = datetime.datetime.strptime(prepTime, '%y-%m-%d')
                timeObject = timeObject + datetime.timedelta(days=-10)
                compareDate = datetime.datetime.now()
                if compareDate >= timeObject:
                    tenDays += (element['ONE'] + "_" +  element['Six'] + "._less_than_ten_days. ")
                elif compareDate == timeObject :
                    tenDays += (element['ONE'] + "_" +  element['Six'] + "._Expires_today. ")
                elif compareDate > timeObject :
                    tenDays += element['ONE'] + "_" +  element['Six'] + "._ID_Expired{8-("
                else :
                    pass
    tenDays += str('No_other_passwords_to_expire.')
    return tenDays       
                
                
#This is for testing purpsoes only            
#if __name__ == '__main__':
#    Expires()