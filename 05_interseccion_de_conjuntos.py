def cargar_lista():
    lista_numeros = []
    print("Ingrese la cantidad de números de la lista")
    cant_a = int(input())

    for i in range(0, cant_a):
        print("Ingrese un número para agregar a la lista")
        numero = int(input())
        
        lista_numeros.append(numero)

    return lista_numeros

def interseccion(list1, list2):
    list_int = [i for i in list1 + list2 if i in list1 and i in list2]
    return list_int

# Zona de inicialización de variables
a = []
b = []

print("Cargar la primer lista")
a = cargar_lista()
print("\nCargar la segunda lista")
b = cargar_lista()

if(len(a) < len(b)):
    # Llama a la función interseccion y le pasa las 2 listas
    # de arriba como argumentos

    lista_ordenada = interseccion(a, b)

print("\u001b[36;1m" + "Lista ordenada: " + str(sorted(set(lista_ordenada))))
