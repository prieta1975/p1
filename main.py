import sys                  # Permite utilizar la variable __name__


def ImprimirParametrosEntrada(*args):
    print('------')
    for element in args:
        print(element)
    print('--------------------')
    print()

def Listas():
    # Ejemplos de uso de listas
    print('--------------------')
    print('EJEMPLOS DE USO DE LISTAS')
    print()
    lista = ['Primero', 'Segundo', 'Tercero']
    print(lista)
    for elemento in lista:
        print(elemento)
    lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(lista2[0])  # Imprime el primer valor de la lista
    print(lista2[0:3])  # Imprime la lista con los 3 primeros números de la lista de entrada
    print(lista2[0:1])  # Imprime la lista con el primer número de la lista de entrada
    print(lista2[-1:])  # Imprime la lista con el último número de la lista de entrada
    print(lista2[:3])  # Imprime los 3 primeros números
    print(lista2[-3:])  # Imprime los 3 últimos números
    print(lista2[-5:-2])  # Imprime desde el quinto al segundo desde el final (3 números)

    parte1 = lista2[:5]  # Primera parte de la lista
    parte2 = lista2[5:]  # Segunda parte de la lista
    print(parte1)
    print(parte2)
    lista3 = parte1 + parte2  # + concatena dos listas
    print(lista3)
    lista3.reverse()  # Reverse:  invierte la lista
    print(lista3)
    lista3.append(0)
    print(lista3)
    print(len(lista3))
    cero = lista3.pop(len(lista3) - 1)  # pop: la variable toma el número en el índice, y lo quita de la lista
    print(cero)  # pop: el número tomado (el último de la lista)
    print(lista3)  # pop: Imprime la lista sin el número
    lista3.sort()  # sort: ordena la lista
    print(lista3)

def Diccionarios():
    # Ejemplos de uso de diccionarios
    # Los diccionarios pueden tener múltiples parejas identificador:valor, tanto cadenas como números
    print('--------------------')
    print('EJEMPLOS DE USO DE DICCIONARIOS')
    print()
    diccionario = {}                            # Genera cadena vacía
    diccionario['ID0'] = 'Usuario0'             # Incorpora un par string:string al diccionario
    diccionario['ID1'] = 'Usuario1'             # Incorpora un par string:string al diccionario
    for i in range(2, 5):                       # Incorpora 3 pares string:string más al diccionario
        diccionario['ID'+str(i)] = 'Usuario' \
                                   + str(i)
    print(diccionario)
    print(diccionario['ID4'])                   # Imprime el valor asociado al ID4
    diccionario[7] = 3                          # Incoporpora un par int:int
    print(diccionario)
    diccionario['ID99'] = 99                    # Incorpora un par string:int
    print(diccionario)
    diccionario[83] = 'Numero 83'               # Incorpora un par int:string
    print(diccionario)

if __name__ == "__main__":  # Determina si estamos en el espacio de nombres principal
    print("En main")
    ImprimirParametrosEntrada(*sys.argv)    # Para lista con los argumentos de entrada

    # Cuerpo de programa
    Listas()
    Diccionarios()

else:
    print("Fuera de main")

print()
print("--------------------")
print("Fin de Programa")






