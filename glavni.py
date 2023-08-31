from semanticka import *
from dnfiknf import *
from logickaekvivalencija import *
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
        """
        Iterira kroz listu i provjerava disjunktivnu i konjuktivnu normalnu formu 
        za svaki element.
    
        :parametar x: Lista za koje se generiraju DNF i KNF oblici
        :tip x: list
        """
        print(i)
        if(i[list(i)[-1]]):
            dnff += dnf(i, atomi) + '|'
        else:
            knff += knf(i, atomi) + '&'
    print("DNF: "+dnff[:-1])
    print("KNF: "+knff[:-1])
elif(izbor==2):
    atomii=int(input("Koliko atoma ima sud?:"))
    sudd=input("Napisite sud koristeći ~,&,|,>>,<->,() i slova A,B,C... sve odvojeno osim zagrada:")
    if(logickaekvivalencija(sud,atomi,sudd,atomii)):
        print("Sudovi su logicki ekvivalentni")
    else:
        print("Sudovi nisu logicki ekvivalentni")
elif(izbor==3):
    print(simplify_logic(sud))
    

