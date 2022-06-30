import os


def Analizador_sintactico():
    a = raw_input("direccion: ")
    if (os.path.exists(a)):
        os.system("g++ -Wall -c    " + a)
        if (os.path.exists("*.o")):
            os.system("del *.o")
    else:
        print ("Error en el nombre del archivo")


def OBJ():
    a = raw_input("direccion: ")
    if (os.path.exists(a)):
        os.system("g++ -Wall -c " + a)
        raw_input()	        
    
    print("\npresione enter para continuar...")
    


def EXE():
    a = raw_input("direccion: ")
    if (os.path.exists(a)):
        os.system("g++ -Wall -o " + "run " + a)
    
    raw_input()	        
    print("\npresione enter para continuar...")
    

def RUN():
    os.system("./run")