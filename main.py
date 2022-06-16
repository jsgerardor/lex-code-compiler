from js_lexer import Analizador_lexico, Analizador_lexico_consola 

def menu():
    opcion = 0
    while (opcion != 3):
        print('''MENU ANALIZADOR
         \t1: Línea de código
         \t2: Analizador Lexico
         \t3: Salir''')
        opcion = int(input("opcion: "))
        if opcion == 1:
            print("Línea de código")
            Analizador_lexico_consola()
            print("\npresione enter para continuar...")
            input()
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
