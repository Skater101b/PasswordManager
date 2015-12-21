'''
Created on Aug 12, 2015

@author: Ryan Ruscett
'''
import sys
import bz2
import base64

    
def unlockPasswords():
    '''This will unlock passwords from a copy of the file in the event there is an issue. Follow the prompts and add the password when required'''
    
    print '''
    -------------------------------------------------------------
    -------------------------------------------------------------
    Let's get you your passwords back. 
    Please open a copy of your passwords file into an editor.
    You will be asked for the password you wanted converted into 
    plan text.
             
    ------------------------------------------------------------
    ------------------------------------------------------------
             '''
    loopValue = True
    while (loopValue):
        print ''' 
    -------------------------------------------------------
    Do you have another Password you would like to get??? 
    Please type Y for yes and N for no.
    -------------------------------------------------------
                '''
        
        YesorNo = str(raw_input("Yes or No Y/N: "))
        YesorNo.lower()
        yes = 'y'
        no = 'n'
        if (YesorNo == yes):
            promptingAction();
        elif (YesorNo == no):
            sys.exit()    

            
def unlock(passwordToUnlock):  
    unEncode = base64.b64decode(passwordToUnlock)
    textValue = bz2.decompress(unEncode)
    print "Your Password is: " + textValue    
    
   
def promptingAction():  
    PasswordValue = str(raw_input("Please enter the password here and hit enter: "))
    unlock(PasswordValue)    
    

if __name__ == '__main__':
    unlockPasswords()