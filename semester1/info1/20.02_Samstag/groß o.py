# Bestimme die Größenordung der Funktionen in Abängigkeit der übergebenen Argumente
#1)
def summe(n):
    if n== 0:
        return 0
    else:
        return n + summe(n-1)

#2)
def length(lst):
    if lst == []:
        return 0
    else:
        return 1+ length(lst[1:])

#3)
def list1(n):
    return([(x+y//z, x+y) for x in range(n) for y in range(0,5) for z in range(1,n)])

#4)
def bin_search(el, sli):
    left, right = 0, len(sli) - 1
    while left <= right:
        mid = (left+right)//2
        if sli[mid] < el:
            left = mid + 1
        elif sli[mid] > el:
            right = mid - 1
        else:
            return True
    return False

#5)
def dictactu(newelement, li, dic):
    newdict = {}
    if newelement in li:
        if newelement not in dic:
            dic[newelement] = 2 * newelement
    return dic

#6)
def setactu (newelement, li, se):
    newdict = set()
    if newelement in li:
        if newelement not in se:
            se.add(newelement)
    return se

