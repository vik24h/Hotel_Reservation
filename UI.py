def add_zimmer_input():
    nr = int(input("Nummer:"))
    anzahlG = int(input("AnzahlGaste:"))
    preis = int(input("Preis:"))
    farbe = input("Farbe:")
    meerblick = input("Meerblick:")
    return nr, anzahlG, preis, farbe, meerblick

def change_preis_input():
    nr = int(input("Nummer des gewunschten Zimmers:"))
    preis = int(input("Neuer Preis:"))
    return nr,preis

def del_zimmer_input():
    nr = int(input("Nummer des gewunschten Zimmers:"))
    return nr

def add_guest_input():
    firstname = input("Vorname=")
    lastname = input("Nachname=")
    return firstname,lastname

def change_nachname_input():
    firstname = input("Vorname des gewunschten Gastes:")
    lastname = input("Nachname des gewunschten Gastes:")
    Neulastname = input("Neuer Nachname:")
    return firstname,lastname,Neulastname

def del_guest_input():
    firstname = input("Vorname des gewunschten Gastes:")
    lastname = input("Nachname des gewunschten Gastes:")
    return firstname,lastname

def do_reserv_input():
    firstname = input("Vorname=")
    lastname = input("Nachname=")
    return firstname,lastname

def zimmer_filter_input():
    seaview = input("Wollen Sie ein Meerblick haben=")
    price = int(input("Preis soll billiger als="))
    return seaview,price