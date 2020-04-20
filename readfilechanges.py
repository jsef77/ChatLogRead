import time

filePath = 'cmykert_log.txt'

lastLine = None
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
    if lines[-1] != lastLine:
        lastLine = lines[-1]
        print(lines[-1])
    time.sleep(1)

