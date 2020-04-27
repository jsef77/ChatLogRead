import time
import os

filePath = 'C:\Users\josef\AppData\Roaming\HexChat\logs\Twitch IRC\#cmykert.log'
lastLine = None

colourLookup = {'red\n': '0 bang;',
                'green\n': '1 bang',
                'blue\n': '2 bang'}



def send2Pd(message):
    #sending messages to PureData

    #debug = "debug"
    cmdMessage = "echo {} | pdsend 3000 localhost udp".format(message)
    os.system(cmdMessage)
    #print(cmdMessage)
    time.sleep(1)
    print("Sent!")


def CommandDetect(newCommand):
    #dealing with detected !commands

        newCommand = newCommand.split("!")[1]
        print('!COMMAND ALERT: ' + newCommand)
        if newCommand in colourLookup:
            print('Command Recognised!')
            print("Sending to PureData...")
            send2Pd(colourLookup.get("{}".format(newCommand)))
        else:
            print('Command Not Recognised. Ignored.')
            newCommand = None
        
        #message = colourLookup.get("{}".format(newCommand), "NO ")
        #print(message + "value sent!")
        #print(newCommand)
        #send2Pd(newCommand)
        #print("Sent!")




with open(filePath,'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            print(line)
            lastLine = line

while True:
    with open(filePath,'r') as f:
        lines = f.readlines()
        
            
#Detect '!'        
    if "!" in lines[-1] and lines[-1] != lastLine:
        lastLine = lines[-1]
        CommandDetect(lines[-1])
        
    elif lines[-1] != lastLine:
        lastLine = lines[-1]
        print(lines[-1])
    time.sleep(1)



