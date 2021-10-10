from _thread import allocate_lock
class Buffer2():
    def __init__(self):
        self.__lock = allocate_lock()

        self.__Gruppen =[]
        self.__Frage=[]
        self.__Punkteanzeigen=False
        self.__LoesungAnzeigen=False
    def getGruppen(self):
        return self.__Gruppen
    def setGruppen(self,Gruppen):
        self.__lock.acquire()
        self.__Gruppen=Gruppen
        self.__lock.release()
    def setFrage(self,Frage):
        self.__lock.acquire()
        self.__Frage=Frage
        self.__lock.release()
    def getFrage(self):
        return self.__Frage
    def setPunkteanzeigen(self,Punkteanzeigen):
        self.__lock.acquire()
        self.__Punkteanzeigen=Punkteanzeigen
        self.__lock.release()
    def getPunkteanzeigen(self):
        return self.__Punkteanzeigen
    def set__LoesungAnzeigen(self,LoesungAnzeigen):
        self.__lock.acquire()
        self.____LoesungAnzeigen=LoesungAnzeigen
        self.__lock.release()
    def get__LoesungAnzeigen(self):
        return self.____LoesungAnzeigen
    #debug=False

        
