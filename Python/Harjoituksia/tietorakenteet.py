def listaesimerkki():
    lista = ["Sininen", "Punainen", "Keltainen", "Vihreä"]
    print("Listan ensimmäinen alkio on:", lista[0])
    print("Lista tulostettuna alkio kerrallaan:")
    for i in lista:
        print(i)


ostoslista = []


def valinta():
    print("Haluatko\n(1)Lisätä listaan\n(2)Poistaa listalta vai")
    valittu = input("(3)Lopettaa?: ")
    if valittu == "1":
        lisays = input("Mitä lisätään?: ")
        ostoslista.append(lisays)
    elif valittu == "2":
        print("Listalla on", len(ostoslista), "alkiota.")
        poistettava = int(input("Monesko niistä poistetaan?: "))
        try:
            ostoslista.pop(poistettava)
        except IndexError:
            print("Virheellinen valinta.")
    elif valittu == "3":
        print("Listalla oli tuotteet:")
        for i in ostoslista:
            print(i)
        return False
    else:
        print("Virheellinen valinta.")
    return True


def luejaprinttaa(tiedostonimi):
    tiedosto = open(tiedostonimi, "r")
    lista = tiedosto.readlines()
    tiedosto.close()
    lista.sort()
    for i in lista:
        if len(i) <= 1:
            break
        # poistetaan rivinvaihdot ennen prittausta
        if i[len(i)-1] == "\n":
            i = i[:-1]
        print(i)


def main():
    print("Sanat laitettuna aakkosjärjestykseen:")
    luejaprinttaa("sanoja.txt")


if __name__ == "__main__":
    main()
