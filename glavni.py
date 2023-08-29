from semanticka import *
from dnfiknf import *
from sympy.logic import simplify_logic

izbor=int(input("1. Semantička tablica, DNF i KNF\n2. Logička jednakost sudova\n3. Minimizacija "))

atomi=int(input("Koliko atoma ima sud?:"))
sud=input("Napisite sud koristeći ~,&,|,>>,<->,() i slova A,B,C... sve odvojeno osim zagrada:")

x=[]
if(izbor==1):
    for i,kombinacija in kombinacije(atomi).items():
        x.append(izrada(expr.parseString(sud)[0],kombinacija))
    dnff=""
    knff=""
    for i in x:
        print(i)
        if(i[list(i)[-1]]):
            dnff += dnf(i, atomi) + '|'
        else:
            knff += knf(i, atomi) + '&'
    dnff=dnff[:-1]
    knff=knff[:-1]
    print("DNF: ")
    print(dnff)
    print("KNF: ")
    print(knff)
elif(izbor==2):
    a=1
    atomii=int(input("Koliko atoma ima sud?:"))
    sudd=input("Napisite sud koristeći ~,&,|,>>,<->,() i slova A,B,C... sve odvojeno osim zagrada:")
    x2=[]
    for i,kombinacija in kombinacije(atomi).items():
        x.append(izrada(expr.parseString(sud)[0],kombinacija))
    for i,kombinacija in kombinacije(atomii).items():
        x2.append(izrada(expr.parseString(sudd)[0],kombinacija))
    for i,j in zip(x,x2):
        if(i[list(i)[-1]]!=j[list(j)[-1]]):
            print("Sudovi nisu jednaki")
            a=0
            break
    if(a==1):
        print("Sudovi su jednaki")
elif(izbor==3):
    print(simplify_logic(sud))
    

