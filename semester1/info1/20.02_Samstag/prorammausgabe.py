#Was geben die Print-Befehle aus?

var1 = "Ham"
var2 = "Egg"
var3 = ["Spam","Spam"]

def foo():
    global var1
    var1 = "HAM"
    var2 = "EGG"
    global var2
    var3[1] = var2

var4 = foo()

print(var1,var2,var3,var4,sep=", ")

var3 += ["Toast","Pizza"]
var1 = list
for a in var3[:]:
    if a == "Pizza":
        del var3[0]
var2 = var1 and var4
var4 = "Egg" and "Spam"
var5 = "Egg" or "Spam"

print(var1,var2,var3,var4,var5,sep=", ")
