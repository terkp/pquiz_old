import socket
import sys
#import Main
from _thread import start_new_thread
from time import sleep

class Testserv2():
    def __init__(self,Buff):
        global HOST, PORT
        self.__Buff=Buff
        HOST = '' # all availabe interfaces
        PORT = 9999 # arbitrary non privileged port 
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print("Could not create socket. Error Code: ", str(msg[0]), "Error: ", msg[1])
            sys.exit(0)

        print("[-] Socket Created")

        # bind socket
        try:
            s.bind((HOST, PORT))
            print("[-] Socket Bound to port " + str(PORT))
        except socket.error:
            print("Bind Failed. Error Code: {} Error: {}".format(str(msg[0]), msg[1]))
            sys.exit()
        self.__i = 0
        s.listen(10)
        print("Listening...")
        self.connecting(s)

    def client_thread(self,conn,i):
        self.__Buff.BufINset(i,"",0)
        while True:
            data = conn.recv(1024)
            if data==b'':
                
                self.__Buff.BufINset(i,"Verbindung unterbrochen",1)
            elif data==b'\r\n':
                pass
            else:
                self.__Buff.BufINset(i,data.decode("utf-8"))
            if not data:
                break
        conn.close()
    def client_thread_senden(self,conn,i):
        conn.send("Welcome to the Server. Type messages and press enter to send.\n".encode('utf-8'))
        while True:
            sleep(0.05)
            reply = self.__Buff.BufOUTget(i)
            if reply!= None:
                try:
                    conn.sendall(reply[1].encode('utf-8')+b'\n')
                except:
                    break
        conn.close()
    def connecting(self,s):
        while True:
            # blocking call, waits to accept a connection
            conn, addr = s.accept()
            self.__i = self.__i+1
            print("["+str(self.__i)+"] Connected to " + addr[0] + ":" + str(addr[1]))
            
            start_new_thread(self.client_thread, (conn,self.__i,))
            start_new_thread(self.client_thread_senden, (conn,self.__i,))
            
        s.close()


