class Conjunto:
    
    def __init__(self, elementos=None):
        self.__elementos = []
        if elementos is not None:
            for elem in elementos:
                if elem not in self.__elementos:
                    self.__elementos.append(elem)
        
    def cargar_conjunto(self, cantidad):
        for i in range(cantidad):
            num = int(input('Introduzca el número {} del conjunto'.format(i+1)))
            self.__elementos.append(num)        
                    
    def mostrar_conjunto(self):
        print('Contenido del conjunto')
        for num in self.__elementos:
            print('{}'.format(num))
            
    def __add__(self, otraLista):
        elementos = self.__elementos.copy()
        for elem in otraLista.__elementos:
            if elem not in elementos:
                elementos.append(elem)
        union_conjunto = Conjunto(elementos)
        print('La union de los conjuntos es')
        return  union_conjunto
    
    def __sub__(self, otraLista):
        elementos = self.__elementos.copy()
        for elem in otraLista.__elementos:
            if elem in elementos:
                elementos.remove(elem)
        diferencia_conjunto = Conjunto(elementos)
        print('La diferencia de conjuntos es')
        return diferencia_conjunto
    
    def __eq__(self, otraLista):
        if len(self.__elementos) == len(otraLista.__elementos):
            resultado = True
            for elem in otraLista.__elementos:
                if elem not in self.__elementos:
                    resultado = False
        else: resultado = False
        return resultado
