class Team:
	def __init__(self, nev, projekt, szerep):
		self.nev = nev
		self.projekt = projekt
		self.szerep = szerep

	def __str__(self):
		return "-- Developer létrehozva. --" + '\n' + self.nev + " a " + self.projekt + \
				"-en dolgozik " + self.szerep + " szerepkörben."

	def __eq__(self, uj_fej):
		return self.nev + " és " + uj_fej.nev + " dolgoznak egy projekten."

Fejleszto1 = Team("Ricsi", "SolArch", "Frontend")
Fejleszto2 = Team("Angéla", "ZerTeng", "Tesztelő")
Fejleszto3 = Team("Peti", "KefERP", "Backend")
Fejleszto4 = Team("Éva", "KefERP", "Frontend")
alkalmazottak = [Fejleszto1, Fejleszto2, Fejleszto3, Fejleszto4]


def egy_projekt():
	for i in range(len(alkalmazottak)):
		print(alkalmazottak[i])
	print()
	for i in range(len(alkalmazottak)):
		for j in range(len(alkalmazottak)):
			if i != j and i < j and alkalmazottak[i].projekt == alkalmazottak[j].projekt:
				print(alkalmazottak[i] == alkalmazottak[j])


if __name__ == "__main__":
	egy_projekt()
