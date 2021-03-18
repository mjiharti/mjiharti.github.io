class Kilpailija():
    """Kilpailija: sisältää pisteet ja värin"""
    vari = ""
    pisteet = 0

    def __init__(self):
        self.vari = input("Anna minulle väri: ")

    def aseta_arvot(self, annettuvari, annetutpisteet):
        self.vari = annettuvari
        self.pisteet = annetutpisteet

    def tulosta(self):
        print("Kilpailijalla", self.vari, "on", str(self.pisteet), "pistettä!")

    def maali(self):
        self.pisteet += 1

    def tilanne(self):
        print("Olen", self.vari, "ja minulla on", self.pisteet, "pistettä!")

def main():
    eka = Kilpailija()
    toka = Kilpailija()
    eka.tilanne()
    toka.tilanne()
    print(eka.__doc__)

if __name__ == "__main__":
    main()