import os
import re
import datetime, time
import random
import sqlite3
# import module

DEBUGING = "working"
# function
def try_writes(file,path):
    try:
        with open("%s" % path, "x") as f:
            f.write("%s" % file)
        return "nothave"
    except FileExistsError:
        return "have"
    finally:
        pass

def try_mkdir(name_path,have='',nothave='',end=''):
    try:
        os.mkdir("%s" % name_path)
        return "nothave"
    except FileExistsError:
        return "have"
    finally:
        pass

def k_print(sentenses,x=0.10,a=1): # KIX-print
        a = x
        for x in sentenses:
            print(x,end='')
            time.sleep(a)
        print('',end='\n')

def readtime(a):   # 获取当前时间
    nowtimestruct = time.localtime()
    utc = - time.timezone // 3600
    nowtime = "[UTC+%d]"% utc + time.strftime("[%Y-%m-%d %H:%M:%S]",nowtimestruct)
    return nowtime

def kix_debuging(sentenses,path='KIX\\System\\Errors.txt'): # 错误日志
    nowstime = readtime(1)
    global DEBUGING
    with open("%s" %(path),'a') as f:
        f.write("%s" % nowstime + sentenses)
        f.write("\n")
        return "Success"

def kix_help(): # 帮助
    try:
        with open('KIX\\help.txt','r',encoding="gbk") as f: ###
            print(f.read())
        return True
    except FileNotFoundError:
        time.sleep(1)
        k_print("[KIX]系统丢失此文件,键入 reset help 以修复.")
        return False
    finally:
        pass

def kix_open(path): # 打开文件
    try:
        with open("%s" %(path), 'r') as f:
            print(f.read())
        return True
    except FileNotFoundError:
        k_print('[KIX](Error 02)无法找到路径为 %s 的文件.' %(path))
        return False
    except PermissionError:
        k_print('[KIX](Error 03)%s 的文件格式错误.' %(path))
        return False
    finally:
        pass

def kix_add(path): # 创建文件夹
    try:
        os.mkdir("%s" %(path))
        k_print("[KIX]成功创建路径为 %s 的文件夹." %(path))
        return True
    except OSError:
        k_print("[KIX](Error 04)文件名错误或文件夹名重复.")
        return False
    finally:
        pass

def kix_write(path): # 写入文件
    k_print("[KIX]写入文件模式...")
    write_ln = 0
    try:
        with open("%s"%(path),"a"):
            pass
    except FileExistsError:
        k_print("[KIX](Error 05)文件名重复!")
        return False
    except FileNotFoundError:
        k_print("[KIX](Error 06)路径不存在!")
        return False
    finally:
        pass
    while True:
        write_ln = write_ln + 1
        write_str = str (input("%d " %(write_ln)))
        if write_str == "\exit":
            break
        if write_str == "\\exit":
            with open("%s"%(path),"a") as f:
                f.write("\exit")
            continue
        with open('%s'%(path),"a") as f:
            f.write("%s" %(write_str))
            f.write("\n")
            continue
    k_print("[KIX]写入完成.")
    return True

def kix_documents(path):
    try:
        lookingList = [x for x in os.listdir('%s' %(path)) if os.path.isdir(x)]
    except FileNotFoundError:
        k_print("[KIX](Error 07)此文件夹不存在!")
        return False
    finally:
        k_print("[KIX]当前路径下文件夹:")
        for y in lookingList:
            print(y)
        return True

def kix_logout(username):
    k_print("[KIX]%s 用户登出成功!" %(username))
    logging()

def kix_reset_password(users,have="SYSTEM"):
    kix_system_input = str (input("[KIX SYSTEM]键入新密码:"))
    admin_password = kix_system_input

def kix_reset_help():
    try:
        with open("KIX\\help.txt","x",encoding="gbk") as f:
            f.write('''Welcome to Use KIX system!
Here are some tips:
add <文件夹路径> 创建文件夹.
Documents (文件夹) 查看(指定文件夹内)所有文件.
open <文件路径> 打开文件.
write <写入文件路径> 写入文件 --默认为.txt文件. (路径要求为:<username>\\...)
DEBUGING 将错误信息储存在一个文件中,默认关闭.
********************ADMINISTRATOR*********************
control <password> 在需要控制权限时键入 control 与管理员账号的密码才可获取权限。''')
            return "[KIX]写入帮助文件成功."
    except FileExistsError:
        return False
    finally:
        pass
