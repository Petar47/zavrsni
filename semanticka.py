from pyparsing import *
from pyparsing import pyparsing_common as ppc
from sympy import *
import itertools

#Definiranje operatora i operanata za izvedbu sintatičke analize logičkih izraza
akcija = ppc.integer
atom = Word(alphas, exact=1)
operand = akcija | atom

ne = oneOf("~")
i = oneOf("&")
ili = oneOf("|")
imp = oneOf(">>")
ekv = oneOf("<->")

#Definiranje gramatike za obradu sintatičke analize logički izraza
expr = infixNotation(
    operand,
    [
        (ne, 1, opAssoc.RIGHT),
        (i, 2, opAssoc.LEFT),
        (ili, 2, opAssoc.LEFT),
        (imp, 2, opAssoc.LEFT),
        (ekv, 2, opAssoc.LEFT),
    ],
)

def kombinacije(atoms):
    """
    Generira sve moguće kombinacije istinitosnih vrijednosti za zadani broj atomskih izraza.
    
    :parametar atoms: Broj atomskih izraza za koje se generiraju kombinacije
    :tip atoms: int
    :return: Rječnik koji mapira indekse na kombinacije istinitosnih vrijednosti
    :return tip: dict
    """
    letters = [chr(ord('A') + i) for i in range(atoms)]
    
    brojKombinacija = 2 ** atoms
    combinations_dict = {}
    
    for i, kombinacija in enumerate(itertools.product([False, True], repeat=atoms)):
        combination_dict = {letter: value for letter, value in zip(letters, kombinacija)}
        combinations_dict[i] = combination_dict
    
    return combinations_dict

def provjeraJedan(sud):
    """
    Provjerava je li drugi element suda `sud` slovo (alfanumerički karakter).
    :parametar sud: Varijabla koja se provjerava
    :tip sud: list ili str
    :return: True ako je drugi element slovo, inače False
    :return tip: bool
    """
    if(len(sud)>1 and sud[1].isalpha()):
        return True
    return False

def provjeraDva(sud):
    """
    Provjerava je li drugi element suda `sud` slovo (alfanumerički karakter).
    :parametar sud: Varijabla koja se provjerava
    :tip sud: list ili str
    :return: True ako je drugi element slovo, inače False
    :return tip: bool
    """
    if(len(sud)>2 and sud[2].isalpha()):
        return True
    return False

