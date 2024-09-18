ladak_szama = int(input("Ládák száma: "))
ladak_tartalma = ""
felpakolt = 0
valid = False
s = ladak_tartalma[0]
half = ladak_szama / 2
i = 0

def input(ladak_tartalma):
    while valid == False:
        valid = True
        ladak_tartalma = input("Ládák tartalma (A/K): ")

        #ellenőrzi hogy az adatot hogy lehet-e vele dolgozni
        if len(ladak_tartalma) == ladak_szama:
            for betu in ladak_tartalma:
                if betu.upper() not in ["A", "K"]:
                    valid = False
                    break


def szamlalo(felpakolt):
    felpakolt = 0
    for lada in ladak_tartalma:
        if lada == s:
            felpakolt += 1
            s = lada
     

while half > i:
    input()
    szamlalo(felpakolt)

print(f"Kamionra felpakolt ládák száma: {felpakolt}")