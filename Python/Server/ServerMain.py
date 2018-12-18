# !/usr/bin/python3
# ServerMain

# import modules
import socket
import time
import threading
import datetime
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

# Function "tcplink"
def tcplink(sock, addr):
    print("Accept new connecting from %s:%s...." % addr )
    name = sock.recv(1024)
    print("%s:%d name = %s." %(addr[0],addr[1],name.decode("utf-8")))
    debuging("[%s:%d][%s]Connect successfully." %(addr[0],addr[1],name.decode("utf-8")))
    sock.send("Your port number:%d".encode("utf-8") %(addr[1]))
    while True:
        data = sock.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
            break
        print("%s:%s" % (name.decode('utf-8'),data.decode("utf-8")))
        debuging("[%s:%d]Message:%s" %(addr[0],addr[1],data.decode("utf-8")))
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
