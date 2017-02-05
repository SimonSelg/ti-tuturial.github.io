# Bestimme Groß O

def quicksort(liste):
    if len(liste) <= 1:
        return liste
    else:
        return quicksort(list(filter(lambda x: x < liste[0], liste[1:]))) + \
               [ liste[0] ] + \
               quicksort(list(filter(lambda x: x >= liste[0], liste[1:])))


print(quicksort([11,67,23,64,67,2,546,67]))

# Schreibe ein Programm rekusiv, dass x hoch n mit n Element der Natürlichen Zahlen berechnet.
# Bestimme ancshließend Groß O
