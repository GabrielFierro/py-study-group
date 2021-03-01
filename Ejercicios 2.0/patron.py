def check_patterns(s1, s2):
    # Zona de inicialización de variables
    s1_len = len(s1)
    s2_len = len(s2)
    valid = True

    # Condicional dónde verifica la longitud de las cadenas
    if(s1_len != s2_len):
        valid = False
        return valid  # Termina la ejecución y retorna False
    elif(s1 == s2):  # Si la longitud de las cadenas coincide
        # Si las cadenas son exactamente iguales, retorna True
        return valid
    else:
        # Si las cadenas se corresponden en respectivo
        valid = reverse(s1, s2, s1_len, s2_len-1)
        if(not valid):
            # Si las cadenas se corresponden en frecuencia
            valid = frequency(s1, s2, s2_len-1)

    return valid


def reverse(s1, s2, s1_len, s2_len):
    # Función que verifica la frecuencia de la primer cadena con respecto a la otra
    # Zona de inicialización de variables
    match = True
    i = 0

    # Mientras los caracteres sean iguales y el iterador sea menor a la longitud de la primer cadena hacer
    while(match and i < s1_len):
        # Si los elementos entre ambas cadenas son diferentes, termina la ejecución
        if(s1[i] != s2[s2_len]):
            match = False
        else:
            # Sino aumenta y decrementa para continuar evaluando
            i = i + 1
            s2_len = s2_len - 1

    return match


def frequency(s1, s2, s2_len):
    # Zona de declaración de variables
    match = False
    i = 0
    s1_ocurrency_letter = s1[0]
    s2_ocurrency_letter = s2[0]

    if(s1.count(s1_ocurrency_letter) == s2.count(s2_ocurrency_letter)):
        match = True

    return match


result = check_patterns("", "")
print(result)   # Return True
result = check_patterns("aaabbb", "xxxyyy")
print(result)   # Return True
result = check_patterns("aaabbc", "abbccc")
print(result)   # Return false
result = check_patterns("asd", "dsa")
print(result)   # Return True
