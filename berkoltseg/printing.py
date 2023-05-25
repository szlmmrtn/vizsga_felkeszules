from calculating import calculating
import datetime

class printing:
    def __init__(self, ber):
        self.netto = ber
        
    def nyomtatas(self):
        self.szamitas = calculating(self.netto)
        self.szamitas.szamolas()

        
        date = datetime.datetime.now().strftime("%Y/%m/%d")
        
        f = open("szalma_marton.txt","w")
        f.write("Bérköltség lap")
        f.write("\n")
        f.write(f"Nettó bér: {self.netto}.0 Ft")
        f.write("\n")
        f.write(f"Diák bérköltség: {self.szamitas.student}.0 Ft")
        f.write("\n")
        f.write(f"Rendes munkaviszony bérköltség: {self.szamitas.worker}.0 Ft")
        f.write("\n")
        f.write("\n")
        f.write(f"Kelt: Szeged, {date}")
      