def rombolas():
    import string
    with open("hazi.txt", 'r', encoding="UTF-8") as f:
        szoveg = f.readlines()

        lista = []
        for i in range(0, len(szoveg)):
            lista.append("")

        for i in range(0, len(szoveg)):
            for j in szoveg[i]:
                if j not in string.punctuation and j != "\n":
                    lista[i] += j

        nincs_ures = []
        for i in lista:
            if i != "":
                nincs_ures.append(i)

        mgh = ["a", "A", "á", "Á", "e", "E", "é", "É", "i", "I", "í", "Í", "o", "O", "ó", "Ó", "ö", "Ö",
               "ő", "Ő", "u", "U", "ú", "Ú", "ü", "Ü", "ű", "Ű"]

        nincs_mgh = []

        for i in range(len(nincs_ures)):
            nincs_mgh.append("")

        for i in range(0, len(nincs_ures)):
            for j in nincs_ures[i]:
                if j not in mgh:
                    nincs_mgh[i] += j

        ures = []

        for i in range(0, len(nincs_mgh)):
            ures.append("")

        for i in range(0, len(nincs_mgh)):
            for j in nincs_mgh[i]:
                if j != " ":
                    ures[i] += j

        with open("ki.txt", 'w') as ki:
            for i in range(0, len(ures)):
                if (i+1) % 3 == 0:
                    ki.write(ures[i] + "\n")


if __name__ == "__main__":
    rombolas()
    