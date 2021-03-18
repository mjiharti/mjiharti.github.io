def toinenpotenssi(luku):
    print("Toinen potenssi on", str(luku ** 2))

def tulosta(tulostus = "Oletustulostus"):
    print(tulostus)

def pituusmitta(mitattava):
    return int(len(mitattava))

def main():
    while True:
        syote = input("Anna syöte (Lopeta lopettaa): ")
        if syote == "Lopeta":
            break
        pituus = pituusmitta(syote)
        if pituus > 0:
            print("Antamasi syöte oli", str(pituus), "merkkiä pitkä.")
        else:
            print("Et antanut syötettä.")

if __name__ == "__main__":
    main()
