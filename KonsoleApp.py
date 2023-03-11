from GastMenu import GastMenu
from ZimmerMenu import ZimmerMenu
from MenuGemeinsam import MenuGemeinsam


def mainmenu():
    print("""
    --- Main Menu ---
    1: Gast Menu
    2: Zimmer Menu
    3: Reservierungs Menu
    4: Exit
    """)
    opt = int(input("opt="))
    if opt == 1:
        GastMenu()
        mainmenu()
    if opt == 2:
        ZimmerMenu()
        mainmenu()
    if opt == 3:
        MenuGemeinsam()
        mainmenu()
    if opt == 4:
        exit()
