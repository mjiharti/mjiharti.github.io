# import random
#
# print("Heitetään kolikkoa viidesti:")
# i = int(0)
# while i < 5:
#     arvonta = random.randint(0, 1)
#     i += 1
#     if arvonta == 0:
#         print("Klaava!")
#     else:
#         print("Kruuna!")

# import moduuli
# moduuli.tulosta("Esimerkkirivi6767")

import tarkastaja

while True:
    testattava = input("Anna testattava sana: ")
    tulos = tarkastaja.testaa(testattava)
    if tulos == True:
        print("Antamasi sana kelpaa salasanaksi!")
        break
    else:
        print("Sana ei kelpaa.")