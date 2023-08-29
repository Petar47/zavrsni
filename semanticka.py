from pyparsing import *
from pyparsing import pyparsing_common as ppc
from sympy import *
import itertools

akcija = ppc.integer
atom = Word(alphas, exact=1)
operand = akcija | atom

ne = oneOf("~")
i = oneOf("&")
ili = oneOf("|")
imp = oneOf(">>")
ekv = oneOf("<->")

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
    letters = [chr(ord('A') + i) for i in range(atoms)]
    
    brojKombinacija = 2 ** atoms
    combinations_dict = {}
    
    for i, kombinacija in enumerate(itertools.product([False, True], repeat=atoms)):
        combination_dict = {letter: value for letter, value in zip(letters, kombinacija)}
        combinations_dict[i] = combination_dict
    
    return combinations_dict

def provjeraJedan(sud):
    if(len(sud)>1 and sud[1].isalpha()):
        return True
    return False

def provjeraDva(sud):
    if(len(sud)>2 and sud[2].isalpha()):
        return True
    return False

def izrada(sud,kombinacija):
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
    
