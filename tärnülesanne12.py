# Katseandmed

# Refleksiivne
maatriksA = [[1, 0, 0],
             [0, 1, 0],
             [0, 0, 1], ]
# Pole refleksiivne
maatriksB = [[1, 0, 0],
             [0, 0, 0],
             [0, 0, 1], ]

maatriksC = [[1, 0],
             [0, 1],
             [0, 0]]

maatriksG = [[0, 0, 0, 0],
             [0, 1, 0, 1],
             [0, 0, 0, 0],
             [0, 1, 0, 1]]

def on_refleksiivne(maatriks):
    veerg = 0

    try:
        # Tsükliga läbime maatriksi peadiagonaali
        for rida in range(len(maatriks)):
            # print("rida " + str(rida))
            # print("veerg " + str(veerg))
            # print("element " + str(maatriks[rida][veerg]))
            # print("---")
            # print(A[rida-1][veerg])
            if maatriks[rida][veerg] != 1:
                return False
            veerg += 1
    # Kui maatriksil ridu<veerge või ridu>veerge, siis läheme mõõtmetest välja minna - sel juhul tagastame False.
    except:
        return False
    # Kui peadiagonaalil on ühed, siis tagastame True
    return True


maatriksD = [[0, 1, 1],
             [1, 0, 0],
             [1, 0, 0], ]

maatriksE = [[0, 1],
             [1, 0],
             [0, 0], ]


def on_symmeetriline(maatriks):
    # Tsükliga läbime maatriksi peadiagonaalist ülespoole jäävad elemendid
    for rida in range(len(maatriks)):
        for veerg in range(len(maatriks[rida])):
            try:
                # Kui tegemist on peadiagonaali elemendiga, siis jätame vahele.
                print("rida " + str(rida))
                print("veerg " + str(veerg))
                print("element " + str(maatriks[rida][veerg]))

                if rida == veerg:
                    print("Jätan vahele")
                    print("...")
                    continue
                # print("läksin edasi")
                # Kui leiame sellise paari millel ei leidu sümmeetrilist paari - ehk implikatsiooni eeldus on tõene
                # aga järeldus väär, siis tagastame false

                elif maatriks[rida][veerg] == 1 and maatriks[veerg][rida] != 1:
                    # print("element: " + str(maatriks[rida][veerg] == 1))
                    # print("refleksiivne element: " + str(maatriks[veerg][rida]))
                    print("Ei leidu sümmeetrilist paari")
                    print(maatriks[rida][veerg])
                    print("...")
                    return False
                elif maatriks[rida][veerg] == 1 and maatriks[veerg][rida] == 1:
                    print("Leidsin sümmeetrilise paarilise")
                    print("Paariline element: " + str(maatriks[rida][veerg]))
                    print("...")

            except IndexError:
                print("Läksin maatriksist välja, jätkan")
            continue
        print("Rida " + str(rida) + " tehtud")
        print("...")

    return True


maatriksF = [[0, 1, 0],
             [0, 1, 1],
             [1, 1, 0], ]


def on_antisymmeetriline(maatriks):
    # Peame kontrollima piadiagonaalilt väljaspool olevaid elemente. Kui leidub 1, siis tema peegel peab olema 0 ja vastupidi.
    # Tsükliga läbime maatriksi peadiagonaalist ülespoole jäävad elemendid
    for rida in range(len(maatriks)):
        for veerg in range(len(maatriks[rida])):
            try:
                # Kui tegemist on peadiagonaali elemendiga, siis jätame vahele.
                print("rida " + str(rida))
                print("veerg " + str(veerg))
                print("element " + str(maatriks[rida][veerg]))

                if rida == veerg:
                    print("Jätan vahele")
                    print("...")
                    continue
                # print("läksin edasi")
                # Kui leiame sellise paari millel ei leidu sümmeetrilist paari - ehk implikatsiooni eeldus on tõene
                # aga järeldus väär, siis tagastame false

                # Kui leiame elemendi väljaspool peadiagonaa
                elif maatriks[rida][veerg] == 1 and maatriks[veerg][rida] == 1:
                    # print("element: " + str(maatriks[rida][veerg] == 1))
                    # print("refleksiivne element: " + str(maatriks[veerg][rida]))
                    print("Leidub sümmeetriline paar, väljaspool peadiagonaali - St seos pole antisümmeetriline")
                    print("Paariline element: " + str(maatriks[veerg][rida]))
                    print("...")
                    return False
                elif maatriks[rida][veerg] == 1 and maatriks[veerg][rida] != 1:
                    print("Pole sümmeetrilist paarilist")
                    print(maatriks[veerg][rida])

                    print("...")

            except IndexError:
                print("Läksin maatriksist välja, jätkan")
            continue
        print("Rida " + str(rida) + " tehtud")
        print("...")

    return True


# Transitiivne
maatriksH = [[0, 1, 1],
             [0, 0, 1],
             [0, 0, 0], ]
# Pole transitiivne,
maatriksI = [[0, 1, 1],
             [0, 0, 1],
             [0, 1, 0], ]

maatriksTühi = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0], ]


def on_transitiivne(maatriks):
    # Peame kontrollima piadiagonaalilt väljaspool olevaid elemente. Kui leidub 1, siis tema peegel peab olema 0 ja vastupidi.
    # Tsükliga läbime maatriksi peadiagonaalist ülespoole jäävad elemendid
    for rida in range(len(maatriks)):
        for veerg in range(len(maatriks[rida])):
            try:
                if maatriks[rida][veerg] == 1:
                    # Kui tegemist on peadiagonaali elemendiga, siis jätame vahele.
                    print("Seos: " + "(" + str(rida) + ":" + str(veerg) + ")")
                    print("element " + str(maatriks[rida][veerg]))
                    kontrollitavRida = veerg

                    # Kontrollime kas sama veeru numbriga reas eksisteeriv seos
                    for kontrollitavVeerg in range(len(maatriks[kontrollitavRida])):
                        if maatriks[kontrollitavRida][kontrollitavVeerg] == 1 and maatriks[rida][
                            kontrollitavVeerg] != 1:
                            print("Leiduvad paarid, mille korral eeldus on tõene ja väide väär")
                            print("Kui " + "(" + str(rida) + ":" + str(veerg) + ") ja " + "(" + str(kontrollitavRida) +
                                  ":" + str(kontrollitavVeerg) + "), siis " + "(" + str(rida) + ":" +
                                  str(kontrollitavVeerg) + ") ei kuulu seosesse")
                            return False

                        if maatriks[kontrollitavRida][kontrollitavVeerg] == 1 and maatriks[rida][
                            kontrollitavVeerg] == 1:
                            print("Leiduvad paarid, mille korral eeldus on tõene ja väide tõene")
                            print("Kui " + "(" + str(rida) + ":" + str(veerg) + ") ja " + "(" + str(kontrollitavRida) +
                                  ":" + str(kontrollitavVeerg) + "), siis " + "(" + str(rida) + ":" +
                                  str(kontrollitavVeerg) + ") kuulub seosesse")

            except IndexError:
                print("Läksin maatriksist välja, jätkan")
            continue
        print("Rida " + str(rida) + " tehtud")
        print("...")

    return True


# print(on_refleksiivne(maatriksA))
# print(on_refleksiivne(maatriksB))
# print(on_refleksiivne(maatriksC))
#print("------------------------")
# print(on_symmeetriline(maatriksE))
# print(on_antisymmeetriline(maatriksG))
print("Test: " + str(on_refleksiivne(maatriksG)))
print(on_symmeetriline(maatriksG))
print(on_antisymmeetriline(maatriksG))
print(on_transitiivne(maatriksG))

