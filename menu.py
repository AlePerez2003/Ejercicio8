from conjunto import Conjunto

def mostrar_menu():
    print('Opción 1: Sumar Conjuntos')
    print('Opción 2: Restar Conjuntos')
    print('Opción 3: Igualdad de Conjuntos')
    print('Opción 0: Finalizar Operación')
    
def menu():
    A = Conjunto()
    B = Conjunto()
    
    cantA = int(input('Ingrese la cantidad de Elementos del Conjunto A'))
    A.cargar_conjunto(cantA)
    
    cantB = int(input('Ingrese la cantidad de Elementos del Conjunto B'))
    B.cargar_conjunto(cantB)
    
    print('Conjunto A:')
    A.mostrar_conjunto()
    print('')
    
    print('Conjunto B:')
    B.mostrar_conjunto()
    print('')
    
    mostrar_menu()
    i = int(input('Ingrese el código'))
    
    while i != 0:
        if i == 1:
            AB = A + B
            AB.mostrar_conjunto()
            print('')
        elif i == 2:
            AB = A - B
            AB.mostrar_conjunto()
            print('')
        elif i == 3:
            if A == B:
                print('Los conjuntos son iguales')
            else: print('Los conjuntos son distintos')
        i = int(input('Ingrese el código'))
                
            
            