def izrada(sud,kombinacija):
    """
    Rekurzivno prolazi strukturu liste/sintatičke analize `sud` 
    i primjenjuje funkciju `izrada`.

    :parametar sud: Sud u obliku sintatičke analize
    :tip sud: list ili ParseResults
    :parametar kombinacija: Kombinacije True/False atoma i sudova.
    :tip kombinacija: dict
    """
    if sud[0]==[]:
        del sud[0]
    if(isinstance(sud[0],ParseResults)):
        izrada(sud[0],kombinacija)
        del sud[0]
    if(len(sud)>1 and isinstance(sud[1],ParseResults)):
        izrada(sud[1],kombinacija)
        del sud[1]
    if(len(sud)>2 and isinstance(sud[2],ParseResults)):
        izrada(sud[2],kombinacija)
        del sud[2]
    match sud[0]:
        """
        Prima listu `sud` i primjenjuje odgovarajuće logičke operacije na kombinacije 
        iz `kombinacija`. Varijabla z predstavlja zadnji obrađeni sud, 
        varijabla pz predstavlja predzadnji obrađeni sud.
        
        :parametar sud: Sud u obliku liste
        :tip sud: list
        :parametar kombinacija: Kombinacije True/False atoma i sudova.
        :tip kombinacija: dict
        """
        case '~':
            z = list(kombinacija)[-1]
            if(provjeraJedan(sud)):
                x=Not(kombinacija[sud[1]])
                kombinacija["~"+sud[1]] = x
            else:
                x=Not(kombinacija[z])
                kombinacija["~"+str(kombinacija[z])] = x
            
        case '|':
            z = list(kombinacija)[-1]
            if(provjeraJedan(sud)):
                x=Or(kombinacija[z],kombinacija[sud[1]])
                kombinacija[str(kombinacija[z])+"|"+sud[1]]=x
            else:
                pz = list(kombinacija)[-2]
                x=Or(kombinacija[pz],kombinacija[z])
                kombinacija[str(kombinacija[pz])+"|"+str(kombinacija[z])]=x
            
        case '&':
            z = list(kombinacija)[-1]
            if(provjeraJedan(sud)):
                x=And(kombinacija[z],kombinacija[sud[1]])
                kombinacija[str(kombinacija[z])+"&"+sud[1]]=x
            else:
                pz = list(kombinacija)[-2]
                x=And(kombinacija[pz],kombinacija[z])
                kombinacija[str(kombinacija[pz])+"&"+str(kombinacija[z])]=x

        case '>>':
            z = list(kombinacija)[-1]
            if(provjeraJedan(sud)):
                x=Implies(kombinacija[z],kombinacija[sud[1]])
                kombinacija[str(kombinacija[z])+">>"+sud[1]]=x
            else:
                pz = list(kombinacija)[-2]
                x=Implies(kombinacija[pz],kombinacija[z])
                kombinacija[str(kombinacija[pz])+">>"+str(kombinacija[z])]=x

        case '<->':
            z = list(kombinacija)[-1]
            if(provjeraJedan(sud)):
                x=Equivalent(kombinacija[z],kombinacija[sud[1]])
                kombinacija[str(kombinacija[z])+"<->"+sud[1]]=x
            else:
                pz = list(kombinacija)[-2]
                x=Equivalent(kombinacija[pz],kombinacija[z])
                kombinacija[str(kombinacija[pz])+"<->"+str(kombinacija[z])]=x
    if(len(sud)>=2):
        match sud[1]:
            """
            Prima listu `sud` i primjenjuje odgovarajuće logičke operacije na kombinacije 
            iz `kombinacija`. Varijabla z predstavlja zadnji obrađeni sud, 
            varijabla pz predstavlja predzadnji obrađeni sud. 
            Ovo ide u slučaju da se drugi element liste treba obraditi.
            
            :parametar sud: Sud u obliku liste
            :tip sud: list
            :parametar kombinacija: Kombinacije True/False atoma i sudova.
            :tip kombinacija: dict
            """
            case '|':
                z = list(kombinacija)[-1]
                if(provjeraDva(sud)):
                    x=Or(kombinacija[sud[0]],kombinacija[sud[2]])
                    kombinacija[sud[0]+"|"+sud[2]]=x
                else:
                    x=Or(kombinacija[sud[0]],kombinacija[z])
                    kombinacija[sud[0]+"|"+str(kombinacija[z])]=x

            case '&':
                z = list(kombinacija)[-1]
                if(provjeraDva(sud)):
                    x=And(kombinacija[sud[0]],kombinacija[sud[2]])
                    kombinacija[sud[0]+"&"+sud[2]]=x
                else:
                    x=And(kombinacija[sud[0]],kombinacija[z])
                    kombinacija[sud[0]+"&"+str(kombinacija[z])]=x

            case '>>':
                z = list(kombinacija)[-1]
                if(provjeraDva(sud)):
                    x=Implies(kombinacija[sud[0]],kombinacija[sud[2]])
                    kombinacija[sud[0]+">>"+sud[2]]=x
                else:
                    x=Implies(kombinacija[sud[0]],kombinacija[z])
                    kombinacija[sud[0]+">>"+str(kombinacija[z])]=x

            case '<->':
                z = list(kombinacija)[-1]
                if(provjeraDva(sud)):
                    x=Equivalent(kombinacija[sud[0]],kombinacija[sud[2]])
                    kombinacija[sud[0]+"<->"+sud[2]]=x
                else:
                    x=Equivalent(kombinacija[sud[0]],kombinacija[z])
                    kombinacija[sud[0]+"<->"+str(kombinacija[z])]=x
    return kombinacija
    
