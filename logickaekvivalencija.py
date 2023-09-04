from semanticka import *
def logickaekvivalencija(sud,atomi,sudd,atomii):
    """
    Utvrđuje jesu li dvije logičke izjave ekvivalentne za zadane kombinacije atoma.

    Ova funkcija uzima dvije logičke izjave 'sud' i 'sudd', 
    zajedno s odgovarajućim skupovima atoma 'atomi' i 'atomii'. 
    Izračunava izjave za sve kombinacije atoma
    u odgovarajućim skupovima i provjerava jesu li rezultati ekvivalentni.

    :parametar sud: Prva logička izjava
    :tip sud: str
    :parametar atom: Broj atoma u prvoj logičkoj izjavi
    :tip atom: int
    :parametar sud: Druga logička izjava
    :tip sud: str
    :parametar atom: Broj atoma u drugoj logičkoj izjavi
    :tip atom: int
    :return: Vraća True ako su sudovi ekvivalentni; False ako nisu
    :return tip: bool
    """
    x=[]
    x2=[]
    for i,kombinacija in kombinacije(atomi).items():
        x.append(izrada(expr.parseString(sud)[0],kombinacija))
    for i,kombinacija in kombinacije(atomii).items():
        x2.append(izrada(expr.parseString(sudd)[0],kombinacija))
    for i,j in zip(x,x2):
        if(i[list(i)[-1]]!=j[list(j)[-1]]):
            return False
    return True
