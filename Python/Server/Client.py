# !/usr/bin/python3
# Client

# import modules
import socket
import sys

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
while True:
    try:
        name = str (input("Press Your Name:"))
        host = str (input("ConnectHost:"))
        port = int (input("ConnectPort:"))
        break
    except ValueError:
        break
        print("数据类型错误.")
        sys.exit()
    finally:
        pass
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
else:
    s.send(name.encode("utf-8"))
    recv = s.recv(1024)
    print(recv.decode("utf-8"))
    while True:
        send = str (input(">>>"))
        if send == "exit":
            break
        s.send(send.encode("utf-8"))
        print("Sending message successfully.")
        continue
    s.close()
finally:
    pass
