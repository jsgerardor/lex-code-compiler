# -*- enconding: utf-8 -*-
import os
from COM.c_lexer import Analizador_lexico
import ply_build.armar as construir


def menu():
    opcion = 0
    while (opcion != 8):
        # os.system("clear")
        print('''MENU COMPILADOR
         \t1: Programa Fuente
         \t2: Analizador Lexico
         \t3: Salir''')
        opcion = int(input("opcion: "))
        if opcion == 1:
            print("Programa Fuente")
            fuente = input("fuente: ")
            os.system("nano " + fuente)
        elif opcion == 2:
            print("Analizador Lexico")
            Analizador_lexico()
            print("\npresione enter para continuar...")
            input()
        elif opcion == 3:
            print("gracias por usar este programa")
        else:
            print("ok")
    pass


if __name__ == '__main__':
    menu()
