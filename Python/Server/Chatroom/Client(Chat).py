# !/usr/bin/python3
# Client

# import modules
import socket
import sys
import re
import threading

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
while True:
    try:
        host = str (input("ConnectHost:"))
        port = int (input("ConnectPort:"))
        break
    except ValueError:
        break
        print("数据类型错误.")
        sys.exit()
    finally:
        pass
def accept(port,s,name):
    while True:
        accept_data = s.recv(1024)
        if accept_data.decode("utf-8")[:10] == name:
            ports = accept_data.decode("utf-8")[11:16]
            msg = accept_data.decode("utf-8")[17:]
            print("%s:%s" %(ports,msg))
            continue
        continue
def send(port,s,name):
    while True:
        send = str (input("%s:%s:" %(port,name)))
        send_data = "%s %s %s" %(name,port,send)
        s.send(send_data.encode("utf-8"))
        continue
        
def Chatroom(port,s,name):
    sends = threading.Thread(target=send,args=(port,s,name))
    accepts = threading.Thread(target=accept,args=(port,s,name))
    accepts.start()
    sends.start()
try:
    s.connect((host,port))
except ConnectionRefusedError:
    print("无法连接(服务器不存在),请检查 IP 和 端口号 输入正确.")
    sys.exit()
except OSError:
    print("非法的 IP 和 端口号 地址.")
    sys.exit()
except ConnectionResetError:
    print("远程主机强迫关闭连接.")
    sys.exit()
except NameError:
    print("未输入数据.")
    sys.exit()
else:
    recv = s.recv(1024)
    print("Your Port Number:",recv.decode("utf-8"))
    while True:
        send = str (input("%s:" %(recv.decode("utf-8"))))
        if send == "exit":
            break
        elif re.match("create",send[:6]):
            print("创建聊天室...")
            s.send("create".encode("utf-8"))
            print("成功发送请求.")
            create_message = s.recv(1024)
            print("成功创建聊天室,编号为 %s." %(create_message.decode("utf-8")))
            Chatroom(recv.decode("utf-8"),s,create_message.decode("utf-8"))
        elif re.match("join",send[:4]):
            room = str (input("聊天室号码:"))
            s.send("join".encode("utf-8"))
            print("成功发送请求.")
            data0 = s.recv(1024)
            if data0.decode("utf-8") == "successful":
                s.send(room.encode("utf-8"))
                data = s.recv(1024)
                if data.decode("utf-8") == "successfully":
                    print("加入 %s 聊天室成功." %(room))
                    Chatroom(recv.decode("utf-8"),s,room)
                    continue
            elif data.decode("utf-8") == 'none':
                print("房间不存在,请检查房间号后重试.")
                continue
        continue
    s.close()
finally:
    pass
