#!/bin/python3
import re, os 
from time import sleep
from gitfinder.mod import searchGitt
#--------------------------------------------------


#            author telegram @pes528


#---------------------------------------------------


green = "\033[1;32m"
rojito = "\033[1;34m"
fin = "\033[0m"


def verifi(lista : list) -> bool:
    try:
        lista[0]
        return True
    except:
        return False


        




def logo():
    print("""
░██████╗░██╗████████╗██╗░░██╗██╗░░░██╗██████╗░
██╔════╝░██║╚══██╔══╝██║░░██║██║░░░██║██╔══██╗
██║░░██╗░██║░░░██║░░░███████║██║░░░██║██████╦╝
██║░░╚██╗██║░░░██║░░░██╔══██║██║░░░██║██╔══██╗
╚██████╔╝██║░░░██║░░░██║░░██║╚██████╔╝██████╦╝
░╚═════╝░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░╚═════╝░\n""")
    print("\033[1;101m                    𝙎𝙀𝘼𝙍𝘾𝙃                \033[0m")
    print("                 𝗯𝘆 Telegram:@𝗽𝗲𝘀𝟱𝟮𝟴 	\n")
    print("""
    ----------------------------------------
    Encuentra repositorios alojados en github
                        v1.0
    ----------------------------------------
    """)
def main() -> None:
    os.system("clear")
    logo()
    
    print("Escribe el nombre del respositorio que quieres buscar\nPreciona 0 para salir\n")
    repositorio = input("BUSCAR---> ")
    if repositorio == "0":
        os.system("clear")
        print("Saliste, para volver a iniciar escribe: python search.py")
    else:
        gitt = searchGitt(repositorio)
        gitt.buscarRepos()
        print(f"TOTAL ENCONTRADOS PARA [{rojito}{gitt.answer}{fin}] --> {rojito}{gitt.totalRepos}{fin}")
        gitt.viewResult()
        print("")
        paginasTotales = gitt.totalRepos/10
        numPag = 3
        contRepos = 0
    
        if gitt.totalRepos > 10:
            gitt.secondPage()

            while gitt.repositoriosActuales < gitt.totalRepos:
                print("—"*40)
                print(f"TOTAL RESPOSITORIOS VISTOS --> \033[1;31m {gitt.repositoriosActuales}\033[0m \nQUEDAN POR VER --> \033[1;31m{gitt.totalRepos-gitt.repositoriosActuales}\033[0m \n")
                sleep(3)
                u = input("Preciona enter para continuar\nPreciona 0 para volver\nOpcion-> : ")
                if u == "0":
                    return main()
                else:
                    gitt.otherPages(numPag)
                    numPag += 1
            print("Llegaste al final 😉 ")
            input("Preciona cualquier tecla para volver: ")
            main()
        elif gitt.totalRepos < 10:
            gitt.secondPage()
            input("Preciona enter para volver: ")
            main()

    

if __name__ == "__main__":
    main()
