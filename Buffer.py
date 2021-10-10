from _thread import allocate_lock
class Buffer():
    def __init__(self):
        self.__lock = allocate_lock()
        self.__Liste_Clients = []
        self.__buffer_In = list()
        self.__buffer_Out = list()
    def BufINget(self):
        self.__lock.acquire()
        if len(self.__buffer_In)==0:
            result = None
        else:
            result = self.__buffer_In.pop(0)
        self.__lock.release()
        return result
    def BufINset(self,Client,Bufin,Regler=-1):
        self.__lock.acquire()
        if Regler==0:
            self.__Liste_Clients.append(Client)
        elif Regler==1:
            self.__Liste_Clients.remove(Client)
            self.__buffer_In.append([Client,Bufin])
        else:
            self.__buffer_In.append([Client,Bufin])
        self.__lock.release()
    def BufOUTget(self,i):
        self.__lock.acquire()
        if len(self.__buffer_Out)==0:
            result = None
        elif self.__buffer_Out[0][0]!=i:
            result = None
        else:
            result = self.__buffer_Out.pop(0)
        self.__lock.release()
        return result
    def BufOUTset(self,Client,Bufin):
        self.__lock.acquire()
        if Client==0:
            for i in self.__Liste_Clients:
                self.__buffer_Out.append([i,Bufin])
        else:
            self.__buffer_Out.append([Client,Bufin])
        self.__lock.release()
