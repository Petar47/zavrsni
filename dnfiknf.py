def provjera(x):
    if(x):
        return 1
    else:
        return 0

def dnfiknff(sud,atomi):
    dnff=""
    knff=""
    rez="("
    rezz="("
    for i in sud:
        """
        Iterira kroz listu i provjerava disjunktivnu i konjuktivnu normalnu formu 
        za svaki element.

        :parametar x: Lista za koje se generiraju DNF i KNF oblici
        :tip x: list
        """
        if(i[list(i)[-1]]):
            """
            Generira Disjunktivnu Normalnu Formu (DNF) iz dane liste `sud` 
            koji predstavlja logički izraz.

            :parametar sud: Lista koja predstavlja logički izraz
            :tip sud: dict
            :return: DNF oblik logičkog izraza
            :return tip: str
            """
            rez="("
            for j in range(atomi):
                if(provjera(i[list(i)[j]])):
                    rez+=str(list(i)[j])
                    rez+='\u2227'
                else:
                    rez+='\u00ac'
                    rez+=str(list(i)[j])
                    rez+='\u2227'       
            rez=rez.rstrip(rez[-1])
            dnff+=rez+")"
        else:
            """
            Generira Konjunktivnu Normalnu Formu (KNF) iz dane liste `sud` 
            koji predstavlja logički izraz.

            :parametar sud: Lista koja predstavlja logički izraz
            :tip sud: dict
            :return: KNF oblik logičkog izraza
            :return tip: str
            """
            rezz="("
            for j in range(atomi):
                if(provjera(i[list(i)[j]])):
                    rezz+=str(list(i)[j])
                    rezz+='\u2228'
                else:
                    rezz+='\u00ac'
                    rezz+=str(list(i)[j])
                    rezz+='\u2228'       
            rezz=rezz.rstrip(rezz[-1])
            knff+=rezz+")"
    return dnff,knff
