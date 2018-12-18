import os
import re
import datetime, time
import random
import sqlite3
# import module

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
    with open("%s" %(path),'a') as f:
        f.write("%s" % nowstime + sentenses)
        f.write("\n")

def kix_logout(username):
    k_print("[KIX]%s 用户登出成功!" %(username))
    logging()

def logging():
    connect = sqlite3.connect("users.db")
    cursor = connect.cursor()
    try:
        create_table = "CREATE TABLE Users (username TEXT PRIMARY KEY, password TEXT)"
        cursor.execute(create_table)
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
                k_print("%s 用户已存在!")
                continue
            finally:
                pass
            kix_logging_input = str (input("[KIX &regedit]Press your password:"))
            Password = kix_logging_input
            insert_table = "INSERT INTO Users(username,password) VALUES ('%s','%s')" %(Username,Password)
            cursor.execute(insert_table)
            connect.commit()
            write_debug = "[%s]" %(Username) + "registe 注册成功."
            kix_debuging("%s" %(write_debug))
            k_print("[KIX]创建新用户成功!")
            continue
        elif re.match("login",kix_logging_input[:5]):
            kix_logging_input = str (input("[KIX &login]Username:"))
            Username = kix_logging_input
            kix_logging_input = str (input("[KIX &login]Password:"))
            Password = kix_logging_input
            cursor.execute('SELECT * from Users where username=?', ('%s' %(Username),))
            users_values = cursor.fetchall()
            try:
                values_username = users_values[0][0]
                values_password = users_values[0][1]
                if Username == values_username and Password == values_password:
                    k_print("[KIX]登入成功!")
                    write_debug = "[%s]" %(Username) + "login 登入成功."
                    kix_debuging("%s" %(write_debug))
                    RUNNING = guest("%s" %(Username),"[KIX @users<%s>]" %(Username))
                    RUNNING.kix_main()
                else:
                    k_print("[KIX](Error 11)用户名或密码错误.")
                    write_debug = "[%s]" %(Username) + "login %s 密码错误." %(Password)
                    kix_debuging("%s" %(write_debug))
                    continue
            except IndexError:
                k_print("[KIX]用户名或密码错误.")
                write_debug = "[%s]" %(Username) + "login %s 密码错误." %(Password)
                kix_debuging("%s" %(write_debug))
            finally:
                pass
            continue
        else:
            k_print("[KIX]指令错误.")
