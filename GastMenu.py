from Gaste import Gaste
from UI import *

def datei_lesen_guest(GastListe):
    """

    Die Methode geht durch die Datei und speichert die Daten in einer Liste
    """
    f = open("gastliste", 'r')
    line = f.readline()
    while line != '':
        p = line.split(',')
        gast = Gaste(p[0], p[1])
        GastListe.append(gast)
        line = f.readline()
    f.close()

def add_guest(GastListe):
    """

    die Methode liest einen Vornamen und Nachnamen von der Tastatur und speichert sie in der Datei
    """
    firstname, lastname = add_guest_input()
    GastListe.append(Gaste(firstname,lastname))
    f = open('gastliste','w')
    for obj in GastListe:
        f.write(obj.vorname+','+obj.nachname+','+'\n')
    f.close()


def change_lastname(GastListe,lastname,firstname,Neulastname):
    """

    wenn die Person mit dem eingegebenen Namen gefunden wird, dann wird der nachname verandert
    """
    f = open('gastliste', 'w')
    found = 0
    for obj in GastListe:
        if obj.nachname == lastname and obj.vorname == firstname:
            obj.nachname = Neulastname
            found = 1
        f.write(obj.vorname + ',' + obj.nachname+','+'\n')
    if found == 0:
        print("Person nicht gefunden! Bitte typen Sie nochmals")
    f.close()


def del_guest(GastListe,lastname,firstname):
    """

    Die Methode schreibt alle Gaste zuruck in der Datei die nicht gleich mit dem eingegebenen Namen sind
    """
    f = open('gastliste', 'w')
    found = 0
    for obj in GastListe:
        if obj.nachname != lastname or obj.vorname != firstname:
            f.write(obj.vorname + ',' + obj.nachname+','+'\n')
        else:
            found = 1
    if found == 0:
        print("Person nicht gefunden!")
    f.close()


def to_string_guest(GastListe):

    for obj in GastListe:
        print(f'Vorname: {obj.vorname}, Nachname: {obj.nachname}')


def GastMenu():
    print("""
     --- GastMenu ---
    1: Fuge ein neuer Gast ein
    2: Aktualisierung des Nachnamens eines Gastes
    3: Loschen eines Gastes
    4: Liste von Gasten
    5: return to main menu
    """)
    GastListe = []
    datei_lesen_guest(GastListe)
    opt = int(input("opt="))
    if opt == 1:
        add_guest(GastListe)
        GastMenu()
    if opt == 2:
        firstname,lastname,Neulastname = change_nachname_input()
        change_lastname(GastListe,lastname,firstname,Neulastname)
        GastMenu()
    if opt == 3:
        firstname,lastname = del_guest_input()
        del_guest(GastListe,lastname,firstname)
        GastMenu()
    if opt == 4:
        to_string_guest(GastListe)
        GastMenu()