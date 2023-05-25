class Szamitas:
    def __init__(self,aold,bold):
        self.aold=aold
        self.bold=bold
        self.ter=0
        self.ker=0

    def szamol(self):
        self.ter=self.aold*self.bold
        self.ker=2*(self.aold+self.bold)