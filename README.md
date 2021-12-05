Cílem projektu Elections Scraper je napsat skript, který z odkazu 'https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ' vyhledá 
výsledky voleb 2017 pro jednotlivé obce dle zadaného územního celku. Výsledky uloží do souboru formátu csv.

Skript je spouštěn z příkazového řádku a očekává 2 parametry:
1. Název územního celku např. Znojmo
2. Název výstupního souboru

Příklad spůštění
C:\Users>C:\Python\Python C:\Python\Project\volby_2017 Znojmo vysledky_Znojmo.csv (tedy Python.exe je v adresáří C:\Python\ a soubor bude uložen do C:\Users)

Skript používá následující moduly:
csv
requests
bs4

Pro vývoj skriptu byl použit PYCharm a moduly do vývojového prostředí byly instalovány v tomto prostředí volbou
View - Tool Windows - Python Packages.

Výstupní csv soubor obsanuje následující informace (= header csv), výsledky jednotlivých stran jsou v %
1. část Kód obce,Název obce,Voliči v seznamu,Vydané obálky,Platné hlasy, + 2. část
2. část seznam stran kandidujících v daném uzemním celku např. Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI, atd.

Ukázka pro uzemní celek Znojmo
Kód obce,Název obce,Voliči v seznamu,Vydané obálky,Platné hlasy,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů,Národ Sobě
593729,Bantice,228,153,151,"5,29","0,00","0,00","8,60","0,00","2,64","7,94","2,64","2,64","2,64","0,00","0,00","5,96","0,00","0,66","22,51","0,00","0,00","21,19","0,00","0,00","0,00","0,66","15,23","0,66","0,66"
593737,Běhařovice,318,209,208,"2,40","0,00","0,00","9,61","0,48","1,44","7,69","0,48","0,96","0,00","0,00","0,48","5,76","0,00","0,00","48,55","0,00","0,00","13,46","0,00","0,00","0,00","0,48","8,17","0,00","0,00"
593745,Bezkov,157,110,110,"0,00","0,00","0,00","8,18","0,00","3,63","10,90","1,81","0,90","2,72","0,00","0,00","5,45","0,00","5,45","22,72","0,00","0,00","23,63","0,00","0,00","0,00","0,00","12,72","1,81","0,00"
593753,Bítov,141,109,107,"14,01","0,00","0,00","7,47","0,00","6,54","16,82","0,93","2,80","0,00","0,93","0,00","6,54","0,00","2,80","20,56","0,93","0,00","11,21","0,00","0,00","0,00","0,00","8,41","0,00","0,00"
593761,Blanné,68,46,45,"2,22","0,00","0,00","2,22","0,00","2,22","15,55","0,00","0,00","0,00","0,00","0,00","2,22","0,00","0,00","53,33","0,00","0,00","0,00","0,00","0,00","0,00","0,00","22,22","0,00","0,00"
593770,Blížkovice,974,624,624,"7,69","0,00","0,16","8,33","0,16","3,84","9,61","0,00","0,64","0,48","0,16","0,00","8,33","0,16","1,76","40,22","0,16","0,32","7,37","0,16","0,48","0,00","0,00","9,77","0,16","0,00"
593788,Bohutice,502,315,313,"6,38","0,00","0,00","3,51","0,31","2,23","8,94","0,31","0,63","1,59","0,00","0,00","5,11","0,00","6,07","47,60","0,00","0,31","4,15","0,00","0,00","0,00","0,00","12,46","0,31","0,00"
593796,Bojanovice,153,80,79,"3,79","0,00","0,00","6,32","0,00","3,79","5,06","0,00","0,00","1,26","0,00","0,00","1,26","0,00","0,00","53,16","0,00","0,00","6,32","0,00","0,00","0,00","0,00","17,72","1,26","0,00"
593800,Borotice,327,160,158,"3,79","0,00","0,00","14,55","0,00","3,79","14,55","0,63","3,16","0,63","0,00","0,00","2,53","0,00","0,63","31,01","0,00","0,63","4,43","0,00","0,00","0,00","0,00","18,98","0,63","0,00"
593818,Boskovštejn,131,95,95,"4,21","0,00","0,00","8,42","0,00","2,10","15,78","1,05","0,00","4,21","0,00","0,00","9,47","0,00","4,21","24,21","0,00","0,00","6,31","0,00","0,00","0,00","0,00","20,00","0,00","0,00"
593826,Božice,1 214,571,566,"7,42","0,35","0,00","7,42","0,53","2,12","11,48","0,88","1,06","1,23","0,00","0,00","7,24","0,00","2,47","30,74","0,00","0,00","4,77","0,00","0,53","0,35","0,17","20,49","0,70","0,00"
.
.
.

