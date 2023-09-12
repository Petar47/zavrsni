from semanticka import *
from dnfiknf import *
from logickaekvivalencija import *
from sympy import symbols, parse_expr
from sympy.logic import simplify_logic
from tabulate import tabulate
import click

@click.command()
@click.option('--s', help='Semantička tablica')
@click.option('--dnfiknf', help='DNF i KNF')
@click.option('--logekv', help='Logička ekvivalencija')
@click.option('--mini', help='Minimizacija')
@click.option('--sve', help='Sve')

def main(s, dnfiknf, logekv, mini, sve):
    if s:
        sem(s)
    if dnfiknf:
        dnfiiknf(dnfiknf)
    if logekv:
        ekvivalencija(logekv)
    if mini:
        minimizacija(mini)
    if sve:
        sem(sve)
        dnfiiknf(sve)
        minimizacija(sve)
def sem(s):
    x=[]
    atomi=len(parse_expr(s).free_symbols)
    for i,kombinacija in kombinacije(atomi).items():
        x.append(izrada(expr.parseString(s)[0],kombinacija))
    kljucevi = list(x[0].keys())
    tablica = [list(y.values()) for y in x]
    print(tabulate(tablica, headers=kljucevi, tablefmt='grid'))
    pass
def dnfiiknf(dnfiknf):
    x=[]
    atomi=len(parse_expr(dnfiknf).free_symbols)
    for i,kombinacija in kombinacije(atomi).items():
        x.append(izrada(dnfiknf,kombinacija))
    dnf,knf=dnfiknff(x,atomi)
    print("DNF: "+dnf)
    print("KNF: "+knf)
    pass
def ekvivalencija(logekv):
    sud=logekv.split("==")
    atomi=len(parse_expr(sud[0]).free_symbols)
    atomii=len(parse_expr(sud[1]).free_symbols)
    if(logickaekvivalencija(sud[0],atomi,sud[1],atomii)):
        print("Sudovi su logicki ekvivalentni")
    else:
        print("Sudovi nisu logicki ekvivalentni")
    pass
def minimizacija(mini):
    print(simplify_logic(mini))
    pass
if __name__ == '__main__':
    main()
