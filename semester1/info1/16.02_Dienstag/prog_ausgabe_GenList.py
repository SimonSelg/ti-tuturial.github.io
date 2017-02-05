""" Die Firma Nerdsnerdsnerds produziert Lebensmittel für Nerds und hat dazu ein Python Programm geschrieben, das
diese für ihre internen Angelegenheiten beschriftet.

Die Beschriftung besteht aus dem verschlüsselten Namen des Klienten, sowie eine Kennzahl die mittels sehr sinnvolen
Vorschriften generiert wird.
"""

import itertools as it


def ticketnamer(orders, spec=False):
    id_module = id_generator(spec)
    enc_clients = dict((compute_id(x[1], id_module), encrypt_name(x[0])) for x in orders)
    return enc_clients


def id_generator(spc):
    i = 0
    while True:
        i += 1
        yield i
        if spc:
            yield i + spc


def compute_id(ticket, id_maker):
    catalogue = {"Alkohol": 1, "Pizza": 2, "Fleischkaese": 3}
    return catalogue[ticket] + next(id_maker)


def encrypt_name(name):
    gen_letter = it.cycle(['Best', 'Encryption', 'Ever'])
    build_enc = ''
    for i in range(0, len(name)):
        if i % 2:
            build_enc += next(gen_letter)
        else:
            build_enc += name[i]
    return build_enc


# Aufgabe: Welche Ausgabe erzeugt der Print-Befehl?

<<<<<<< HEAD
ords = [("Ritterchen", "Alkohol"), ("Lappen", "Pizza"), ("Lappen",
                                                         "Fleischkaese")]
=======
ords = [("Ritterchen", "Alkohol"), ("Lappen", "Pizza"), ("Lappen", "Fleischkaese")]
>>>>>>> 59e6b463e143b924771d1be38d757132aa3e7086
print(ticketnamer(ords, 5))
