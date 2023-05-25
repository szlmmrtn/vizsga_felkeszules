
from szamitas import Szamitas
from datetime import datetime

class Kiir:
    def __init__(self,nev,aold,bold):
        self.nev=nev
        self.aold=aold
        self.bold=bold

    def nyomtatos_funkcio(self):
        self.szamol = Szamitas(self.aold,self.bold,)
        self.szamol.szamol()

        date=datetime.now().strftime("%Y/%m/%d")


        f=open("gyetyinas_daniel.txt","w")
        f.write("Számitásos lap")
        f.write("\n")
        f.write(f"Felhasználó neve: {self.nev}")
        f.write("\n")
        f.write(f"Egyik oldal hossza: {self.aold} m")
        f.write("\n")
        f.write(f"Másik oldal hossza: {self.bold} m")
        f.write("\n")
        f.write(f"Kerület {self.szamol.ker} m")
        f.write("\n")
        f.write(f"Terület {self.szamol.ter} m")
        f.write("\n")
        f.write("\n")
        f.write(f"Kelt: Szeged,{date}")
        