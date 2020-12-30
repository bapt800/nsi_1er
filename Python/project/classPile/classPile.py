"""
Baptiste Entat
20 dec 2020
"""
from typing import List


class ClassPile:
    """
    class pour la gestion d'une pile
    """
    def __init__(self, sizePile:int = None, listIn:list = None, debugLevel:int = 0):
        """
        sizePile = Int, listIn = None -> pile de la taille de sizePile\n
        sizePile = None, listIn = lst -> copie de la liste dans la pile\n
        debugLevel:int = 0 -> mode release (essaye d'ignorer les erreur)\n
        debugLevel:int = 1 -> mode debug (leve les exception)
        """
        if debugLevel == 0:
            self._debugLevel = 0
        elif debugLevel == 1:
            self._debugLevel = 1
        else:
            raise NotImplementedError("!-> not implemented param <-!")

        if sizePile != None and listIn == None:
            self._pile = [0]* (sizePile + 1)
            #self._pile[0] = 0 
            self._size = sizePile
        elif sizePile == None and listIn != None:
            self._pile = []
            self._pile.append(len(listIn))
            for i in listIn:
                self._pile.append(i)
            self._size = len(listIn)
        else:
            if self._debugLevel == 1:
                raise NotImplementedError("!-> not implemented param", "\nobj -> ", self, "\nsizePile -> ", sizePile, "\nlisteIn -> ", listIn, "\ndebugLevel -> ", debugLevel, "\n<-!")
                return None

        


    def set_Size(self, newSizePile:int, dataMod:int = 0) -> None:
        """
        change la taille de la pile\n
        dataMod: 0->suppression ; 1->conservation complete ; 2->conservation partiel
        """
        if dataMod == 0: #dataMod: 0->suppression
            self._pile = [0] * (newSizePile + 1)
            self._size = newSizePile
        elif dataMod == 1: #dataMod: 1->mode conservation complete
            if newSizePile < self._size:
                if self._debugLevel == 1:
                    raise Warning("Perte de donnee possible")
                return None
            else:
                for i in range(0, newSizePile - self._size):
                    self._pile.append(0)
                self._size = newSizePile
        elif dataMod == 2: #dataMod: 2->conservation partiel
            buff = []
            for i in range(0, self._size):
                buff.append(self._pile[i + 1])
            self._pile = [0] * (newSizePile + 1)
            self._size = newSizePile
            for i in range(0, newSizePile):
                if i < len(buff):
                    self.push(buff[i])
                else:
                    self.push(0)
                    self._pile[0] -= 1
        else:
            if self._debugLevel == 1:
                raise NotImplementedError("notImplemented value of dataMod -> ", dataMod)
            return None

    def clear(self) -> None:
        self._pile = [0] * (self._size + 1)

    def push(self, value) -> None:
        """
        ajoute une valeur dans la pile
        """
        if (self._pile[0] + 1) > self._size:
            if self._debugLevel == 1:
                raise ValueError("!-> erreur debordement de la pile <-!")
            return None
        else:
            self._pile[self._pile[0] + 1] = value
            self._pile[0] += 1

    def pushList(self, listIn):
        if ((type(listIn) is list) == False) and ((type(listIn) is tuple) == False):
            if self._debugLevel == 1:
                raise NotImplementedError("!-> not implemented type ->", type(listIn)," <-!")
            return None
        elif (self._pile[0] + len(listIn)) > self._size:
            if self._debugLevel == 1:
                raise ValueError("!-> erreur debordement de la pile <-!")
            return None
        iList = 0
        for i in range(self._pile[0], self._pile[0] + len(listIn)):
            self._pile[i + 1] = listIn[iList]
            self._pile[0] += 1
            iList += 1
            
    
    def pop(self) -> None:
        """
        supprime la derniere valeur de la pile
        """
        if (self._pile[0]) <= 0:
            if self._debugLevel == 1:
                raise ValueError("!-> erreur pile vide <-!")
            return None
        else:
            self._pile[self._pile[0]] = 0
            self._pile[0] -= 1
    

    #section get
    def get_ActualBloc(self) -> int:
        """
        renvoie le nombre de bloc actuellement utilisé dans la pile
        """
        return self._pile[0]
    
    def get_Taille(self) -> int:
        """
        renvoie la taille maximal de la pile
        """
        return self._size
    

    def get_pile(self) -> list:
        """
        renvoie la pile sans l'index sous forme de liste
        """
        if self._debugLevel == 0: #illegal en release
            raise PermissionError("illegal lol")

        buff = []
        for i in range(0, self._size):
            buff.append(self._pile[i + 1])
        return buff

    def get_last(self):
        """
        renvoie le dernier element la pile
        """
        return self._pile[self._pile[0]]
    
    def get_lastAndPop(self):
        """
        renvoie le dernier element la pile et le supp
        """
        buff = self.get_last()
        self.pop()
        return buff
    

    #section Fx
    def fx_reverse(self) -> None:
        """
        inverse la pile
        """
        pileWork = []
        for i in range(0, self._size):
            pileWork.append(self._pile[i + 1])
        pileWork.reverse()
        self.clear()
        for i in range(0, len(pileWork)):
            self.push(pileWork[i])
            
    def fx_sort(self) -> None:
        """
        !-> not fully implemented <-!
        tri la pile
        """
        pileWork = []
        for i in range(0, self._size):
            pileWork.append(self._pile[i + 1])
        pileWork.sort()
        self.clear()
        for i in range(0, len(pileWork)):
            self.push(pileWork[i])

    def debug_statPile(self):
        print("--->beging> stats de la pile <<---")
        print("bloc utilisée ->", self.get_ActualBloc(), "sur", self.get_Taille())

        pileClean = []
        for i in range(0, self._size):
            pileClean.append(self._pile[i + 1])
        print("pile sans index interne ->", pileClean)

        print("pile avec index interne ->", self._pile)
        print("pile debugLevel ->", self._debugLevel)
        print("--->END> stats de la pile <<---")

#raise NotImplementedError("!-> not implemented <-!")
