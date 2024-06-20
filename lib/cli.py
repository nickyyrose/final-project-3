# lib/cli.py

from models.seeds import seeds_database
from helpers import (
    exit_program,
    add_store, update_store, delete_store, view_all_stores, view_store,
    add_instrument, update_instrument, delete_instrument, view_all_instruments, view_instrument,
    add_inventory, update_inventory, delete_inventory, view_all_inventorys, view_inventory
)

def main():
    seeds_database()  
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            store_menu()
        elif choice == "2":
            instrument_menu()
        elif choice == "3":
            inventory_menu()
        else:
            print("Invalid choice")

def menu():
    print("""
          
MMMMMMMWKxc,...  ...,cokKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMNk:.               .,lkKWMMMMMMMMMMMMMMMMMMMMMMMMNX0kxdoddxOKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMW0:                      .;okXWMMMMMMMMMMMMMMMWKko:'..        .,o0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMWk.                           .;lxOKXXNNXXK0koc,.                 ,KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MWk.                                 ........                  ..,;cxNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MK,                                                         ,lkKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
Wo                                                        ,kNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
K,                                                       ,0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
O.                                                       :XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMOcoXN0XWMMMMMMMMMMMMMMMM
x.               'c::lo'  .cc.    .:l'     .cc.          .cONNNNNNWWNWWNWWWWWWWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXdoc.;0x'cKklkNXKNMMMMMMMMM
x.               ;xdo0Nl. :0Kc... ,OXo.    :KK:..'.........'::c:c::l:cc:lc;:ll:coccolclolcodllodoloddoodxdoodxddddxxdxxkOko,.co..ll.,o;.l0l'xKdoKWXNMM
x.               ;xdo0Nl  :0Kc    ,OKl.    :00:.','''''''''''.'.'..,..'.''  .' .'..'. .'. .'. .'. .'....'....'....,....':'...,;..oo.'d:.,d;.ll.'kk,cKM
x.               ;xdo0Nl  ;00:    ,OKl.    :00:.'''''..'.'....'.'..'..'.'.  .. .'..'. .'. .'. .'. .'.  .'.. .'....,... .:' ..........:,.;x;.:o..cc.,kN
x.               ;xdo0Nl  ;00:    ,kKl.    :00:..'''...''''''.'.,..,.''.,,..',.',..,'.';'.,;'.,;,.':;'';:;,,;c;,;;l:;;;coc;;..   ...    .. .,:..oc. .d
k.               :xkkOO;  .dd'    .lx;     'dd'    .;cdkOOOO0O0000000000KK00KK0KKKKKKKKXKKXXXXXXXXXNNXXNNNNNNNNNNWWWWWWWWWWNKx;    ..';cloodoc,.  .,dX
k.               .';:'..                          ;ONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNkodk0XNMMMMMMMMN0dx0NMM
O.   .,..             .............              .OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
X;   .......          ......                     .kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
Wd.  ..........         ........                   .dKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MX:   .........       .........                      .;lxO0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MM0'    ................         .;coddol;.              .'xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMW0,     .............     .;lx0XWMMMMMMWXOdc,.         .,OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMXd,.          .,'...,cokXWMMMMMMMMMMMMMMMMWXOxdllclox0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMN0dl:,''.'';:ldk0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
 _______         _______________________    _______________________ _______ _______    _______ _______ _       _______ _______ _______ _______ 
(       )\     /(  ____ \__   __(  ____ \  (  ____ \__   __(  ___  |  ____ |  ____ \  (       |  ___  | (    /(  ___  |  ____ (  ____ (  ____ )
| () () | )   ( | (    \/  ) (  | (    \/  | (    \/  ) (  | (   ) | (    )| (    \/  | () () | (   ) |  \  ( | (   ) | (    \/ (    \/ (    )|
| || || | |   | | (_____   | |  | |        | (_____   | |  | |   | | (____)| (__      | || || | (___) |   \ | | (___) | |     | (__   | (____)|
| |(_)| | |   | (_____  )  | |  | |        (_____  )  | |  | |   | |     __)  __)     | |(_)| |  ___  | (\ \) |  ___  | | ____|  __)  |     __)
| |   | | |   | |     ) |  | |  | |              ) |  | |  | |   | | (\ (  | (        | |   | | (   ) | | \   | (   ) | | \_  ) (     | (\ (   
| )   ( | (___) /\____) |__) (__| (____/\  /\____) |  | |  | (___) | ) \ \_| (____/\  | )   ( | )   ( | )  \  | )   ( | (___) | (____/\ ) \ \__
|/     \(_______)_______)_______(_______/  \_______)  )_(  (_______)/   \__(_______/  |/     \|/     \|/    )_)/     \(_______|_______//   \__/
                                                                                                                                               

          """)
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Manage stores")
    print("2. Manage instruments")
    print("3. Manage inventorys")

