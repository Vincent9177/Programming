import sqlite3
import os

class vlog:
    """
    Module vlog
    This login system is written by python3/sqlite3.
    You can use this system to improve your project or code and simplify your code.
    """
    class connect:
        """
        Create the login system.
        How to use:
        x = vlog.connect(name,[path])
        Args explain:
        name:The login system's name.
        [path]:The login system's data path.(default value:absolute path)
        """
        def __init__(self,name,path=os.getcwd()):
            self.__name = name
            self.__path = r"%s\vlog.db" %(path)
            self.__connect = sqlite3.connect(self.__path)
            self.__cursor = self.__connect.cursor()
            try:
                self.__cursor.execute("CREATE TABLE %s(username TEXT PRIMARY KEY,password TEXT)" %(self.__name))
            except sqlite3.OperationalError:
                pass
            finally:
                pass
        def add(self,username,password):
            self.__cursor.execute("INSERT INTO %s(username,password) VALUES('%s','%s');" %(self.__name,username,password))
        def selectin(self,username,password):
            self.__cursor.execute("SELECT * FROM %s WHERE username = '%s' AND password = '%s'"%(self.__name,username,password))
            self.__result = self.__cursor.fetchall()
            if self.__result:
                return True
            else:
                return False
        def delete(self):
            pass
        def commit(self):
            self.__cursor.commit()
            return True
        def select(self):
            pass

class SystemExistsError(Exception,vlog):
    pass
class SystemNotFoundError(Exception,vlog):
    pass

domain = vlog.connect("s")
domain.add("is","is")
domain.add("is","is")