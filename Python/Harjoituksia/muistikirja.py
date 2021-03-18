# -*- coding: cp1252 -*-.
import time

# Alustellaan merkkijonoja
tiedostonimi = "muistio.txt"
valikkoteksti = "(1) Lue muistikirjaa\n(2) Lis�� merkint�\n(3) Tyhjenn� muistikirja\n(4)\
 Vaihda muistiota\n(5) Lopeta\n"
kaytossa = "K�ytet��n muistiota:"
tyhjennetty = "Muistio tyhjennetty."
eiloydy = "Tiedostoa ei l�ydy, luodaan tiedosto."
lopetetaan = "Lopetetaan."

try:
    tiedosto = open(tiedostonimi, "r")
    tiedosto.close()
except IOError:
    print("Oletusmuistioa ei l�ydy, luodaan tiedosto.")
    # Luodaan oletusmuistio
    tiedosto = open(tiedostonimi, "a")
    # suljetaan samoin tein, koska viel� ei olla kirjoittamassa mit��n
    tiedosto.close()

while True:
    print(kaytossa, tiedostonimi)
    print(valikkoteksti)
    valinta = input("Mit� haluat tehd�?: ")

    if valinta == "1":
        tiedosto = open(tiedostonimi, "r")
        sisalto = tiedosto.read()
        tiedosto.close()
        print(sisalto)
    if valinta == "2":
        tiedosto = open(tiedostonimi, "a")
        uusi_merkinta = input("Kirjoita uusi merkint�: ")
        paivays = time.strftime("%X %x")
        tiedosto.write(uusi_merkinta + ":::" + paivays + "\n")
        tiedosto.close()
    if valinta == "3":
        tiedosto = open(tiedostonimi, "w")
        tiedosto.close()
        print(tyhjennetty)
    if valinta == "4":
        try:
            tiedostonimi = input("Anna tiedoston nimi: ")
            tiedosto = open(tiedostonimi, "r")
            tiedosto.close()
        except:
            print(eiloydy)
            # luodaan puuttuva tiedosto
            tiedosto = open(tiedostonimi, "w")
            tiedosto.close()
    if valinta == "5":
        print(lopetetaan)
        break
