from semanticka import *
from dnfiknf import *
from logickaekvivalencija import *
from sympy import symbols, parse_expr
from sympy.logic import simplify_logic
from tabulate import tabulate

izbor=int(input("1. Semantička tablica, DNF i KNF\n2. Logička jednakost sudova\n3. Minimizacija "))

sud=input("Napisite sud koristeći ~,&,|,>>,<->,() i slova A,B,C... sve odvojeno osim zagrada:")
atomi=len(parse_expr(sud).free_symbols)
x=[]
if(izbor==1):
    for i,kombinacija in kombinacije(atomi).items():
        x.append(izrada(expr.parseString(sud)[0],kombinacija))
    kljucevi = list(x[0].keys())
    tablica = [list(y.values()) for y in x]
    dnf,knf=dnfiknff(x,atomi)
    print(tabulate(tablica, headers=kljucevi, tablefmt='grid'))
    print("DNF: "+dnf)
    print("KNF: "+knf)
elif(izbor==2):
    sudd=input("Napisite sud koristeći ~,&,|,>>,<->,() i slova A,B,C... sve odvojeno osim zagrada:")
    atomii=len(parse_expr(sudd).free_symbols)
    if(logickaekvivalencija(sud,atomi,sudd,atomii)):
        print("Sudovi su logicki ekvivalentni")
    else:
        print("Sudovi nisu logicki ekvivalentni")
elif(izbor==3):
    print(simplify_logic(sud))
