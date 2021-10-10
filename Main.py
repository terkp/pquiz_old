import Testserv2
import Anwendung
import Buffer
import Buffer2
import Anzeige
import Anzeige2
from _thread import start_new_thread
from tkinter import *

class Main():
    def __init__(self):
        Buff = Buffer.Buffer()
        Buff2 = Buffer2.Buffer2()
        root = Tk()
        Ausgabe = Anzeige2.App(root)
        start_new_thread(Anzeige.App,(Buff2,))
        start_new_thread(Testserv2.Testserv2,(Buff,))
        start_new_thread(Anwendung.Anwendung,(Buff,Ausgabe,Buff2))
        root.mainloop()

A = Main()





