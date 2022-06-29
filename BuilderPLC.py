#!python3.9.6
from fileinput import filename
import os
import sys
import time
import json
import glob
import zipfile
import requests


terminalmode = False
forcelibmode = False
silentmode = False
debugmode = False
nolibmode = False
firstrun = True
logmode = False
push = False
sleeptime = 1

path = os.getcwd ()

if silentmode == False:
    print ("PLC builder ver: " + "0.999" + " stable" + "by Alexandr Krasnow")
    print ("Use flag --help to read the help\n")
    if debugmode == True:
        print ("\nFlags: " + str (sys.argv) )


#keys
if len (sys.argv) >= 2:

    key = sys.argv [1]

    if key == "-s":
        silentmode = True

    if key == "--silent":
        silentmode = True

    if key == "--nolib":
        nolibmode = True
        terminalmode = True
        
    if key == "--forcelib":
        forcelibmode = True
        terminalmode = True

    if key == "--custom":
        sleeptime = int (input (""))
        terminalmode = True

    if key == "--debug":
        debugmode = True

    if key == "--upload":
        push = True

    if key == "--help":
        print ("\nЧИТАЙ КЗ!!!\n")
        quit ()
        

if len (sys.argv) >= 2:
    #print ("Enter the path to your program without a file name, if you want to use the current path, then specify the -h key")

    path = sys.argv [len (sys.argv) - 1]
    if debugmode == True:
        print ("Input path: " + str (path))

    if path == "--dir":
        path = os.getcwd ()
    

    checkpath = os.path.exists(path)
    if checkpath == True:
        checkpath = os.path.isfile(path)
        if checkpath == False:
            os.chdir (path)
            terminalmode = True
        else:
            if silentmode == False:
                print ("\nWARNING!!!")
                print ("Do not specify the file name\n")
                print ("Yout path: " + path + "\n")
                print ("Working path: " + os.getcwd ())
                print ("\n")
                input ("--------------------\nPress Enter for restart\n")
            quit ()
    else:
        if silentmode == False:
            print ("\nWARNING!!!")
            print ("Path not found\n")
            print ("Yout path: " + path + "\n")
            print ("Working path: " + os.getcwd ())
            print ("\n")
            input ("--------------------\nPress Enter for restart\n")
        quit ()
file = 0
shortfile = 0
last = 0
new = 0
newmax = 0
lastmax = 0

###FIRSTRUN

for file in glob.glob("*.py"):
    if debugmode == True:

        print ("\nUsing file: " + str (file))
        print ("Path: " + os.getcwd () + "\n")
            


        print ("\n\nLast:" + str (last) + "\n")
        print ("Lastmax: " + str (lastmax) + "\n")
        print ("New: " + str (new) + "\n")
        print ("Newmax: " + str (newmax) + "\n")

        print ("\n\nLast:" + str (last) + "\n")
        print ("Lastmax: " + str (lastmax) + "\n")
        print ("New: " + str (new) + "\n")
        print ("Newmax: " + str (newmax) + "\n\n")

    if silentmode == False:
                
        starttime = time.time ()

        print ("Current: " + str (time.ctime (starttime)))
        print ("\nUsing file: " + str (file))
        print ("Path: " + os.getcwd () + "\n")
            
        print ("Extracting a short file name..." )

    file = file.lower ()
    shortfile = file [::-1]
    shortfile = shortfile [3:]
    shortfile = shortfile [::-1]

    if silentmode == False:
        print ("OK  Shortname: %s\n" % shortfile )


#        print ("Building main file...")
#    f = open ("main.sh", 'wt')
#    f.write ("#! /bin/bash"); 
#    f.write ('python %s'% file );
#    f.close ()

    if silentmode == False:
        print ("OK  Building complite\n")
        print ("Reading file...")
        f = open ("main.sh", 'rt')
        print ("Main File".center (65, "-"))
        print ("")
        print (    f.read ())
        print ("-".center (65, "-"))
        print ("")
        f.close ()
        
        
        print ("Make zip archive...")
    zip = zipfile.ZipFile (shortfile + '.zip', 'w', compression=zipfile.ZIP_DEFLATED)

    if silentmode == False:
        print ("Building archive...")
        print ("File: " + file + "\n")
        
    zip.write (file)
    zip.write ("main.sh")
    zip.close ()

    if silentmode == False:
        print ("Ok   Buildi complite\n")

        print ("Checking zip archive...")
        print (zipfile.is_zipfile(shortfile + '.zip'))
        print ("")


    if silentmode == False:
        print ("Testing zip archive...")
        print ("ZIP".center (65, "-"))
        print ("")
        zip = zipfile.ZipFile (shortfile + '.zip', 'r')
        print (zip.    printdir ())
        print ("-".center (65, "-"))
        print ("")
        zip.close ()

    if push == True:
        with open("config.json", "r") as read_file:
            read = json.load(read_file)
        if silentmode == False:
            print ("\nUploading file")
            print ("Server IP: " + str (read["ip"]))
            print ("Server PORT: " + str (read["port"]))

        fp = open(shortfile + ".zip", 'rb')
        files = {'file': (shortfile + ".zip", open(shortfile + ".zip", 'rb'))}
        urladr = str ("http://" + str(read["ip"]) + ":" + str(read["port"]) + str(read["url"]))

        if silentmode == False:
            print ("Server URL: " + urladr)

        resp = requests.post(urladr, files=files)
        fp.close()

