
# coding: utf-8

# In[18]:

class Gangster:
    def __init__(self, gunshothits=28, bullets=6, bagofdope="20 g's of finest dope"):
        self.gunshothits = gunshothits
        self.bullets = 3
        self.bagofdope = bagofdope
        

    def shootaguy(self):
        counthits = 0
        for shot in range(self.bullets):
            if shot / 2 == 0:
                print("Killer!!!")
                counthit += 1
            else:
                print("shoot again!!!")
        return "U shot %D times and got %d hits" (%self.bullets, counthits)
            
    
    def chill(self):
        return "Go home asshole! I wanna relax!!!"
    
    
    def dealing():
        print("U need some dope?")
        return self.getBagofdope()
    
    
    def getBagofdope(self):
        return self_bagofdope
    
    def setBagofdope(self, dope="20 g's of finest dope"):
        self_bagofdope = dope
    
    bagofdope = property(None, setBagofdope)
    
    
    def party(self, chicks=20):
        if chicks < 20
            return "go home I don't wanna party with u."
        else:
            return "let's get it on!!!!"
        
        

if __name__ == "__main__":
    G = Gangster()
    print(G.bagofdope)
    print(G.shootaguy)
    littleG = Gangster(7, 9)
    print(littleG.shootaguy())
    print(littleG.dealing())
    print(littleG.party(10))

        


# In[ ]:



