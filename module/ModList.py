"""Module pour la gestion des listes"""

def Bool(elmt, liste):
    """prends un element et une liste et renvoie s'il y est présent"""
    if elmt in liste:
        if __name__ == "__main__":
            print("True")
        return True
    else:
        if __name__ == "__main__":
            print("False")
        return False

def Square(liste):
    """met tous les element aux carre"""
    rListe = []
    for i in liste: 
        rListe.append(i**2)
    return rListe

def Inverse(liste):
    rListe = []
    for i in range(len(liste), 0, -1):
        print("**>", i-1)
        rListe.append(liste[i-1])
    return rListe

def Prems(liste):
    rListe = []
    for i in range(0, len(liste)):
        nb = liste[i]
        y = 2
        while y < nb and nb%y != 0:
            y += 1
        if y == nb: rListe.append(liste[i])
        print("/")
        print(i)
    return rListe