def provjera(x):
    if(x):
        return 1
    else:
        return 0

def dnf(sud,atomi):
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
