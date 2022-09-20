def hazi2():
    print("Adjon meg egy számot és egy mértékegységet (cm/inch): ")
    ert = float(input())
    mert = input()
    if "inch" in mert:
        ert = ert * 2.54
        print(ert)
    elif "cm" in mert:
        ert = ert / 2.54
        print(ert)
    else:
        print("Not correct unit!")
hazi2()
