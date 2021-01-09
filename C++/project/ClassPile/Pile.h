class Pile
{
public:
    Pile(void);
    Pile(int taille);


    void clear(void);


    //get section
    int get_taille(void);
    int get_actualBlocs(void);

    //set section
    void resize(int newSize);
    void push(int value);

private:
    int m_taille;
    int m_pile[10];
};

/*
Attention � ne pas oublier le ; � la fin de la classe dans un
fichier .h ! L'erreur appara�trait dans tous les fichiers ayant
une ligne #include "client.h" , parce que la compilation a lieu
apr�s l'appel au pr�processeur.
*/