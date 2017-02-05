Aufgabe 1:
----------
>>> [[x*2 for x in range(y*3, y*3 + 3)] for y in range(8)]


Aufgabe 2:
----------
>>> [dict((x,y)for x in range(1, 11) for y in ['Monty', 'Python'])]


Aufgabe 3:
----------
>>> reduce(lambda x, y: x*y, range(1, 5))


Aufgabe 4:
----------
def test(f):
    def Monty(python):
        print('Monty Python wird ausgeführt')
        print(python * 2)
        t = f(python)
        return t
    return Monty
        
@test
def Spam(v):
    b = str(v)
    print('Spam wird ausgeführt')
    a = dict((x , b) for x in range(1, len(b)+1))
    print(a)
    print(v + ' ' + 'of Bryan')
    return True

Spam('Life')



Lösungen:
=========

Aufgabe 1:
----------
[[0, 2, 4], [6, 8, 10], [12, 14, 16], [18, 20, 22], [24, 26, 28], [30, 32, 34], 
[36, 38, 40], [42, 44, 46]]

Aufgabe 2:
----------
[{1: 'Python', 2: 'Python', 3: 'Python', 4: 'Python', 5: 'Python', 6: 'Python', 
7: 'Python', 8: 'Python', 9: 'Python', 10: 'Python'}]

Aufgabe 3:
---------
24

Aufgabe 4:
----------
Monty Python wird ausgeführt
LifeLife
Spam wird ausgeführt
{1: 'Life', 2: 'Life', 3: 'Life', 4: 'Life'}
Life of Bryan
