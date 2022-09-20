def hazi():
    mond = input("Adjon meg egy mondatot: ")
    db = {}
    for i in mond:
        if i in db:
            db[i] = db[i] + 1
        else:
            db[i] = 1
    print("Betűk gyakorisága: ", db)

    txt = mond[::-1]
    print("Fordítva: ", txt)

    print("Listába rendezve szavanként: ", mond.split(" "))
hazi()