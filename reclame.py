from algemene_functies import mijn_functie_2

def aanbieding_1(smaak,prijs,korting):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro"
    return uitvoer

print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten,btw):
    totaal = 0 
    for nr in inkomsten:    
        totaal += nr 
    bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."

inkomsten = [220, 430, 125, 160, 205, 90, 345]

btw = 0.09

print(inkomsten_totaal(inkomsten,btw))

def laag_en_hoog(mijn_lijst):
    minimaal = min(mijn_lijst)
    maximaal = max(mijn_lijst)
    nieuwe_lijst = [minimaal, maximaal]
    return nieuwe_lijst

def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {totaal} euro."

def meervoudig(invoer_lijst):
    uitvoer = laag_en_hoog(invoer_lijst)
    return uitvoer

mijn_lijst = [220, 430, 125, 160, 205, 90, 345]

bijvoorbeeld = [10,5,3,2,1,2,9]

print(laag_en_hoog(mijn_lijst))

print(gemiddelde(mijn_lijst))

print(meervoudig(bijvoorbeeld))

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

print(combinatie(bijvoorbeeld))