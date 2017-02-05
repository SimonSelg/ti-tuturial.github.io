
# Ein Apha-Nerd-Kaffeautomat soll implementiert werden. Den Automaten soll man mit
# 10 ct (inp10) und 20ct (inp20) bezahlen können. An dem Automaten kann man sich
# ein kleinen Kaffee (reqKK) für 30 ct und einen Cappuccino Spezial XXL (reqCS)
# für 50 ct holen. Der Höchstkontostand am Automaten beträgt 60 ct. Der Rest-
# betrag bleibt wird nicht als Wechselgeld ausgegeben, sondern bleibt für den
# Nächsten.

# a) Malen Sie den zugeörigen Moore-Automaten

# b) Implementieren Sie den Automaten mit Python

def next_state(state, inp):
    """Calculate the successor state for a given state and input.

    Args:
      state (int): a natural number, representing the automaton's current state
      inp (string): a string representing the automaton's input

    Returns:
      int: a natural number, representing the automaton's successor state

    """
    pass  # TODO: replace by your implementation


def output(state):
    """Calculate the output in a given state.

    Args:
      state (int): a natural number, representing the automaton's current state

    Returns:
      string: the output of the automaton

    """
    pass  # TODO: replace by your implementation


def automaton():
    """Main loop of the automaton."""
    state = 0
    while True:
        state = next_state(state, input('> '))
        print(output(state))


if __name__ == '__main__':
    automaton()

# c) Schreiben Sie pro Funktion 2 Doctest
# d) Bauen Sie den Automaten, damit wir zukünftik Kaffee haben. Drohnenlieferung ist
# freiwillig zu Realisieren.
