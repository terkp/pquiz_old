from tkinter import *
import lesen
from _thread import allocate_lock
from tkinter.filedialog import askopenfilename



    

class App:
    def __init__(self,master):
        self.__lock = allocate_lock()
        self.__nästeFstart = False
        self.__weiter=True
        self.__Loan=False
        self.__Punkteanzeigen=False
        self.__Aenderungflag=False
        self.__Datein=lesen.lesen()
        self.__Liste_Fragen=[]
        self.__Gruppen=[]
        self.Frage=-1
        self.neFrag=False
        #Spieler,akktuelle Anwort, Punkte ,Aktiv, Löschen
        self.__Gruppenaenderung=[-1,-1,-1,False,False]
        frame = Frame(master)
        frame.pack()
        frame2 = Frame(master)
        frame2.pack()



        self.slogan = Button(frame,
                             text="Nächste Frage senden     ",
                             command=self.setFrageT)
        self.slogan.pack(side=LEFT)
        self.weiterb = Button(frame,
                             text="Lösung Anzeigen",
                             command=self.LoAnT)
        self.weiterb.pack(side=LEFT)
        self.weiterb = Button(frame,
                             text="Anworten Anzeigen",
                             command=self.weiterT)
        self.weiterb.pack(side=LEFT)
        self.weiterb = Button(frame,
                             text="Punkte Anzeigen",
                             command=self.PunkteanzeigenTrue)
        self.weiterb.pack(side=BOTTOM)
        self.weiterb = Button(frame,
                             text="Frage Anzeigen",
                             command=self.PunkteanzeigenFalse)
        self.weiterb.pack(side=BOTTOM)
        Button(frame2,text='File Open', command=self.callback).pack(fill=X)
        self.w = Canvas(frame2, width=500, height=300)
        self.w.pack()
        self.Guppenakk()
        Label(frame2, text="Gruppe:").pack(side=LEFT)
        self.e_Gruppe = Entry(frame2, width=10)
        self.e_Gruppe.pack(side=LEFT)
        Label(frame2, text="Antwort:").pack(side=LEFT)
        self.e_Antwort = Entry(frame2, width=10)
        self.e_Antwort.pack(side=LEFT)
        Label(frame2, text="Punkte:").pack(side=LEFT)
        self.e_Punkte = Entry(frame2, width=10)
        self.e_Punkte.pack(side=LEFT)
        self.aendernb = Button(frame2,
                             text="Ändern",
                             command=self.aendern)
        self.aendernb.pack(side=LEFT)
        self.aktivb = Button(frame2,
                             text="Aktiv",
                             command=self.aktiv)
        self.aktivb.pack(side=LEFT)
        self.delb = Button(frame2,
                             text="Gruppe Löschen",
                             command=self.deleteG)
        self.delb.pack(side=LEFT)
        Label(master, text="Punkte/ normal:").pack(side=LEFT)
        self.Punkte_normal = Entry(master, width=5)
        self.Punkte_normal.pack(side=LEFT)
        Label(master, text="sortier:").pack(side=LEFT)
        self.Punkte_sortier = Entry(master, width=5)
        self.Punkte_sortier.pack(side=LEFT)
        Label(master, text="schaetzen 1:").pack(side=LEFT)
        self.Punkte_schaetzen = Entry(master, width=5)
        self.Punkte_schaetzen.pack(side=LEFT)
        Label(master, text="2:").pack(side=LEFT)
        self.Punkte_schaetzen2 = Entry(master, width=5)
        self.Punkte_schaetzen2.pack(side=LEFT)
        self.Punkte_normal.insert(0, "1")
        self.Punkte_sortier.insert(0, "1")
        self.Punkte_schaetzen.insert(0, "2")
        self.Punkte_schaetzen2.insert(0, "1")
        Label(master, text="Frage:").pack(side=LEFT)
        self.ak_Frage = Entry(master, width=5)
        self.ak_Frage.pack(side=LEFT)
        self.ak_Frageae = Button(master,
                             text="Ändern",
                             command=self.Frage_aendern)
        self.ak_Frageae.pack(side=LEFT)

    def Frage_aendern(self):
        self.__lock.acquire()
        try:
            self.Frage=int(self.ak_Frage.get())
            self.neFrag=True
        except:
            pass
        self.__lock.release()
    def deleteG(self):
        self.__lock.acquire()
        try:
            self.__Gruppenaenderung=[int(self.e_Gruppe.get())-1,-1,-1,False,True]
            self.__Aenderungflag=True
        except:
            self.__Aenderungflag=False
        self.__lock.release()
    def aendern(self):
        self.__lock.acquire()
        try:
            try:
                antwort = int(self.e_Antwort.get())
            except:
                antwort = -1
            try:
                punkte = int(self.e_Punkte.get())
            except:
                punkte = -1
            self.__Gruppenaenderung=[int(self.e_Gruppe.get())-1,antwort,punkte,-False,False]
            self.__Aenderungflag=True
        except:
            self.__Aenderungflag=False
        self.__lock.release()
    def Gruppenae(self):
        if self.__Aenderungflag:          
            self.__Aenderungflag=False
            return self.__Gruppenaenderung
        else:
            return True
    def aktiv(self):
        self.__lock.acquire()
        try:
            self.__Gruppenaenderung=[int(self.e_Gruppe.get())-1,-1,-1,True,False]
            self.__Aenderungflag=True
        except:
            self.__Aenderungflag=False
        self.__lock.release()
        
    def Guppenakk(self):
        self.w.delete("all")
        j=0
        
        #self.w.create_text(10,10+j*30,text=str(j)+': ')
        for Typ in self.__Gruppen:
            j=j+1
            self.w.create_text(10,j*20,text=str(j)+': ',font=("Cambria", 15))
            self.w.create_text(100,j*20+10,text=Typ[0],font=("Cambria", 15))
            self.w.create_text(240,j*20,text=Typ[1],font=("Cambria", 15))
            self.w.create_text(300,j*20,text=Typ[2],font=("Cambria", 15))
            self.w.create_text(350,j*20,text=str(Typ[3]),font=("Cambria", 15))
        self.w.after(300,self.Guppenakk)
    def setGruppen(self,gruppen):
        self.__Gruppen=gruppen
    def callback(self):
        name = askopenfilename()
        self.__Liste_Fragen = self.__Datein.Fragen_einlesen(name)
    def setFrageT(self):
        self.__lock.acquire()
        self.__nästeFstart = True
        self.__lock.release()
    def setFrageF(self):
        self.__lock.acquire()
        self.__nästeFstart = False
        self.__lock.release()
    def weiterT(self):
        self.__lock.acquire()
        self.__weiter = True
        self.__lock.release()
    def weiterF(self):
        self.__lock.acquire()
        self.__weiter = False
        self.__lock.release()
    def LoAnT(self):
        self.__lock.acquire()
        self.__Loan = True
        self.__lock.release()
    def LoAnF(self):
        self.__lock.acquire()
        self.__Loan = False
        self.__lock.release()
    def PunkteanzeigenTrue(self):
        self.__lock.acquire()
        self.__Punkteanzeigen = True
        self.__lock.release()
    def PunkteanzeigenFalse(self):
        self.__lock.acquire()
        self.__Punkteanzeigen = False
        self.__lock.release()
    def getFrage(self):
        return self.__nästeFstart
    def getWeiter(self):
        return self.__weiter
    def getLoAn(self):
        return self.__Loan
    def getPunkteanzeigen(self):
        return self.__Punkteanzeigen
    def holeFragen(self):
        return self.__Liste_Fragen
    #def adebug(self,Buff2):
     #   print("hä?")
      #  if Buff2.debug==False:
       #     Buff2.debug=True
        #else:
         #   Buff2.debug=False
