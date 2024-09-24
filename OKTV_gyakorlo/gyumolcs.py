import random

#ládak szama (2<N<100 000, N páros szám))
n = 100
ladak_szama = n

#ládák tartalma
ladak_tartalma = ['A'] * int(n/2) + ['K'] * int(n/2)
random.shuffle(ladak_tartalma)
#print(ladak_tartalma)

kozep = ladak_szama / 2
arany = 1


#ismétlés ameddig nem lesz egyenlő az arány
while arany != 0:
    #értékek nullázása
    arany = 0
    ertek = 1
    felpakolt = 0
    keresett = "A"
    i = 0

    while i < ladak_szama:
        #'kozep'-et elérve a 'keresett' és 'ertek' kicserélése
        if i == kozep:
            keresett = "K"
            ertek = -1
        #ládák számolása
        if ladak_tartalma[i] == keresett:
            felpakolt += 1
            arany += ertek
        
        i += 1

    #'kozep' változtatása
    if arany > 0:
        kozep = (kozep - ladak_szama) / 2
    elif arany < 0:
        kozep = (kozep + ladak_szama) / 2

#kiíratások
#print("arány:", arany)
print(f"Kamionra felpakolt ládák száma: {felpakolt}")