
# coding: utf-8

# # Shellausgabe

# Geben Sie an, was bei Folgenden Zeilen ausgegeben wird!

# In[1]:

list(map(lambda x: x**2, range(21)))


# In[10]:

a = [1, 4., 2, 5, 3, 6, 3.3]
list(filter(lambda x: isinstance(x, int),a))


# In[33]:

a = range(2,40)
e1 = {x*2 for x in range(2, 51)}
e2 = {x*3 for x in range(2, 34)}
e3 = {x*5 for x in range(2, 21)}
e4 = {x*7 for x in range(2, 15)}
e5 = {x*9 for x in range(2, 12)}
list(filter(lambda x: x not in e1 and x not in e2 and x not in e3 and x not in e4 and x not in e5, a))


# # Generatoren

# Welche Ausgabe erzeugt der Code?

# In[20]:

def gen1():
    x = 0
    while True:
        x += 2
        if x % 4 == 0:
            x -= 1
        yield x
        

def gen2():
    y = 0
    ge = gen1()
    while True:
        y += 3
        if y % 6 == 0:
            yield next(ge)
        else:
            yield y

            
gen = gen2()
li = []
for i in range(10):
    li.append(next(gen))
li


# # Programm

# In[32]:

def abs_sub(x, y):
    b = x >= y
    print(b)
    if b:
        return x-y
    if not b:
        return y-x

print(abs_sub(3,3))
print(abs_sub(2,3))