Skript je rozdělen do následujících funkcí:

def convert_to_href(root: str, xr: str, shift: int) -> str:
    """
    Vrácí link na obce uzemního celku nebo detalní výsledky obce, který skládá z root a xr
    :param root: obsahuje 1. část odkazu https:\\....
    :param xr: obsahuje 2. část odkazu na konkrétní obci
    :param shift: pozice první znaku 2. části odkazu, ta následně končí znakem "
    :return: vrací kompletní link na stránku obce nebo detail obce
    """

def collect_cities() -> None:
    """
    Funkce vytvoří 2 listy, list měst (mesta) z uvodní stránky 'https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ'
    a ve stejném pořádí list odkazů (href) na seznam obcí pro danný uzemní celek. Obě proměnné (mesta
    a href) jsou globální. Proměnná "flag" zajišťuje přeskakování řádku následujícího po řádku obsahujícího název
    územního celku.
    """

def collect_villages(i) -> dict:
    """
    Pro danný uzemní celek (sys.argv[1]) vyhledá v tabulce všechny obce a linky na detalní výsledky voleb
    Proměnná "flag" zajišťuje přeskakování řádků dle analýzy obsahu proměnné soup.
    :param i: index zadaného (příkazový řádek) uzemního celku v listu mesta
    :return: dictionary kde klíč je název obce a hodnota je list 2 hodnoty, číslo obce a link na výsledky voleb.

    """
def write_result(rdict: dict, fname: str) -> None:
    """
    Funkce prochází jednotlivé obce uzemního celku a zapisuje detalní výsledky do výstupního souboru.
    Výsledky jsou uloženy na html stránce ve 3 tabulkách. První obsahuje sumární čísla (počet voličů, volební
    účast atd.), druhá a třetí detalní výsledky pro jednotlivé strany. Proměnná "headers" pro první tabulku je
    upravena dvěmi příkazy headers.insert tak aby hodnoty odpovídaly pořadí hodnot v "results".
    Pro další tabulky je "headers" zadáno ručně (pořadí při načtení z html nesedí na "results".
    Pro 1. řádek ve výstupním souboru je headers doplněno o list kandidujích stran a headers je zapsán jako hlavička
    do výstupního souboru.

    :param rdict: slovník {jmeno obce : [cislo obce, link na detalni výsledky]}
    :param fname: výstupní soubor
    """

    def table_1(tab: bs4.element.ResultSet) -> list:
        """
        Pomocná funkce (z důvodu zpřehlednění kódu) zpracovává 1. tabulku z detalních výsledků obce.
        :param tab: vyparsované tabulky z detalních výsledků obce
        :return: vrací list složený z dictionary kde klíč je položka z header a hodnota je odpovídající hodnota
        """
    def table_2_3(tab: bs4.element.ResultSet) -> list:
        """
        Pomocná funkce (z důvodu zpřehlednění kódu) zpracovává 2. a 3. tabulku z detalních výsledků obce.
        V list results jsou přeskočeny první 2 hodnoty, které jsou prázné.

        :param tab: vyparsované tabulky z detalních výsledků obce
        :return: list obsahující pro každou stranu dictionary s detalnímí čísly pro stranu
        """

def volby2017():
    """
    Hlavní část scriptu. Volá collect_cities, tím si vytvoří list platných uzemních celku (mesta) a list (href) linků
    na seznam obcí pro daný územní celek.
    Následně kontroluje platnost vstupních parametrů. Pokud vyhodnocení vstupní parametrů vykazuje chybu script končí
    - nejsou zadány 2 parametry
    - pokud je zadán neexistující uzemní celek
    - pokud je zadán již existující soubor
    Pokud kontrola vstupních parametrů skončíla úspěšně je postupně volána funkce
    - collect_villages (připraví list obcí pro danný uzemní celek a linky na detalní výsledky voleb)
    - write_result (načte detalní výsledky voleb pro obec a zapíše je do výstupního souboru)

    :return: none
    """

