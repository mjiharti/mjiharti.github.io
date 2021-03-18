def kasitteleluku():
    try:
        luku = int(input("Anna luku: "))
        print("Syöte oli kelvollinen.")
        return
    except Exception:
        print("Virheellinen syöte!")

def kasitteletiedosto(nimi, lisays):
    try:
        tiedosto = open(nimi, "r")
        luku = int(tiedosto.readline())
        tuloste = luku + lisays
    except IOError:
        print("Virheellinen tiedostonnimi")
    except ValueError:
        print("Tiedoston sisältö virheellinen!")
    else:
        print("Saatiin tulos", str(tuloste))

def main():
    tiedostonimi = input("Anna tiedoston nimi: ")
    kasitteletiedosto(tiedostonimi, 313)

if __name__ == "__main__":
    main()

