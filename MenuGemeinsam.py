from Gaste import Gaste
from datetime import date
from Reservirung import Reservierung
from ZimmerMenu import *
from GastMenu import *
from Time import *


def datei_lesen_reserv(ReservListe):
    """

        Die Methode geht durch die Datei und speichert die Daten in einer Liste
    """
    h = open('Reservliste', 'r')
    line = h.readline()
    while line != '':
        p = line.split(',')
        reserv = Reservierung(p[0], p[1], p[2], p[3], p[4])
        ReservListe.append(reserv)
        line = h.readline()
    h.close()

def test_if_reserv_good(ReservListe,datum,nr):
    """

    testet ob die Reservierung moglich ist
    """
    for obj in ReservListe:
        if int(obj.zimmer) == nr:
            if compare_two_dates(datum,obj.anfang) == 0 and compare_two_dates(datum,obj.ende) == 1:
                return 0
    return 1

def do_reserv(ReservListe, ZimmerListe, GastListe, firstname, lastname):
    """

    Die Methode macht eine Reservierung. Testet ob sie moglich ist, ob nicht falsche Felder eingegeben wurden
    """
    found = 0
    for i in range(len(GastListe)):
        if GastListe[i].nachname == lastname and GastListe[i].vorname == firstname:
            found = 1
            index = i
    if found == 0:
        print("Person nicht gefunden!")
    else:
        found = 0
        print('\n')
        to_string_zimmer(ZimmerListe)
        nr = int(input("Nummer:"))
        for obj in ZimmerListe:
            if int(obj.nummer) == int(nr):
                found = 1
        if found == 0:
            print("Zimmer nicht gefunden!")
        else:
            nrGaste = int(input("Anzahl Gaste:"))
            if int(nrGaste) > int(ZimmerListe[nr-1].anzahlG):
                print("Zu viele Gaste")
            else:
                anfang = input("Anfang(Format ZZ/MM/YYYY):")
                ende = input("Ende(Format ZZ/MM/YYYY):")
                if compare_two_dates(anfang,ende) == 0:
                    print("Falscher input!")
                else:
                    if test_if_reserv_good(ReservListe,anfang,nr) == 0 or test_if_reserv_good(ReservListe,ende,nr) == 0:
                        print("Zimmer ist nicht frei!")
                    else:
                        ReservListe.append(Reservierung(index, nr, nrGaste, anfang, ende))
                        for obj in GastListe:
                            if obj.nachname == lastname and obj.vorname == firstname:
                                obj.reserv.append(Reservierung(index,nr,nrGaste,anfang,ende))
                        h = open('Reservliste', 'w')
                        for obj in ReservListe:
                            h.write(f'{obj.indexGast},{obj.zimmer},{obj.nrG},{obj.anfang},{obj.ende},' + '\n')
                        h.close()

def aktuelle_Res(ReservListe,GastListe):
    """

    Die Methode gibt an wie viele Zimmer aktuell besetzt sind
    """
    heute = date.today()
    for obj in ReservListe:
        if compare_date_with_heute(heute, obj.ende) == 1:
            print(f'Gast:{GastListe[int(obj.indexGast)].vorname} {GastListe[int(obj.indexGast)].nachname}, '
                  f'Reservierung(Zimmer:{obj.zimmer}, Anzahl Gaste:{obj.nrG}, Anfangdatum:{obj.anfang}, Enddatum:{obj.ende}')

def Zimmer_filter(ZimmerListe, seaview, price):
    """

    Die Methode fur die Preis und Meeresblick Kriterien
    """
    for obj in ZimmerListe:
        if obj.meerblick == seaview and int(obj.preis) < int(price):
            print(
                f'Nummer:{obj.nummer}, Anzahl Gaste:{obj.anzahlG}, Preis:{obj.preis}, Farbe:{obj.farbe}, Meerblick:{obj.meerblick}')

def Zimmer_frei(ReservListe,ZimmerListe):
    """

    """
    heute = date.today()
    for i in range(len(ZimmerListe)):
        frei = 1
        for obj in ReservListe:
            if int(obj.zimmer) == i+1:
                if compare_date_with_heute(heute,obj.anfang) == 0 and compare_date_with_heute(heute,obj.ende) == 1:
                    frei = 0
        if frei == 1:
            print(f'Nummer:{ZimmerListe[i].nummer}, Anzahl Gaste:{ZimmerListe[i].anzahlG}, Preis:{ZimmerListe[i].preis}, Farbe:{ZimmerListe[i].farbe}, Meerblick:{ZimmerListe[i].meerblick}')



def MenuGemeinsam():
    print("""
    --- Reservierungs Menu ---
    1: Mach eine Reservierung
    2: Liste von Gasten mit aktuellen Reservierungen
    3: Zimmer mit Preis und Meerblick Kriterien
    4: heutige freien Zimmer
    5: zuruck zum Main Menu
    """)
    opt = int(input('opt='))

    GastListe = []
    datei_lesen_guest(GastListe)

    ZimmerListe = []
    datei_lesen_zimmer(ZimmerListe)

    ReservListe = []
    datei_lesen_reserv(ReservListe)

    if opt == 1:
        firstname,lastname = do_reserv_input()
        do_reserv(ReservListe, ZimmerListe, GastListe, firstname, lastname)
        MenuGemeinsam()
    if opt == 2:
        aktuelle_Res(ReservListe,GastListe)
        MenuGemeinsam()
    if opt == 3:
        seaview, price = zimmer_filter_input()
        Zimmer_filter(ZimmerListe, seaview, price)
        MenuGemeinsam()
    if opt == 4:
        Zimmer_frei(ReservListe,ZimmerListe)
        MenuGemeinsam()
