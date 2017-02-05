class A(object):
    number = 1
    def __init__(self, text):
        self.text = text
        
    def printNumber(self):
        print(self.number)


class B (A):
    def __init__(self,text):
        super().__init__(text)
                
    def __str__(self):
        return "k" + self.text

    def __add__(self, other):
        return self.text + other.text

    def printNumber(self):
        self.number = 2
        print(B.number)

class C(A):
    def __init__(self, text, number = 3):
        self.number = 3 # siehe Aufgabe 3
        super().__init__(text)
        
    def printNumber(self):
        # self.number = 3 
        print(self.number)
        

class D(B,C):
    number = 4
    def __init__(self,text):
        super().__init__(text)

    def __add__(self,other):
        return other.text + " ist != alpha Nerd"
                
a = A("!")
b = B("ein Nerd")
c = C("Ne")
d = D("! ")

#1) Zeichne ein Klassendiagramm (Klassenhierachie und Methoden)







#2) Welche Ausgaben werden hier erzeugt?

a.printNumber()

b.printNumber()

c.printNumber()

d.printNumber()

print(b)

print(b+d)

print(d+b)

print(b+a)

print(a+b)



#3) Ändert sich die Ausgabe wenn man die Zeile "self.number = 3" in der init Methode auskommentiert
#   und stattdessen in die printNumber Methode der gleichen Klasse schreibt?



