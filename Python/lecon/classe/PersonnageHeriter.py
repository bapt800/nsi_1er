class Personnage:
    
    def __init__(self, nomPersonnage = "", degatsPersonnage= 10, vitessePersonnage= 10):
        self.nom= nomPersonnage
        self.degat = degatsPersonnage
        self.vitesse= vitessePersonnage
    
    def AfficheStat(self):
        print(self.nom)
        print(self.degat)
        print(self.vitesse)

class Archer(Personnage):
    def __init__(self, nomPersonnage = "", degatsPersonnage= 8, vitessePersonnage= 12):
        Personnage.__init__(self, nomPersonnage, degatsPersonnage, vitessePersonnage)
        self.specialAttack= "cat spike"
        

Zelda= Archer("Zelda")
Zelda.AfficheStat()
print(Zelda.specialAttack)
