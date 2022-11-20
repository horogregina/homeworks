elrendezes = "{0:>5}{1:>1}{2:>5}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}{11:>4}{12:>4}{13:>4}"
print(elrendezes.format("", " ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"))
print("\t:--------------------------------------------------", sep="")
lista = []
for i in range(0, 12):
    for j in range(1, 13):
        lista.append((i + 1) * j)
    print(elrendezes.format(str(i + 1), ":", lista[0],  lista[1],  lista[2],  lista[3],  lista[4],  lista[5],  lista[6],  lista[7],  lista[8],  lista[9],  lista[10],  lista[11]))
    lista = []
