mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)
cara = "=" * 35
nabidka = """1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""
print("VÍTEJTE U NAŠÍ APLIKACE DESTINATIO")
print(cara)
print(nabidka)
print(cara)
destinace = input("CISLO DESTINACE:")
cele_jmeno = input("JMENO:") + input("PRIJMENI:")
email = input("EMAIL:")
print(cara)
print("CISLO DESTINACE:" + " " + destinace)
print(cara)
spravna_destinace = mesta[int(destinace) - 1]
cena = ceny[int(destinace) - 1]
print(spravna_destinace)
print(cena)
print(cara)
print(f"""DEKUJI, {cele_jmeno} ZA OBJEDNAVKU,
CIL. DESTINACE: {spravna_destinace}, CENA JIZDNEHO: {cena},
NA TVUJ MAIL {email} JSME TI POSLALI LISTEK.""")
print(cara)
      