def store_menu():
    print("""
 _______________________ _______ _______  _______ 
(  ____ \__   __(  ___  |  ____ |  ____ \(  ____ |
| (    \/  ) (  | (   ) | (    )| (    \/| (    \/
| (_____   | |  | |   | | (____)| (__    | (_____ 
(_____  )  | |  | |   | |     __)  __)   (_____  )
      ) |  | |  | |   | | (\ (  | (            ) |
/\____) |  | |  | (___) | ) \ \_| (____/\/\____) |
\_______)  )_(  (_______)/   \__(_______/\_______)
            """)
    print("1. Add a store")
    print("2. Update a store")
    print("3. Delete a store")
    print("4. View all stores")
    print("5. View a store")
    choice = input("> ")
    if choice == "1":
        add_store()
    elif choice == "2":
        update_store()
    elif choice == "3":
        delete_store()
    elif choice == "4":
        view_all_stores()
    elif choice == "5":
        view_store()
    else:
        print("Invalid choice")

def instrument_menu():
    print("""
            
__________       _______________________         _______ _______ _      ________________ 
\__   __( (    /(  ____ \__   __(  ____ )\     /(       |  ____ ( (    /\__   __(  ____ |
   ) (  |  \  ( | (    \/  ) (  | (    )| )   ( | () () | (    \/  \  ( |  ) (  | (    \/
   | |  |   \ | | (_____   | |  | (____)| |   | | || || | (__   |   \ | |  | |  | (_____ 
   | |  | (\ \) (_____  )  | |  |     __) |   | | |(_)| |  __)  | (\ \) |  | |  (_____  )
   | |  | | \   |     ) |  | |  | (\ (  | |   | | |   | | (     | | \   |  | |        ) |
___) (__| )  \  /\____) |  | |  | ) \ \_| (___) | )   ( | (____/\ )  \  |  | |  /\____) |
\_______//    )_)_______)  )_(  |/   \__(_______)/     \(_______//    )_)  )_(  \_______)
                                                                                         

            """)
    print("1. Add an instrument")
    print("2. Update an instrument")
    print("3. Delete an instrument")
    print("4. View all instruments")
    print("5. View an instrument")
    choice = input("> ")
    if choice == "1":
        add_instrument()
    elif choice == "2":
        update_instrument()
    elif choice == "3":
        delete_instrument()
    elif choice == "4":
        view_all_instruments()
    elif choice == "5":
        view_instrument()
    else:
        print("Invalid choice")

def inventory_menu():
    print("""
            
__________               _______ _      ________________ _______         
\__   __( (    /|\     /(  ____ ( (    /\__   __(  ___  |  ____ )\     /|
   ) (  |  \  ( | )   ( | (    \/  \  ( |  ) (  | (   ) | (    )( \   / )
   | |  |   \ | | |   | | (__   |   \ | |  | |  | |   | | (____)|\ (_) / 
   | |  | (\ \) ( (   ) )  __)  | (\ \) |  | |  | |   | |     __) \   /  
   | |  | | \   |\ \_/ /| (     | | \   |  | |  | |   | | (\ (     ) (   
___) (__| )  \  | \   / | (____/\ )  \  |  | |  | (___) | ) \ \__  | |   
\_______//    )_)  \_/  (_______//    )_)  )_(  (_______)/   \__/  \_/   
                                                                         

            """)
    print("1. Add an inventory")
    print("2. Update an inventory")
    print("3. Delete an inventory")
    print("4. View all inventorys")
    print("5. View an inventory")
    choice = input("> ")
    if choice == "1":
        add_inventory()
    elif choice == "2":
        update_inventory()
    elif choice == "3":
        delete_inventory()
    elif choice == "4":
        view_all_inventorys()
    elif choice == "5":
        view_inventory()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
