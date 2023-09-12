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
        """
        U ovom slučaju program čita string koji korisnik unosi i obrađuje 
        funkciju izrada za taj sud.
        
        :parametar sud: sud kojeg obrađujemo
        :tip sud: string
        :parametar atomi: broj atoma u sudu
        :tip atomi: int
        Rezultat:
        Tablica u formatu mreže koja prikazuje kombinacije ulaznog niza.
        """
        x=[]
        atomi=len(parse_expr(args.string).free_symbols)
        for i,kombinacija in kombinacije(atomi).items():
            x.append(izrada(args.string,kombinacija))
        kljucevi = list(x[0].keys())
        tablica = [list(y.values()) for y in x]
        print(tabulate(tablica, headers=kljucevi, tablefmt='grid'))  
    case 'dnfiknf':
        """
        U ovom slučaju program čita string koji korisnik unosi i obrađuje 
        funkciju dnfiknf za taj sud.
        
        :parametar sud: sud kojeg obrađujemo
        :tip sud: string
        :parametar atomi: broj atoma u sudu
        :tip atomi: int
        Rezultat:
        DNF i KNF suda
        """
        x=[]
        atomi=len(parse_expr(args.string).free_symbols)
        for i,kombinacija in kombinacije(atomi).items():
            x.append(izrada(args.string,kombinacija))
        dnf,knf=dnfiknff(x,atomi)
        print("DNF: "+dnf)
        print("KNF: "+knf)
    case 'logekv':
        """
        U ovom slučaju program čita string koji korisnik unosi, odvaja sudove, zatim obrađuje funkciju logickaekvivalencija za taj sud.
        
        :parametar sud: dva suda koja uspoređujemo
        :tip sud: niz
        :parametar atomi: broj atoma u prvom sudu
        :tip atomi: int
        :parametar atomii: broj atoma u drugom sudu
        :tip atomii: int
        Rezultat:
        Logička ekvivalencija suda
        """
        sud=args.string.split("==")
        atomi=len(parse_expr(sud[0]).free_symbols)
        atomii=len(parse_expr(sud[1]).free_symbols)
        if(logickaekvivalencija(sud[0],atomi,sud[1],atomii)):
            print("Sudovi su logicki ekvivalentni")
        else:
            print("Sudovi nisu logicki ekvivalentni")
    case 'min':
        """
        U ovom slučaju program čita string koji korisnik unosi i pomoću sympy 
        radi minimzaciju za taj sud.
        
        :parametar sud: sud
        :tip sud: string
        Rezultat:
        Minimizacija suda
        """
        print(simplify_logic(args.string))
