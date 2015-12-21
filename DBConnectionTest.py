'''
Created on Mar 11, 2015

@author: Ryan Ruscett



NOTE - This class works in conjunction with the DBConfig.ini and is not currently supported. Please do not use the db-Sync option for it doesn't work well with dates. It 
needs to be updated and if the push is there it can happen. Currently it is not. 

'''
import MySQLdb
from ConfigParser import SafeConfigParser


def connectGetVersionWithPropsFile() :
    
    '''You would run this method by doing DBConnectionTest.connectGetVersionWithPropsFile(). It would take you properties file and get the version of the database you wanted to use.
    This is only if that feature is set up. If it is you will see a sync now button on the GUI and if turned on. It will submit data to a database for storage. '''
    
    parser = SafeConfigParser()
    parser.read('C:\Program Files (x86)\PassWordKreeper\DBConConfig.ini')
    A = parser.get('Database_Information', 'username')
    B = parser.get("Database_Information", 'password')
    C = parser.get("Database_Information", 'databaseName')
    D = parser.get("Database_Information", 'host')
    print (A)
    print (B)
    print (C)
    print (D)
    
    # Open database connection
    db = MySQLdb.connect(D,A,B,C )
    cursor = db.cursor()
    
    # execute SQL query using execute() method.
    sqlVersion = ("SELECT VERSION()")
    try :
        cursor.execute(sqlVersion)
        db.commit()
    except :
        db.rollback()
        db.close()
        
    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print ("Database version : %s " % data)
    
    # disconnect from server
    db.close()

def connectGetVersion() :
    
    '''method to get the version of your database. it's shorter and less to type. It does basically the same thing as the other method in this class'''
    
    # Open database connection
    db = MySQLdb.connect("127.0.0.1","root","salem","ibm_ucd" )
    
    # db = MySQLdb.connect("9.32.253.253","root","root","testdb" )
    cursor = db.cursor()
    
    # execute SQL query using execute() method.
    sqlVersion = ("SELECT VERSION()")
    try :
        cursor.execute(sqlVersion)
        db.commit()
    except :
        db.rollback()
        db.close()
        
    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print ("Database version : %s " % data)
    
    # disconnect from server
    db.close()
    
def SubmitPSW(userName, passWord) :
    
    '''This is the submitPassword function. This is what happens if a database is set up in order to store the data in the database. 
    NOTE: This feature does not currently work with Dates and will need upgrades if it is to be used. '''
    
    parser = SafeConfigParser()
    parser.read('C:\Program Files (x86)\PassWordKreeper\DBConConfig.ini')
    A = parser.get('Database_Information', 'username')
    B = parser.get("Database_Information", 'password')
    C = parser.get("Database_Information", 'UserData')
    D = parser.get("Database_Information", 'host')
     
  
    db = MySQLdb.connect(D,A,B,C )
    cursor = db.cursor()
   
    sqlSubmitname = ("INSERT INTO UDS(name, psw) VALUES(%s, %s)")
   
    try:
        cursor.execute(sqlSubmitname, userName, passWord)
        db.commit()
    except db.Error as err:
        print("Something went wrong: {}".format(err))    
        db.rollback()
    except MySQLdb.DatabaseError as e :
        print("sooo: ".format(e))
    
    except Exception.message :
        print (Exception)
      
    finally:
        db.close()
        
        
    