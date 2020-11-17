def verificar_secuencia(secuencia_fin):
    # Función que dadas dos secuencias de codones, verifica si cumple la condición inicial de que el codón inicial sea AUG y la secuencia final sea UAA, UAG o UGA. Retorna un valor booleano.
    # Zona de inicialización de variable
    secuencia_final = ["UAA", "UAG", "UGA"]
    exito = False
    i = 0

    while (i <= 2 and not exito):
        if secuencia_final[i] == secuencia_fin:
            exito = True
        i = i + 1
    
    return exito


print("Ingrese la secuencia que desea verificar")

secuencia_gen = input()

longitud = len(secuencia_gen)

longitud_menor = longitud - 3

secuencia_inicial = secuencia_gen[0:3]

secuencia_final = secuencia_gen[longitud_menor:longitud]

if secuencia_inicial == "AUG":
    es_secuencia = verificar_secuencia(secuencia_final)

if es_secuencia:
    print("Las secuencias de codones ingresadas son válidas")
else:
    print("Las secuencias de codones ingresadas no son válidas")

