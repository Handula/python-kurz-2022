def cislo():
    telefonni_cislo = input("Jake je Vase telefonni cislo: ")
    if len(telefonni_cislo) == 9:
        return True
    elif len(telefonni_cislo) == 13 and telefonni_cislo[:4]== "+420":
        return True
    else:
        return False
print(cislo()) 


def zprava():
        sms = input("Zde prosim vypiste zpravu, kterou chcete poslat: ")
        delka = len(sms)
        cena = (delka//180)*3
        print(f"Tato zprava bude stat {cena} kc")
print(zprava())