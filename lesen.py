class lesen():
    def __init__(self):
        pass
    def Fragen_einlesen(self,string):
        try:
            fobj = open(string, "r")
            fragen =fobj.readlines()
            fobj.close()
            self.__Liste_Fragen=[]
            #print(fragen)
            j=0
            for zeile in fragen:
                j=j+1
                zeile = zeile.rstrip()
                liste = zeile.split('#')
                lis=[]
                if liste[0]=='normal':
                    lis2=[]
                    for i in range(4):
                        lis2.append(liste[i+2])
                    liste[6] = liste[6].replace('a',"1")
                    liste[6] = liste[6].replace('b',"2")
                    liste[6] = liste[6].replace('c',"3")
                    liste[6] = liste[6].replace('d',"4")
                    try:
                        lis=[liste[0],liste[1],lis2,int(liste[6]),liste[7]]
                    except:
                        lis=[liste[0],liste[1],lis2,int(liste[6])]
                elif liste[0] == "sortier":
                    lis2=[]
                    lis3=[]
                    for i in range(4):
                        lis2.append(liste[i+2])
                    for i in range(4):
                        liste[i+6] = liste[i+6].replace('a',"1")
                        liste[i+6] = liste[i+6].replace('b',"2")
                        liste[i+6] = liste[i+6].replace('c',"3")
                        liste[i+6] = liste[i+6].replace('d',"4")
                        lis3.append(int(liste[i+6]))
                    try:
                        lis=[liste[0],liste[1],lis2,lis3,liste[10]]
                    except:
                        lis=[liste[0],liste[1],lis2,lis3]
                elif liste[0] == "schaetzen":
                    try:
                        lis=[liste[0],liste[1],int(liste[2]),liste[3]]
                    except:
                        lis=[liste[0],liste[1],int(liste[2])]
                self.__Liste_Fragen.append(lis)
            return self.__Liste_Fragen
        except:
            print("Einlesen Fehlgeschlagen bei Zeile "+str(j))
            return []

