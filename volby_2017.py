import os
import csv
import sys
import requests
import bs4

mesta = []
href = []


def convert_to_href(root: str, xr: str, shift: int) -> str:
    """
    Vrácí link na obce uzemního celku nebo detalní výsledky obce
    :param root: obsahuje 1. část odkazu https:\\....
    :param xr: obsahuje 2. část odkazu na konkrétní obci
    :param shift: pozice první znaku 2. části odkazu, ta následně končí znakem "
    :return: vrací kompletní link na stránku obce nebo detail obce
    """
    xr = xr[shift:xr[shift:len(xr)].find('"') + shift]
    xr = root + xr.replace('amp;', '')
    return xr


def collect_cities() -> None:
    """
    Funkce vytvoří 2 listy, list měst (mesta) z uvodní stránky 'https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ'
    a ve stejném pořádí list odkazů (href) na seznam obcí pro danný uzemní celek. Obě proměnné (mesta
    a href) jsou globální. Proměnná "flag" zajišťuje přeskakování řádku následujícího po řádku obsahujícího název
    územního celku.
    """

    r = requests.get('https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ')
    if r.status_code == 200:
        flag = -1
        soup = bs4.BeautifulSoup(r.text, 'html.parser')
        for item in soup.find_all('td'):
            flag += 1
            if len(item.get_text()) > 1 and not item.get_text().startswith('CZ'):
                mesta.append(item.get_text())
                flag = 0
            if flag == 2:
                href.append(convert_to_href('https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&', str(item.find('a')), 28))


def collect_villages(i) -> dict:
    """
    Pro danný uzemní celek (sys.argv[1]) vyhledá v tabulce všechny obce a linky na detalní výsledky voleb
    Proměnná "flag" zajišťuje přeskakování řádků dle analýzy obsahu proměnné soup.
    :param i: index zadaného (příkazový řádek) uzemního celku v listu mesta
    :return: dictionary kde klíč je název obce a hodnota je list 2 hodnoty, číslo obce a link na výsledky voleb.
    """
    rdict = {}
    village_num = ''
    village_href = ''
    r = requests.get(href[i])
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    flag = -1
    for item in soup.find_all('td'):
        flag += 1
        if len(item.get_text()) > 1 and item.get_text().isnumeric():
            village_num = str(item.get_text())
            village_href = convert_to_href('https://volby.cz/pls/ps2017nss/', str(item.find('a')), 9)
            flag = 0
        if flag == 1:
            village_name = str(item.get_text())
            rdict[village_name] = [village_num, village_href]
    return rdict


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
    csv_header = ['Kód obce', 'Název obce', 'Voliči v seznamu', 'Vydané obálky', 'Platné hlasy']
    csv_output = list()

    outfile = open(fname, 'w', encoding='UTF8', newline='')
    writer = csv.writer(outfile)

    def table_1(tab: bs4.element.ResultSet) -> list:
        """
        Pomocná funkce (z důvodu zpřehlednění kódu) zpracovává 1. tabulku z detalních výsledků obce.
        :param tab:
        :return: vrací list složený z dictionary kde klíč je položka z header a hodnota je odpovídající hodnota
        """
        headers = [header.text for header in tab[0].find_all('th')]
        headers.insert(1, 'Zprac.')
        headers.insert(2, 'Zprac %')
        res = [{headers[i]: cell.text for i, cell in enumerate(row.find_all('td'))}
               for row in tab[0].find_all('tr')]
        return res

    def table_2_3(tab: bs4.element.ResultSet) -> list:
        """
        Pomocná funkce (z důvodu zpřehlednění kódu) zpracovává 2. a 3. tabulku z detalních výsledků obce.
         V list results jsou přeskočeny první 2 hodnoty, které jsou prázné.

        :param tab: vyparsované tabulky z detalních výsledků obce
        :return: list obsahující pro každou stranu dictionary s detalnímí čísly pro stranu
        """
        res = list()
        headers = ['Poradi', 'Nazev', 'Hlasy', 'Hlasy %', 'Link']
        for k in range(1, 3):
            res.extend([{headers[i]: cell.text for i, cell in enumerate(row.find_all('td'))}
                        for row in tab[k].find_all('tr')][2:])
        return res

    for i, village in enumerate(rdict):
        running = ['|', '/', '-', '\\']
        r = requests.get(rdict[village][1])
        csv_output.clear()
        soup = bs4.BeautifulSoup(r.text, 'html.parser')
        tables = soup.find_all('table')
        csv_output = [rdict[village][0], village]
        results = table_1(tables)
        csv_output.extend([results[2]['Voličiv seznamu'], results[2]['Vydanéobálky'], results[2]['Platnéhlasy']])
        results.clear()
        results = table_2_3(tables)
        if i == 0:
            csv_header.extend([strana['Nazev'] for strana in results])
            writer.writerow(csv_header)
        csv_output.extend([strana['Hlasy %'] for strana in results])
        writer.writerow(csv_output)
        print(running[i % 4], end="\r")
    outfile.close()
    print(' ', end='\r')


def volby2017():
    """
    Hlavní část scriptu. Volá collect_cities, tím si vytvoří list platných uzemních celku (mesta) a list (href) linků
    na seznam obcí pro daný územní celek.
    Následně kontroluje platnost vstupních parametrů. Pokud vyhodnocení vstupní parametrů vykazuje chybu script končí
    - nejsou zadány 2 parametry
    - pokud je zadám neexistující uzemní celek
    - pokud je zadán již existující soubor
    Pokud kontrola vstupních parametrů skončíla úspěšně je postupně volána funkce
    - collect_villages (připraví list obcí pro danný uzemní celek a linky na detalní výsledky voleb)
    - write_result (načte detalní výsledky voleb pro obec a zapíše je do výstupního souboru)

    :return: none
    """
    collect_cities()
    if len(sys.argv) == 3:
        try:
            inx = mesta.index(sys.argv[1])
        except ValueError:
            print('Neexistující územní celek ' + '"' + sys.argv[1] + '"!')
            return
        if sys.argv[2] in os.listdir():
            print('Zadaný soubor "' + sys.argv[2] + '" již existuje!')
            return
    else:
        print('Špatný počet argumentů. Dva jsou očekávány!')
        return
    dvillages = collect_villages(inx)
    write_result(dvillages, sys.argv[2])


if __name__ == '__main__':
    volby2017()
