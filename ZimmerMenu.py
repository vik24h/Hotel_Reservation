from Zimmer import Zimmer
from UI import *


def datei_lesen_zimmer(ZimmerListe):
    """

    Die Methode geht durch die Datei und speichert die Daten in einer Liste
    """
    g = open("zimmerliste", 'r')
    line = g.readline()
    while line != '':
        p = line.split(',')
        zimmer = Zimmer(p[0], p[1], p[2], p[3], p[4])
        ZimmerListe.append(zimmer)
        line = g.readline()
    g.close()


def add_zimmer(ZimmerListe):
    """

    Diese Methode benutzt eine input Methode aus dem UI um ein Zimmer zu speichern
    """
    nr, anzahlG, preis, farbe, meerblick = add_zimmer_input()
    ZimmerListe.append(Zimmer(nr,anzahlG,preis,farbe,meerblick))
    g = open('zimmerliste', 'w')
    for obj in ZimmerListe:
        g.write(f'{obj.nummer},{obj.anzahlG},{obj.preis},{obj.farbe},{obj.meerblick},'+'\n')
    g.close()


def change_preis(ZimmerListe,nr,preis):
    """

    wenn die Nummer des Zimmers gefunden wird, wird der Preis mit dem neuen aktualisiert
    """
    g = open('zimmerliste', 'w')
    found = 0
    for obj in ZimmerListe:
        if int(obj.nummer) == int(nr):
            obj.preis = preis
            found = 1
        g.write(f'{obj.nummer},{obj.anzahlG},{obj.preis},{obj.farbe},{obj.meerblick},'+'\n')
    if found == 0:
        print("Zimmer nicht gefunden!")
    g.close()


def del_zimmer(ZimmerListe,nr):
    """

    alle Zimmer ausser den eingegebenen werden zuruck in der Datei geschrieben
    """
    g = open('zimmerliste', 'w')
    found = 0
    for obj in ZimmerListe:
        if int(obj.nummer) != int(nr):
            g.write(f'{obj.nummer},{obj.anzahlG},{obj.preis},{obj.farbe},{obj.meerblick},'+'\n')
        else:
            found = 1
    if found == 0:
        print("Zimmer nicht gefunden!")
    g.close()


def to_string_zimmer(ZimmerListe):
    """

    formatierung fur das Anschreiben der Zimmer
    """
    for obj in ZimmerListe:
        print(f'Nummer:{obj.nummer}, Anzahl Gaste:{obj.anzahlG}, Preis:{obj.preis}, Farbe:{obj.farbe}, Meerblick:{obj.meerblick}')


def ZimmerMenu():
    print("""
    --- ZimmerMenu ---
    1: Fuge ein Zimmer ein
    2: Aktualisierung des Preises eines Zimmers
    3: Loschen eines Zimmers
    4: Liste von Zimmern
    5: zuruck zum Main Menu
    """)
    ZimmerListe = []
    datei_lesen_zimmer(ZimmerListe)
    opt = int(input("opt="))
    if opt == 1:
        add_zimmer(ZimmerListe)
        ZimmerMenu()
    if opt == 2:
        nr, preis = change_preis_input()
        change_preis(ZimmerListe,nr,preis)
        ZimmerMenu()
    if opt == 3:
        nr = del_zimmer_input()
        del_zimmer(ZimmerListe,nr)
        ZimmerMenu()
    if opt == 4:
        to_string_zimmer(ZimmerListe)
        ZimmerMenu()


