class Spieler():
    def __init__(self,name,Servernummer):
        self.Gruppe = name
        self.Punkte = 0
        self.Server = Servernummer
        self.Aktiv= True
        self.aktuelleAntwort = 0
        self.zeit=0