# KIX 主函数
def kix_main(username,have,inputstr):
    while True:    
        kix_main_input = str (input("%s" %(inputstr)))
        if re.match("help",kix_main_input[:4]):
            return_help = kix_help()
            while True:
                if return_help:
                    break
                continue
            continue
        elif re.match("open",kix_main_input[:4]):
            kix_open_path = kix_main_input[5:]
            return_open = kix_open("%s\\%s\\%s"%("KIX\\Users",username,kix_open_path))
            while True:
                if return_open:
                    break
                continue
            continue
        elif re.match("write",kix_main_input[:5]):
            kix_write_path = kix_main_input[6:]
            return_write =  kix_write("%s\\%s\\%s" %("KIX\\Users",username,kix_write_path))
            while True:
                if return_write:
                    break
                continue
            continue
        elif re.match("documents",kix_main_input[:9]):
            kix_documents_path = kix_main_input[10:]
            return_documents = kix_documents("%s\\%s\\%s" %("KIX\\Users",username,kix_documents_path))
            while True:
                if return_documents:
                    break
                continue
            continue
        elif re.match("reset help",kix_main_input[:10]):
            kix_reset_help()
            continue
        elif re.match("logout",kix_main_input[:6]):
            kix_logout(username)
            while True:
                return_logout = kix_logout(username)
                if return_logout:
                    break
                    logging()
                else:
                    continue
        elif re.match("add",kix_main_input[:3]):
            kix_add_path = kix_main_input[4:]
            return_add =  kix_add("%s\\%s\\%s" %("KIX\\Users",self.username,kix_add_path))
            while True:
                if return_add:
                    break
                continue
            continue
        elif re.match("system.error",kix_main_input[:12]):
            if have == "USERS":
                k_print("[KIX](ERROR 09)权限不足!")
                continue
        else:
            k_print("[KIX](ERROR)%s 不是可执行的命令." %(kix_main_input))
            continue

admin_password = "weiyuxuan"

def logging():
    connect = sqlite3.connect("KIX\\System\\UserData.db")
    cursor = connect.cursor()
    try:
        cursor.execute("CREATE TABLE Users (username TEXT PRIMARY KEY, password TEXT)")
    except sqlite3.OperationalError:
        pass
    finally:
        pass
    while True:
        kix_logging_input = str (input("[KIX]:"))
        if re.match("registe",kix_logging_input[:7]):
            k_print("[KIX]准备注册新用户...")
            kix_logging_input = str (input("[KIX &regedit]Press your Username:"))
            Username = kix_logging_input
            try:
                os.mkdir("KIX\\Users\\%s" %(Username))
            except FileExistsError:
                k_print("%s 用户已存在!" %(Username))
                continue
            finally:
                pass
            kix_logging_input = str (input("[KIX &regedit]Press your password:"))
            Password = kix_logging_input
            cursor.execute("INSERT INTO Users(username,password) VALUES ('%s','%s')" %(Username,Password))
            connect.commit()
            k_print("[KIX]创建新用户成功!")
            continue
        elif re.match("login",kix_logging_input[:5]):
            kix_logging_input = str (input("[KIX &login]Username:"))
            Username = kix_logging_input
            kix_logging_input = str (input("[KIX &login]Password:"))
            Password = kix_logging_input
            if Username == "KIX-SYSTEM-LOGIN" and Password == admin_password:
                k_print("[KIX]system.admin 登入成功.")
                kix_main("system.admin","SYSTEM","[KIX @system<admin>]:")
            cursor.execute("SELECT * from Users where username='%s'" %(Username))
            users_values = cursor.fetchall()
            try:
                values_username = users_values[0][0]
                values_password = users_values[0][1]
                if Username == values_username and Password == values_password:
                    k_print("[KIX]登入成功!")
                    kix_main("%s" %(Username),"have","[KIX @root<%s>]:" %(Username))
                else:
                    k_print("[KIX](Error)用户名或密码错误.")
                    write_debug = "[%s]" %(Username) + "login %s 密码错误." %(Password)
                    continue
            except IndexError:
                k_print("[KIX]用户名或密码错误.")
                write_debug = "[%s]" %(Username) + "login %s 密码错误." %(Password)
            finally:
                pass
            continue
        else:
            k_print("[KIX]指令错误.")
try_mkdir("KIX")
try_mkdir("KIX\\System")
try_mkdir("KIX\\Users")
path_kix_sysfile = try_mkdir("KIX\\System")
path_kix = try_mkdir("KIX")
path_kix_Users = try_mkdir("KIX\\Users")
if path_kix == path_kix_sysfile == path_kix_Users =="nothave":
    print("[KIX SYSTEM]已创建本地文件.")
else:
    print("[KIX SYSTEM]检测到本地文件夹.")

logging()




