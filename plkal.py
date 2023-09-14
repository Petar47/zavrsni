from semanticka_tablica import *
from dnfiknf import *
from logickaekvivalencija import *
from sympy import symbols, parse_expr, Eq
from sympy.logic import simplify_logic
from tabulate import tabulate
import click

@click.command()
@click.argument('izraz', required=True)
@click.option('-s', '--sem', is_flag=True, help='Semantička tablica')
@click.option('-d', '--dnfiknf', is_flag=True, help='DNF i KNF')
@click.option('-l', '--logekv', is_flag=True, help='Logička ekvivalencija')
@click.option('-m', '--mini', is_flag=True, help='Minimizacija')
@click.option('--sve', is_flag=True, help='Sve')

def main(izraz, sem, dnfiknf, logekv, mini, sve):
    if sem:
        tablica(izraz)
    if dnfiknf:
        dnfiiknf(izraz)
    if logekv:
        ekvivalencija(izraz)
    if mini:
        minimizacija(izraz)
    if sve:
        tablica(izraz)
        dnfiiknf(izraz)
        if izraz.find("<->") != -1:
           ekvivalencija(izraz)
        minimizacija(izraz)
        
def provjeraAtoma(izraz):
    atomi=set()
    for slovo in izraz:
        if slovo.isalpha():
            atomi.add(slovo)
    return len(atomi)

def tablica(s):
    x=[]
    atomi=provjeraAtoma(s)
    for i,kombinacija in kombinacije(atomi).items():
        x.append(semanticka(expr.parseString(s)[0],kombinacija))
    kljucevi = list(x[0].keys())
    tablica = [list(y.values()) for y in x]
    print(tabulate(tablica, headers=kljucevi, tablefmt='grid'))
    pass
def dnfiiknf(dnfiknf):
    x=[]
    atomi=provjeraAtoma(dnfiknf)
    for i,kombinacija in kombinacije(atomi).items():
        x.append(semanticka(dnfiknf,kombinacija))
    dnf,knf=dnfiknff(x,atomi)
    print("DNF: "+dnf)
    print("KNF: "+knf)
    pass
def ekvivalencija(logekv):
    sud=logekv.split("<->")
    atomi=provjeraAtoma(sud[0])
    atomii=provjeraAtoma(sud[1])
    if(logicka_ekvivalencija(sud[0],atomi,sud[1],atomii)):
        print("Sudovi su logicki ekvivalentni")
    else:
        print("Sudovi nisu logicki ekvivalentni")
    pass
def minimizacija(mini):
    if mini.find("<->") != -1:
        mini=mini.split("<->")
        print(simplify_logic(mini[0]))
        print(simplify_logic(mini[1]))
    else:
        print(simplify_logic(mini))
    pass
if __name__ == '__main__':
    main()
