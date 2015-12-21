from distutils.core import setup
import py2exe
import os

'''This is used to build the program with py2exe'''


    
''' Test Build method to see if I am including all the files required for this to work in my executable '''
    
Mydata_files = []
for files in os.listdir('.'):
    Mydata_files.append(files)
        
buildIndex = Mydata_files.index('build')
Mydata_files.pop(buildIndex)
buildIndex2 = Mydata_files.index('dist')
Mydata_files.pop(buildIndex2)

    

setup(windows=['testnotbookgui.py'],
      data_files = Mydata_files,
      options = {
                 "py2exe": {
                            }
                 }
      )