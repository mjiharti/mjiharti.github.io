# tiedostonimi = input("Minkäniminen tiedosto luodaan?: ")
# sisalto = input("Mitä kirjoitetaan tiedostoon?: ")
# tiedosto = open(tiedostonimi, "w")
# tiedosto.write(sisalto)
# tiedosto.close()
# print("Luotiin tiedosto", tiedostonimi, "ja siihen tallennettiin teksti:", sisalto)

# tiedosto = open("merkkijonoja.txt", "r")
#
# while True:
#     rivi = tiedosto.readline()
#     if len(rivi) <= 1:
#         break
#     if rivi[len(rivi)-1] == "\n":
#         rivi = rivi[:-1]
#     if rivi.isalnum():
#         print(rivi, "kelpaa salasanaksi.")
#     else:
#         print(rivi, "sisältää virheellisiä merkkejä.")
#
# tiedosto.close()