#    if silentmode == False:
#        print ("Cleaning build files...\n")

#        print ("Remove main file")
#    if os.path.isfile('main.sh'):
#        os.remove ('main.sh')
#        if silentmode == False:
#            print ("OK")


    if silentmode == False:
        print ("\nBuild time: " + str (time.time () - starttime) + "sec\n")

    if silentmode == False:
        print ("\n...Enable auto mode...\n")





###LOOP RUN

while True:

    for file in glob.glob("*.c"):

        if debugmode == True:

            print ("\nUsing file: " + str (file))
            print ("Path: " + os.getcwd () + "\n")


            print ("\n\nLast:" + str (last) + "\n")
            print ("Lastmax: " + str (lastmax) + "\n")
            print ("New: " + str (new) + "\n")
            print ("Newmax: " + str (newmax) + "\n")

            print ("\n\nLast:" + str (last) + "\n")
            print ("Lastmax: " + str (lastmax) + "\n")
            print ("New: " + str (new) + "\n")
            print ("Newmax: " + str (newmax) + "\n\n")

        new = os.path.getmtime(file)
        if new > newmax:
            newmax = new
        else:
            time.sleep (sleeptime) 
        
        if newmax != lastmax:
            last = os.path.getmtime(file)

            if last > lastmax: 
                lastmax = last
            else:
                time.sleep (sleeptime)

            if debugmode == True:
                print ("\n\nLast:" + str (last) + "\n")
                print ("Lastmax: " + str (lastmax) + "\n")
                print ("New: " + str (new) + "\n")
                print ("Newmax: " + str (newmax) + "\n\n")

            if silentmode == False:

                starttime = time.time ()

                print ("Current: " + str (time.ctime (starttime)))
                print ("\nUsing file: " + str (file))
                print ("Path: " + os.getcwd () + "\n")
            
                print ("Extracting a short file name..." )

            file = file.lower ()
            shortfile = file [::-1]
            shortfile = shortfile [3:]
            shortfile = shortfile [::-1]

            if silentmode == False:
                print ("OK  Shortname: %s\n" % shortfile )



#                print ("Building main file...")
#            f = open ("main.sh.sh", 'wt')
#            f.write ("#! /bin/bash\n"); 
#            f.write ('python %s\n'% file );
#            f.close ()

            if silentmode == False:
                print ("OK  Building complite\n")
                print ("Reading file...")
                f = open ("main.sh", 'rt')
                print ("Main File".center (65, "-"))
                print ("")
                print (    f.read ())
                print ("-".center (65, "-"))
                print ("")
                f.close ()


                print ("Make zip archive...")
            zip = zipfile.ZipFile (shortfile + '.zip', 'w', compression=zipfile.ZIP_DEFLATED)

            if silentmode == False:
                print ("Building archive...")
                print ("File: " + file + "\n")
            zip.write (file)
            zip.write ("main.sh")
            zip.close ()

            if silentmode == False:
                print ("Ok   Buildi complite\n")

                print ("Checking zip archive...")
                print (zipfile.is_zipfile(shortfile + '.zip'))
                print ("")


            if silentmode == False:
                print ("Testing zip archive...")
                print ("ZIP".center (65, "-"))
                print ("")
                zip = zipfile.ZipFile (shortfile + '.zip', 'r')
                print (zip.    printdir ())
                print ("-".center (65, "-"))
                print ("")
                zip.close ()

            if push == True:
                with open("config.json", "r") as read_file:
                    read = json.load(read_file)
                if silentmode == False:
                    print ("\nUploading file")
                    print ("Server IP: " + str (read["ip"]))
                    print ("Server PORT: " + str (read["port"]))

                fp = open(shortfile + ".zip", 'rb')
                files = {'file': (shortfile + ".zip", open(shortfile + ".zip", 'rb'))}
                urladr = str ("http://" + str(read["ip"]) + ":" + str(read["port"]) + str(read["url"]))

                if silentmode == False:
                    print ("Server URL: " + urladr)

                resp = requests.post(urladr, files=files)
                fp.close()

#            if silentmode == False:
#                print ("Cleaning build files...\n")
#
#                print ("Remove main file")
#            if os.path.isfile('main.sh'):
#                os.remove ('main.sh')
#                if silentmode == False:
#                    print ("OK")


            if silentmode == False:
                print ("\nBuild time: " + str (time.time () - starttime) + "sec\n")


            firstrun = False

            if silentmode == False:
                print ("\n...Waiting for changes...\n")



    if file == 0:
        if silentmode == False:
            print ("\nWARNING!!!")
            print ("Your program file was not found!")
            print ("Make sure that builder is launched from the right place and the program has the .c file extension\n")
            print ("Yout path: " + path + "\n")
            print ("Working path: " + os.getcwd ())
            print ("\n")
            input ("--------------------\nPress Enter for restart\n")
        
        if terminalmode == True:
            quit ()


        


if terminalmode == False:
    if silentmode == False:
        input ("--------------------\nPress Enter for exit\n")
else:
    if silentmode == False:
        print ("\n")
        
        

