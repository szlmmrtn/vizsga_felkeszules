class calculating:
    def __init__(self, ber):
        self.netto = ber
        self.student = 0
        self.worker= 0
        
    def szamolas(self):
        self.student = self.netto * 1.15
        self.worker = self.netto * 1.83