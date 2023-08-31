def provjera(x):
    if(x):
        return 1
    else:
        return 0

def dnf(sud,atomi):
    """
    Generira Disjunktivnu Normalnu Formu (DNF) iz dane liste `sud` 
    koji predstavlja logički izraz.

    :parametar sud: Lista koja predstavlja logički izraz
    :tip sud: dict
    :return: DNF oblik logičkog izraza
    :return tip: str
    """
    rez="("
    for i in range(atomi):
        if(provjera(sud[list(sud)[i]])):
            rez+=str(list(sud)[i])
            rez+='&'
        else:
            rez+='~'
            rez+=str(list(sud)[i])
            rez+='&'       
    rez=rez.rstrip(rez[-1])
    rez+=")"
    return rez

def knf(sud,atomi):
    """
    Generira Konjunktivnu Normalnu Formu (KNF) iz dane liste `sud` 
    koji predstavlja logički izraz.

    :parametar sud: Lista koja predstavlja logički izraz
    :tip sud: dict
    :return: KNF oblik logičkog izraza
    :return tip: str
    """
    rez="("
    for i in range(atomi):
        if(provjera(sud[list(sud)[i]])):
            rez+=str(list(sud)[i])
            rez+='|'
        else:
            rez+='~'
            rez+=str(list(sud)[i])
            rez+='|'       
    rez=rez.rstrip(rez[-1])
    rez+=")"
    return rez
