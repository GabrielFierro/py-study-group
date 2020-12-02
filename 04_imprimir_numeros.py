def listar_numeros(lista):
    # Función que recibe una lista de números y retorna una cadena de caracteres con el
    # caracter de escape de salto de línea entre medio de dichos números.
    numero = ""
    for x in range(0, len(lista)):
        numero = str(numero) + str(lista[x]) + "\n"

    return numero


lista_numeros = [1, 2, 3, 4, 5]
# lista_numeros = [1, 1, 1]
# lista_numeros = [3, 2, 1]
# lista_numeros = [10, 20, 30, 14, 14, 16, 20]

mostrarNumeros = listar_numeros(lista_numeros)

print("\u001b[36;1m" + mostrarNumeros)