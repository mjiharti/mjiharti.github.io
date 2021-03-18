# lause_alku = "Muuttujaan muuttuja on tallennettu"
# lause_loppu = "merkkijonosisältöä"
# print(lause_alku, lause_loppu + ".")

# luku_1 = 1000
# luku_2 = 24
# teksti = "Laskutoimituksen tulos on:"
# tulos = (luku_1+luku_2+15)**2
#
# print(teksti, tulos)

# luku = 10.6411
# merkkijono = "Merkkijono"
#
# luku = int(luku)
# merkkijono = merkkijono*2
#
# print("Kokonaislukumuunnos ei osaa pyöristää:", luku)
# print("Merkkijonon kertominen tuottaa toistoa:", merkkijono)

# print("""Tämä on usean rivin tulostus:
# Teksti on jaettu usealle riville.
# Nimi:\tPetteri
# Ammatti:\t\tKartturi""")

# print("Laskin")
# luku1 = int(input("Anna ensimmäinen luku: "))
# luku2 = int(input("Anna toinen luku: "))
# lopputeksti = "Tulos on: "
#
# print("""(1) +
# (2) -
# (3) *
# (4) /""")
# valinta = input("Tee valinta (1-4): ")
# if valinta == "1":
#     lopputeksti = lopputeksti + str(luku1 + luku2)
# elif valinta == "2":
#     lopputeksti = lopputeksti + str(luku1 - luku2)
# elif valinta == "3":
#     lopputeksti = lopputeksti + str(luku1 * luku2)
# elif valinta == "4":
#     lopputeksti = lopputeksti + str(luku1 / luku2)
# else:
#     lopputeksti = "Valintaa ei tunnistettu."
#
# print(lopputeksti)

# sana = "Hattukauppias"
# print("Muuttujan 4 ensimmäistä kirjainta ovat", sana[0:4])
# print("Muuttujan 4 viimeistä kirjainta ovat", sana[-4:len(sana)])
# print("Muuttujan teksti on väärinpäin", sana[::-1])

class Nimike:
    """Uusi luokka"""
    nimi = "Eemeli"
    suku = "Jaava"
    def nimi(self):
	    print(self.nimi, self.suku)
