# README

Files included within this repo:
* readfilechanges.py - Main Python 2.7 script
* PythonColourValues - [PureData](https://puredata.info) patch for use with script
* RGB Interface.touchOSC - optional interface for use with [touchOSC](https://hexler.net/products/touchosc) (recieved by Pd patch on port 9001)
* README.md - this file

__readfilechanges.py was written using Python 2.7. There is a chance it might break with Python 3.x without any ammendments to the script.__

readfilechanges.py looks for a text file to monitor. The script was written using HexChat chatlog text files specifically.
It is recommended to use HexChat, as it is the only IRC client to have been tested. It also formats things nicely.
In theory, any IRC client /should/ work, so long as they write a chatlog in real time to a textfile. In theory.

The script sends udp packets on the port 3000, which can be received by anything listening to that port on localhost.
It was tested and built for use with a PureData patch, like the one included in this repo.


## SETUP

to change which file readfilechanges.py monitors, edit the line:

filePath = '[PATH TO CHATLOG TEXT FILE]'


The script should then monitor that text file for incoming commands, and send a 'bang' via udp with id's 0, 1, and 2, depending
on the command it reads.

!red = id 0
!green = id 1
!blue = id 2

Once the file path is set,
1. connect to Twitch Chat via IRC client (ensure file path is correct!)
2. run script
3. open .pd file
4. start gemwin within PureData
5. send/receive messages in Twitch Chat


## ADDING COMMANDS

If you wish to include more commands for the python file to recognise, edit the dictionary 'colourLookup' within the script.

For example, if you want to add the command "!rotate" (with the udp id 3) to be recognised, the dictionary will look like*:

colourLookup = {'red\n': '0 bang;',
                'green\n': '1 bang',
                'blue\n': '2 bang'
		'rotate\n': '3 bang'}

*MAKE SURE YOU ADD THE '\n' IN THE DICTIONARY.

You'll then have to edit the PureData patch to listen for a udp message with id 3. And then do what you wish with that incoming bang.
