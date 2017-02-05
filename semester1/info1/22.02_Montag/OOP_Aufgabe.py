# a) Erstellen Sie das Klassendiagramm +
#    MRO erstellen (bis man keinen Bock mehr hat)
# b) Nennen Sie 4 Typen von Methoden, die bei OOP eingesetzt werden können
#    und erklären Sie diese kurz
# c) Nennen Sie 3 Arten von magischen Methoden und bringen Sie jeweils 2 (1)
#    Beispiel.


# Zu a)
class A:
    something

class B(A):
    stuff

class G:
    stuff

class D:
    stuff

class C(A, G):
    stuff

class T(B):
    stuff

class F(C, D):
    stuff

class Z(T, F):


