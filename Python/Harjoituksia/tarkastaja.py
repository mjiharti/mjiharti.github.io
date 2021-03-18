def testaa(syote):
    if len(syote) < 5 or syote.isalpha() or syote.isdigit():
        return False
    else:
        return True
