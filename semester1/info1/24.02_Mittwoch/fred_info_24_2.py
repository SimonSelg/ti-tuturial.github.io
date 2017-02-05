""" In einer Datingplattform geben alle Mitglieder
eine Liste mit zwei Leidenschaften / Hobbies an,
wobei ausgewählt werden kann zwischen:
I`m just horny
Sex
Pain
Big butts
Read

Außerdem wird das Geschlecht (m/w) angegeben.

Tritt ein neues Mitglied der Datingplattform bei wird zunächst
anhand der Leidenschaften ausgewählt, wer ein potentieller,
andersgeschlechtlicher Datingpartner für das Mitglied wäre.
Für ein match reicht bereits eine Übereinstimmung der
Leidenschaften aus.

Aufgabe a):
Mit wem matcht das neue Mitglied (newavenger), wenn die Mitglieder
members bereits auf der Plattform aggieren (dh. welche Elemente enthält die
Variable z im return statement)?

members = [("Daniel", "m", "4", "3"), ("Julia", "w", "2", "5"),
           ("Danny", "m", "3", "3"), ("Feli", "w", "1", "4"),
           ("Pano", "m", "2", "4"), ("Johanna", "w", "5", "4"),
           ("Simon", "m", "3", "5")]

newavenger = ["Freeeed", "m", "Big butts", "Pain"]

Aufgabe b)
Laufzeit? In O-Notation, wenn ich das noch machen will....
"""



def dating_friends(newavenger, members):
    y = dict((x[0], list(x[1:])) for x in members)
    for b in legend.keys():
        for a in newavenger: 
            if a == b:
                newavenger[newavenger.index(a)] = legend[b]
            else:
                continue
    z = []
    for element in y.keys():
        sli = y[element][1:]
        for item in sli:
            slo = newavenger[2:]
            for num in slo:
                if int(item)*int(item) == int(num):
                    if newavenger[1] != y[element][0]:
                        z.append(element)
    return z
     
    








members = [("Daniel", "m", "4", "3"), ("Julia", "w", "2", "5"),
           ("Danny", "m", "3", "3"), ("Feli", "w", "1", "4"),
           ("Pano", "m", "2", "4"), ("Johanna", "w", "5", "4"),
           ("Simon", "m", "3", "5")]


newavenger = ["Freeeed", "m", "Big butts", "Pain"]


legend = {"I'm just horney": "1", "Sex": "4", "Pain": "9", "Big butts": "16",
          "Reading": "25"}
