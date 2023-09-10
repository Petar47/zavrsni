from semanticka import *
from dnfiknf import *
from logickaekvivalencija import *
from sympy import symbols, parse_expr
from sympy.logic import simplify_logic
from tabulate import tabulate
import argparse

parser = argparse.ArgumentParser(description='Python program s opcijama')
parser.add_argument('string', type=str, help='Ulazni string')
parser.add_argument('--opcija', type=str, help='Opcija za obradu', required=True)

args = parser.parse_args()

opcija = args.opcija
match opcija:
    case 's':
        x=[]
        atomi=len(parse_expr(args.string).free_symbols)
        for i,kombinacija in kombinacije(atomi).items():
            x.append(izrada(args.string,kombinacija))
        kljucevi = list(x[0].keys())
        tablica = [list(y.values()) for y in x]
        print(tabulate(tablica, headers=kljucevi, tablefmt='grid'))  
    case 'dnfiknf':
        x=[]
        atomi=len(parse_expr(args.string).free_symbols)
        for i,kombinacija in kombinacije(atomi).items():
            x.append(izrada(args.string,kombinacija))
        dnf,knf=dnfiknff(x,atomi)
        print("DNF: "+dnf)
        print("KNF: "+knf)
    case 'logekv':
        atomi=len(parse_expr(args.string).free_symbols)
        sudd=input("Napisite sud koristeći ~,&,|,>>,<->,() i slova A,B,C... sve odvojeno osim zagrada:")
        atomii=len(parse_expr(sudd).free_symbols)
        if(logickaekvivalencija(args.string,atomi,sudd,atomii)):
            print("Sudovi su logicki ekvivalentni")
        else:
            print("Sudovi nisu logicki ekvivalentni")
    case 'min':
        print(simplify_logic(args.string))
