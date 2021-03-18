class Emo:
    arvo = 0
    tila = "Toiminnassa"

    def nimi(self):
        print("Minä olen emoluokka.")

class Lapsi(Emo):

    def nimi(self):
        print("Minä olen lapsiluokka.")

def main():
    emo = Emo()
    lapsi = Lapsi()
    print(emo.tila)
    emo.nimi()
    print(lapsi.tila)
    lapsi.nimi()

if __name__ == "__main__":
    main()
