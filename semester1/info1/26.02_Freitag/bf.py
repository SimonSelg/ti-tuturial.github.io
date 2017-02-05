"""Eine Gruppe von Nerds erweiterte die Brainfuck
syntax. Welche Ausgabe erscheint nun bei diesem
Funktionsaufruf?

bf("+{>+++++x---+++++++++++++X.+++++++++++++.}
>{++++++++[>++++++++++<-]>.}", "")

"""


##########################################
### Main Interpreter functionality
##########################################

class BFError(Exception):
    pass


def bf(bfprog="", inp=""):
    """ brainfuck main interpreter function, reads program
        and calls interpreter
        Arguments:
        bfprog - the program text

    """
    try:
        bfinterpret(bfprog, inp)
    except BFError as e:
        print("Abbruch wegen BF-Fehler:", e)
    except Exception as e:
        print("Interner Interpreter-Fehler:", e)
    else:
        print("\n <BF-Programmausfuehrung regulaer beendet>")


def bfinterpret(srctext, inp):
    """BF interpreter main loop

    Arguments:
    srctext - the BF source
    inp - user input
    """
    pc = 0  # Programm counter, current state in srctext
    ptr = 0  # Current brainfuck cell
    data = dict()  # {ptr: current bf value}
    inp = list(inp)
    while pc < len(srctext):
        # See instruction dictionary at bottom
        (pc, ptr) = instr.get(srctext[pc], noop)(pc, ptr,
                                                 srctext, data, inp)
        pc += 1


##########################################
### Brainfuck standart syntax:
##########################################

def noop(pc, ptr, src, data, inp):
    return pc, ptr


def left(pc, ptr, src, data, inp):
    return pc, ptr - 1


def right(pc, ptr, src, data, inp):
    return pc, ptr + 1


def incr(pc, ptr, src, data, inp):
    data[ptr] = data.get(ptr, 0) + 1
    return pc, ptr


def decr(pc, ptr, src, data, inp):
    data[ptr] = data.get(ptr, 0) - 1
    return pc, ptr


def beginloop(pc, ptr, src, data, inp):
    if data.get(ptr, 0):
        return pc, ptr
    loop = 1
    while loop > 0:
        pc += 1
        if pc >= len(src):
            raise BFError("Kein ']' gefunden")
        if src[pc] == ']':
            loop -= 1
        elif src[pc] == '[':
            loop += 1
    return pc, ptr


def endloop(pc, ptr, src, data, inp):
    loop = 1
    while loop > 0:
        pc -= 1
        if pc < 0:
            raise BFError("Kein '[' gefunden")
        if src[pc] == ']':
            loop += 1
        elif src[pc] == '[':
            loop -= 1
    return pc - 1, ptr


def ch_in(pc, ptr, src, data, inp):
    if inp:
        data[ptr] = ord(inp[0])
        del inp[0]
        if data[ptr] > 127:
            raise BFError("Non-ASCII-Zeichen gelesen")
    return pc, ptr


def ch_out(pc, ptr, src, data, inp):
    if not 0 <= data.get(ptr, 0) <= 127:
        BFError("Ausgabe eines Non-ASCII-Zeichen")
    print(chr(data.get(ptr, 0)), end='', flush=True)
    return pc, ptr


##########################################
### New Brainfuck Syntax: the AN-Brainfuck
##########################################

def beginsmth(pc, ptr, src, data, inp):
    if data.get(ptr, 0) != 0:
        return pc, ptr
    else:
        num = 1
        while num > 0:
            pc += 1
            if pc >= len(src):
                raise BFError("Kein '}' gefunden")
            if src[pc] == '}':
                num -= 1
            elif src[pc] == '{':
                num += 1
        return pc, ptr


def endsmth(pc, ptr, src, data, inp):
    return pc, ptr


def beginsmth2(pc, ptr, src, data, inp):
    cur_value = data.get(ptr, 0)
    new_value = 0
    pc += 1
    while src[pc] != 'X':
        if pc >= len(src):
            raise BFError("Kein 'X' gefunden")
        if src[pc] == "+":
            new_value += cur_value
        elif src[pc] == "-":
            new_value = 0
        else:
            raise BFError("U done goofed!")
        pc += 1
    data[ptr] = new_value
    return pc, ptr


def endsmth2(pc, ptr, src, data, inp):
    return pc, ptr


# Instruction dictionary
instr = {'<': left, '>': right, '+': incr, '-': decr,
         '.': ch_out, ',': ch_in, '[': beginloop, ']': endloop,
         '{': beginsmth, '}': endsmth, 'x': beginsmth2, 'X': endsmth2}


# Check Solution
bf("+{>+++++x---+++++++++++++X.+++++++++++++.}>{++++++++[>++++++++++<-]>.}", "")