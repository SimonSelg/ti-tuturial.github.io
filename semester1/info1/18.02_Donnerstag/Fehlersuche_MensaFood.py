class MensaEssen():
    def init(list)
        """ Im list wird eine Liste mit Liste mit dem Gericht und die Anzahl der Gerichte angegeben """
        self.liste = list
        
    def getStatus(self):

        def getStatusHelper(liste):
            print( "Gericht" , liste[0][0] , "existiert noch" , liste[0][1],"Mal")
            getStatusHelper(liste[1:])

        getStatusHelper(self.liste)
        
    def buyFood(self,food):
        for lst in self.liste:
            if food = lst[0]:
                lst[1] -= 1
                break

    def bringFood(self,food):
       for lst1 in self.liste:
           for lst2 in food:
                if lst1[0] == lst2[0]:
                    lst1[1] += lst2[1]
                    break
