
# coding: utf-8

# In[15]:

class Gangster:
    def __init__(self, gunshothits=28, bullets=6, bagofdope="20 g's of finest dope"):
        self.gunshothits = gunshothits
        self.bullets = bullets  # Semantischer Fehler
        self.bagofdope = bagofdope
        

    def shootaguy(self):
        counthits = 0
        for shot in range(self.bullets):
            if shot % 2 == 0:   # Semantischer Fehler
                print("Killer!!!")
                counthits += 1   # Laufzeit
            else:
                print("shoot again!!!")
        return "U shot %d times and got %d hits"  % (self.bullets, counthits) # syntax, % in Klammer + syntax, %D
            
    
    def chill(self):
        return "Go home asshole! I wanna relax!!!"
    
    
    def dealing(self):    # Syntax self
        print("U need some dope?")
        return self.getBagofdope()
    
    
    def getBagofdope(self):
        return self._bagofdope  # Syntax .
    
    def setBagofdope(self, dope="20 g's of finest dope"):
        self._bagofdope = dope
    
    bagofdope = property(getBagofdope, setBagofdope) # Syntax None
    
    
    def party(self, chicks=20):
        if chicks < 20:  # Syntax
            return "go home I don't wanna party with u."
        else:
            return "let's get it on!!!!"
        
        

if __name__ == "__main__":
    G = Gangster()
    print(G.bagofdope)
    print(G.shootaguy())    # Semantischer Fehler
    littleG = Gangster(7, 9)
    print(littleG.shootaguy())
    print(littleG.dealing())
    print(littleG.party(10))


# In[ ]:



