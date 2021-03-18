# -*- coding: cp1252 -*-.

import time
import pickle

def printtaavalikko():
    print("(1) Lue muistikirjaa\n(2) Lis�� merkint�\n(3) Muokkaa merkint��\n\
(4) Poista merkint�\n(5) Tallenna ja lopeta\n")

def luotiedosto():
    try:
        tiedosto = open("muistio.dat", "rb")
    except IOError:
        # Jos tiedostoa ei ole, luodaan se ja talletetaan sinne tyhj� lista
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
        # N�m� valintojen k�sittelyt voisivat olla my�s omana metodinaan
        valinta = input("Mit� haluat tehd�?: ")
        if valinta == "5":
            tallennadata(merkinnat)
            print("Lopetetaan.")
            break
        elif valinta == "1":
            if len(merkinnat) > 0:
                for i in merkinnat:
                    print(i)
        elif valinta == "2":
            merkinta = input("Kirjoita uusi merkint�: ")
            merkinnat.append(merkinta + ":::" + paivays)
        elif valinta == "3":
            print("Listalla on", str(len(merkinnat)), "merkint��.")
            muutettava = int(input("Mit� niist� muutetaan?: "))
            muutettavaInd = muutettava - 1
            muutettavateksti = merkinnat[muutettavaInd]
            print(muutettavateksti)
            uusiteksti = input("Anna uusi teksti: ")
            merkinnat[muutettavaInd] = uusiteksti + ":::" + paivays
        elif valinta == "4":
            print("Listalla on", str(len(merkinnat)), "merkint��.")
            poistettava = int(input("Mik� niist� poistetaan?: "))
            poistettavaInd = poistettava - 1
            poistettu = merkinnat.pop(poistettavaInd)
            print("Poistettiin merkint�:", poistettu)

if __name__ == "__main__":
    main()