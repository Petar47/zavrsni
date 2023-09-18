from semanticka_tablica import *
from dnfiknf import *
from logickaekvivalencija import *
from sympy import symbols, parse_expr, Eq
from sympy.logic import simplify_logic
from tabulate import tabulate
import click

@click.command()
@click.argument('izraz', required=True)
@click.option('-s', '--sem-tablica', is_flag=True, help='Semantička tablica')
@click.option('-d', '--dnf', is_flag=True, help='DNF')
@click.option('-k', '--knf', is_flag=True, help='KNF')
@click.option('--el-kon', is_flag=True, help='Elementarna konjukcija')
@click.option('--el-dis', is_flag=True, help='Elementarna disjunkcija')
@click.option('-t','--taut', is_flag=True, help='Tautologija')
@click.option('-l', '--logekv', is_flag=True, help='Logička ekvivalencija')
@click.option('-m', '--mini', is_flag=True, help='Minimizacija')
@click.option('--sve', is_flag=True, help='Sve')
def main(izraz, sem_tablica, dnf, knf, el_kon, el_dis, taut, logekv, mini, sve):
    if sem_tablica:
        tablica(izraz)
    if dnf:
        dnff(izraz)
    if knf:
        knff(izraz)
    if el_kon:
        elkon(izraz)
    if el_dis:
        eldis(izraz)
    if taut:
        tau(izraz)
    if mini:
        minimizacija(izraz)
    if sve:
        tablica(izraz)
        dnff(izraz)
        knff(izraz)
        elkon(izraz)
        eldis(izraz)
        tau(izraz)
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
def dnff(dnfiknf):
    x=[]
    atomi=provjeraAtoma(dnfiknf)
    for i,kombinacija in kombinacije(atomi).items():
        x.append(semanticka(dnfiknf,kombinacija))
    dnf,knf=dnfiknff(x,atomi)
    print("DNF: "+dnf)
    pass
def knff(dnfiknf):
    x=[]
    atomi=provjeraAtoma(dnfiknf)
    for i,kombinacija in kombinacije(atomi).items():
        x.append(semanticka(dnfiknf,kombinacija))
    dnf,knf=dnfiknff(x,atomi)
    print("KNF: "+knf)
    pass
def elkon(el):
    x=[]
    atomi=provjeraAtoma(el)
    for i,kombinacija in kombinacije(atomi).items():
        x.append(semanticka(el,kombinacija))
    dnf,knf=dnfiknff(x,atomi)
    kon=dnf.split("\u2228")
    print("Elementarna konjukcija:")
    for i in kon:
        print(i[1:-1])
def eldis(el):
    x=[]
    atomi=provjeraAtoma(el)
    for i,kombinacija in kombinacije(atomi).items():
        x.append(semanticka(el,kombinacija))
    dnf,knf=dnfiknff(x,atomi)
    kon=knf.split("\u2227")
    print("Elementarna disjunkcija:")
    for i in kon:
        print(i[1:-1])
def tau(s):
    x=[]
    atomi=provjeraAtoma(s)
    for i,kombinacija in kombinacije(atomi).items():
        x.append(semanticka(expr.parseString(s)[0],kombinacija))
    for i in x:
        if(i[list(i)[-1]]==False):
            print("Sud nije tautologija")
            return
    print("Sud je tautologija")
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
