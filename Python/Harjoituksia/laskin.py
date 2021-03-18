import math

uusisana = " "

def pyydalukua(teksti):
    while True:
        try:
            luku = int(input(teksti))
        except ValueError:
            print("Virheellinen syöte!")
        else:
            return luku

while True:
    luku1pyynto = "Anna" + uusisana + "ensimmäinen luku: "
    luku2pyynto = "Anna" + uusisana + "toinen luku: "
    luku1 = pyydalukua(luku1pyynto)
    luku2 = pyydalukua(luku2pyynto)
    valinta = 0

    while int(valinta) < 7:
        lopputeksti = ""
        lopputekstin_alku = "Tulos on: "
        print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(luku1/luku2)\n(6)cos(luku1/luku2)\n(7)Vaihda luvut\n(8)Lopeta")
        print("Valitut luvut:", luku1, luku2)
        valinta = input("Tee valinta (1-8): ")
        if valinta == "1":
            lopputeksti += lopputekstin_alku + str(luku1 + luku2)
        elif valinta == "2":
            lopputeksti += lopputekstin_alku + str(luku1 - luku2)
        elif valinta == "3":
            lopputeksti += lopputekstin_alku + str(luku1 * luku2)
        elif valinta == "4":
            lopputeksti += lopputekstin_alku + str(luku1 / luku2)
        elif valinta == "5":
            lopputeksti += lopputekstin_alku + str(math.sin(luku1/luku2))
        elif valinta == "6":
            lopputeksti += lopputekstin_alku + str(math.cos(luku1/luku2))
        elif valinta != "7" and valinta != "8":
            lopputeksti = "Valintaa ei tunnistettu."

        if len(lopputeksti) > 1:
            print(lopputeksti)

    if valinta == "7":
        uusisana = " uusi "
        continue
    if valinta == "8":
        break
