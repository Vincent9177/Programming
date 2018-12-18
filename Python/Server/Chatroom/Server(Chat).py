# !/usr/bin/python3
# ServerMain

import datetime
import random
import re
import socket
import threading
import time

# "Random" List
FileNumberList=["0","1","2","3","4","5","6","7","8","9","0"]
FileStringList=["a","b","c","d","e","f","g","h","i","o","p","q","r","s","t","u","v","w","x","y","z"]
FileCapitalList=["A","B","C","D","E","F","G","H","I","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# Chatroom List
ChatroomList=[]
# Create socket connecting
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Get host and port name
host = str (input("Server Host:")) 
port = int (input("Server Port:"))
# Create Server
s.bind((host,port))
s.listen(5)

# Function "Read time"
def readtime(a):
    nowtimestruct = time.localtime()
    utc = - time.timezone // 3600
    nowtime = "[UTC+%d]"% utc + time.strftime("[%Y-%m-%d %H:%M:%S]",nowtimestruct)
    return nowtime

# Function "debuging"
def debuging(sentenses):
    with open("Server.txt","a") as f:
        f.write(readtime(1) + sentenses)
        f.write("\n")

def random_name(a):
    FileName = random.randint(10000000,99999999)
class chatroom(object):
    def __init__(self,sock,name,ports):
        self.sock = sock
        self.name = name
        self.ports = ports
    def create(self):
        ChatroomList.append(self.name)
        while True:
            data = self.sock.recv(1024)
            if data.decode("utf-8")[:4] == "exit":
                print("%d closed the chatroom %s." %(ports,name))
                ChatroomList.remove(name)
            if data.decode("utf-8")[:10] == self.name:
                print(data.decode("utf-8"))
                self.sock.send(data)
                continue
# Function "tcplink"
def tcplink(sock, addr):
    global create_name
    print("Accept new connecting from %s:%s...." % addr)
    debuging("[%s:%d]Connect successfully." %(addr[0],addr[1]))
    sock.send("%d".encode("utf-8") %(addr[1]))
    while True:
        data = sock.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
            break
        elif re.match("create",data.decode("utf-8")):
            create_name = random_name(1)
            print("%s:%d is creating the chatting room named %s..." %(addr[0],addr[1],create_name))
            sock.send(create_name.encode("utf-8"))
            run = chatroom(sock,create_name,addr[1])
            run.create()
            continue
        elif re.match("join",data.decode("utf-8")):
            sock.send("successful".encode("utf-8"))
            data = sock.recv(1024)
            room = data.decode("utf-8")
            if room in ChatroomList:
                print(room,ChatroomList)
                sock.send("successfully".encode("utf-8"))
                run = chatroom(sock,create_name,addr[1])
                run.create()
                continue
            else:
                print(room,ChatroomList)
                sock.send("none".encode("utf-8"))
                continue
    sock.close()
    print("Connecting from %s:%s closed." % addr)
    debuging("[%s:%s]Connect closed." %(addr))
    

# Accept connecting from client(Create a child threading)
print("Server created at %s..."%(host))
time.sleep(1)
print("Waiting for connecting...")
while True:
    sock, addr = s.accept()
    target = threading.Thread(target=tcplink,args=(sock,addr))
    target.start()

print("%s:%s" % (name.decode('utf-8'),data.decode("utf-8")))
debuging("[%s:%d]Message:%s" %(addr[0],addr[1],data.decode("utf-8")))