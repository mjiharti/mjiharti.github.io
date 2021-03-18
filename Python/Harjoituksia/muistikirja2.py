# -*- coding: cp1252 -*-.

import time
import pickle

def printtaavalikko():
    print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Muokkaa merkintää\n\
(4) Poista merkintä\n(5) Tallenna ja lopeta\n")

def luotiedosto():
    try:
        tiedosto = open("muistio.dat", "rb")
    except IOError:
        # Jos tiedostoa ei ole, luodaan se ja talletetaan sinne tyhjä lista
        tyhjalista = []
        tiedosto = open("muistio.dat", "wb")
        pickle.dump(tyhjalista, tiedosto)
        tiedosto.close()
        print("Virhe tiedostossa, luodaan uusi muistio.dat.")

def luedata():
    tiedosto = open("muistio.dat", "rb")
    merkintalista = pickle.load(tiedosto)
    tiedosto.close()
    return merkintalista

def tallennadata(lista):
    tiedosto = open("muistio.dat", "wb")
    pickle.dump(lista, tiedosto)
    tiedosto.close()

def main():
    luotiedosto()
    merkinnat = luedata()
    while True:
        paivays = time.strftime("%X %x")
        printtaavalikko()
        # Nämä valintojen käsittelyt voisivat olla myös omana metodinaan
        valinta = input("Mitä haluat tehdä?: ")
        if valinta == "5":
            tallennadata(merkinnat)
            print("Lopetetaan.")
            break
        elif valinta == "1":
            if len(merkinnat) > 0:
                for i in merkinnat:
                    print(i)
        elif valinta == "2":
            merkinta = input("Kirjoita uusi merkintä: ")
            merkinnat.append(merkinta + ":::" + paivays)
        elif valinta == "3":
            print("Listalla on", str(len(merkinnat)), "merkintää.")
            muutettava = int(input("Mitä niistä muutetaan?: "))
            muutettavaInd = muutettava - 1
            muutettavateksti = merkinnat[muutettavaInd]
            print(muutettavateksti)
            uusiteksti = input("Anna uusi teksti: ")
            merkinnat[muutettavaInd] = uusiteksti + ":::" + paivays
        elif valinta == "4":
            print("Listalla on", str(len(merkinnat)), "merkintää.")
            poistettava = int(input("Mikä niistä poistetaan?: "))
            poistettavaInd = poistettava - 1
            poistettu = merkinnat.pop(poistettavaInd)
            print("Poistettiin merkintä:", poistettu)

if __name__ == "__main__":
    main()