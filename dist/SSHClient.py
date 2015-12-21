import getpass

import telnetlib


def Connect(): 
    HOST = "9.32.253.253"

    user = raw_input("Enter your remote account: ")

    password = getpass.getpass()
 
    tn = telnetlib.Telnet(HOST)
#tn.read_until("You are about to send your password information to a remote computer in Internet zone. This might not be safe. Do you want to send anyway(y/n): \r\n")
#tn.write("n")


    tn.read_until("login:\r\n ", 5)

    tn.write(user + "\r\n", )


    tn.read_until("Password: " , 5)
    tn.write(password + "\r\n")
    tn.interact()
    print (tn.read_very_eager())


    
