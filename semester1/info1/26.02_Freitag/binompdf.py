def faculty(n):
    def gen():
        yield 1
        a, b = 1, 2
        while True:
            yield a
            a, b = a*b,b+1
    g = gen()
    dic = {}
    for i in range(n+1):
        dic[i] = next(g)
    return dic


def binompdf(n, k):
    facs = faculty(n)
    return facs[n]/(facs[n-k]*facs[k])


def calc_bin(op, n):
    s = ""
    c = 0
    while c != n+1:
        if c == 0:
            s += "x^"+str(n)
            if op == "+":
                s += "+"
            else:
                s += "-"
        elif c == n:
            s += "y^"+str(n)
        elif c != 0 or c != n:
            s += str(int(binompdf(n, c)))+"*"
            s += "x"
            if n-c > 1:
                s += "^"+str(n-c)
            s += "*y"
            if c > 1:
                s += "^"+str(c)
            if op == "-":
                if c % 2:
                    s += "+"
                else:
                    s += "-"
            if op == "+":
                s += "+"
        c += 1
    return s



            