# class
class guest(object):
    def __init__(self,username,inputstr):
        self.username = username
        self.inputstr = inputstr
    def kix_add(path): # 创建文件夹
        try:
            os.mkdir("%s" %(path))
            k_print("[KIX]成功创建路径为 %s 的文件夹." %(path))
            return "add %s 文件夹创建成功."
        except OSError:
            k_print("[KIX](Error 04)文件名错误或文件夹名重复.")
            return "add (Error 04)%s 文件名错误或文件名重复." %(path)
        finally:
            pass
    def kix_help(): # 帮助
        try:
            with open('KIX\\help.txt','r',encoding="gbk") as f: ###
                print(f.read())
            return "help 获取帮助成功"
        except FileNotFoundError:
            time.sleep(1)
            k_print("[KIX]系统丢失此文件,键入 reset help 以修复.")
            return "help (Error) 丢失文件"
        finally:
            pass
    def kix_open(path): # 打开文件
        try:
            with open("%s" %(path), 'r') as f:
                print(f.read())
            return "open %s 打开文件成功." %(path)
        except FileNotFoundError:
            k_print('[KIX](Error 02)无法找到路径为 %s 的文件.' %(path))
            return "open (Error 02)%s 路径文件不存在." %(path)
        except PermissionError:
            k_print('[KIX](Error 03)%s 的文件格式错误.' %(path))
            return "open (Error 03)%s 文件格式错误." %(path)
        finally:
            pass
    def kix_add(path): # 创建文件夹
        try:
            os.mkdir("%s" %(path))
            k_print("[KIX]成功创建路径为 %s 的文件夹." %(path))
            return "add %s 文件夹创建成功." %(path)
        except OSError:
            k_print("[KIX](Error 04)文件名错误或文件夹名重复.")
            return "add (Error 04)%s 文件名错误或文件名重复." %(path)
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
            return "write (Error 05)%s 文件名重复." %(path)
        except FileNotFoundError:
            k_print("[KIX](Error 06)路径不存在!")
            return "write (Error 06)%s 路径不存在." %(path)
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
        return "write %s 路径文件写入成功." %(path)
    def kix_reset_help():
        try:
            with open("KIX\\help.txt","x",encoding="gbk") as f:
                f.write('''Welcome to Use KIX system!
Here are some tips:
add <文件夹路径> 创建文件夹.
Documents (文件夹) 查看(指定文件夹内)所有文件.
open <文件路径> 打开文件.
write <写入文件路径> 写入文件 --默认为.txt文件. (键入 \exit 可退出，键入\\exit可输入'\exit')
DEBUGING 将错误信息储存在一个文件中,默认关闭.
********************ADMINISTRATOR*********************
control <password> 在需要控制权限时键入 control 与管理员账号的密码才可获取权限。''')
                return "[KIX]写入帮助文件成功."
        except FileExistsError:
            return "[KIX](Error 08)帮助文件已存在."
        finally:
            pass
    def kix_add(path): # 创建文件夹
        try:
            os.mkdir("%s" %(path))
            k_print("[KIX]成功创建路径为 %s 的文件夹." %(path))
            return "add %s 文件夹创建成功."
        except OSError:
            k_print("[KIX](Error 04)文件名错误或文件夹名重复.")
            return "add (Error 04)%s 文件名错误或文件名重复." %(path)
        finally:
            pass
    def kix_main(self):
        while True:
            kix_main_input = str (input("%s" %(self.inputstr)))
            if re.match("help",kix_main_input[:4]):
                return_help = guest.kix_help()
                while True:
                    if return_help:
                        break
                    continue
                write_debug = "[%s]" %(self.username) + "%s" %(return_help)
                kix_debuging(write_debug)
                continue
            elif re.match("open",kix_main_input[:4]):
                kix_open_path = kix_main_input[5:]
                return_open = guest.kix_open("%s\\%s\\%s"%("KIX\\Users",self.username,kix_open_path))
                while True:
                    if return_open:
                        break
                    continue
                write_debug = "[%s]" %(self.username) + "%s" %(return_open)
                kix_debuging(write_debug)
                continue
            elif re.match("write",kix_main_input[:5]):
                kix_write_path = kix_main_input[6:]
                return_write =  guest.kix_write("%s\\%s\\%s" %("KIX\\Users",self.username,kix_write_path))
                while True:
                    if return_write:
                        break
                    continue
                write_debug = "[%s]" %(self.username) + "%s" %(return_write)
                kix_debuging(write_debug)
                continue
            elif re.match("documents",kix_main_input[:9]):
                kix_documents_path = kix_main_input[10:]
                return_documents = guest.kix_documents("%s\\%s\\%s" %("KIX\\Users",self.username,kix_documents_path))
                while True:
                    if return_documents:
                        break
                    continue
                write_debug = "[%s]" %(self.username) + "%s" %(return_documents)
                kix_debuging(write_debug)
                continue
            elif re.match("reset help",kix_main_input[:10]):
                guest.kix_reset_help()
                write_debug = "[%s]" %(self.username) + "%s" %("[KIX]reset help 修复帮助文件成功.")
                kix_debuging(write_debug)
                continue
            elif re.match("add",kix_main_input[:3]):
                kix_add_path = kix_main_input[4:]
                return_add =  guest.kix_add("%s\\%s\\%s" %("KIX\\Users",self.username,kix_add_path))
                while True:
                    if return_add:
                        break
                    continue
                write_debug = "[%s]" %(self.username) + "%s" %(return_add)
                kix_debuging(write_debug)
                continue
            elif re.match("logout",kix_main_input[:6]):
                kix_logout(self.username)
                while True:
                    return_logout = kix_logout(self.username)
                    if return_logout:
                        break
                        k_print("[KIX]用户登出成功.")
                        write_debug = "[%s]" %(self.username) + "logout 登出成功."
                        kix_debuging("%s" %(write_debug))
                        logging()
                    else:
                        continue
            else:
                k_print("[KIX](ERROR)%s 不是可执行的命令." %(kix_main_input))
                write_debug = "[%s]" %(self.username) + "%s" %("[KIX](ERROR)%s 不是可执行的命令." %(kix_main_input))
                kix_debuging(write_debug)
                continue
class managers(guest):
    def reset_password(username):
        pass
        

logging()