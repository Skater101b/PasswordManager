'''
Created on Feb 23, 2015

@author: Ryan Ruscett


This class is a helpfer class for additional functionality that is added. It's only used for testing etc. 

'''
import pickle
import os


def build():
    ''' Test Build method to see if I am including all the files required for this to work in my executable '''
    Mydata_files = []
    for files in os.listdir('.'):
        Mydata_files.append(files)
        
   # buildIndex = Mydata_files.index('build')
   # Mydata_files.pop(buildIndex)
   # buildIndex2 = Mydata_files.index('dist')
   # Mydata_files.pop(buildIndex2)
    print Mydata_files

def DisplayMessages(): 
    PasswordsExpired = open(".passwd.dat", 'r')
    Contents = PasswordsExpired.read()
    Contents.split("")
    print Contents
    PasswordsExpired.close()
 #   for element in e:
 #       if element['six'] != None :
 #           expireList = []
 #           a = (element["six"])
 #           expireList.extend(a)
 #          print expireList
            
 
 
if __name__ == '__main__':
    build()           