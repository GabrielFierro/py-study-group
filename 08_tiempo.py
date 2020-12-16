import datetime
import time

def calcular_diferencia(anio_a, anio_nac):
    # Función que calcula la diferencia entre el año actual y el año de nacimiento
    return anio_a - anio_nac

def recordatorio():
    # Función que por defecto setea un recordatorio de menos de 1 minuto
    
    # Zona de inicialización de variables
    tiempo_actual = datetime.datetime.now() # Almaceno el tiempo actual con formato de dia y hora
    segundos_actuales = tiempo_actual.second # Guardo los segundos actuales según datetime
    segundos_aux = segundos_actuales    # Almaceno en una variable auxiliar los segundos actuales
    diferencia_min = 0  # Defino que el tiempo es menor a 1 minuto

    while(diferencia_min == 0):
        # Mientras la diferencia sea igual a cero, muestro por consola los segundos hasta llegar a cero
        print("Faltan",diferencia_min,"minutos con",segundos_aux,"segundos")
        segundos_aux = segundos_aux - 1
        time.sleep(1) 
        if segundos_aux == 0:   # Si los segundos llegaron a cero, termina la ejecución del while
            diferencia_min = diferencia_min - 1

    print("\u001b[32m¡FE"+"\u001b[36mLICES "+"\u001b[35mFIES"+"\u001b[33mTAS!")    # Finalizó el recordatorio e imprime el mensaje


# Zona de inicialización de variables del tiempo actual
tiempo_actual = datetime.datetime.now()

anio_actual = tiempo_actual.year  

mes_actual = tiempo_actual.month

dia_actual = tiempo_actual.day

# Solicito los datos de la fecha de nacimiento del usuario

print("Ingrese su anio de nacimiento")
anio_nacimiento = int(input())

print("Ingrese su mes de nacimiento")
mes_nacimiento = int(input())

print("Ingrese su día de nacimiento")
dia_nacimiento = int(input())

# Invoco a la función calcular_edad
edad = calcular_diferencia(anio_actual, anio_nacimiento) 

if mes_nacimiento >= mes_actual:
    if dia_nacimiento < dia_actual:
        edad = edad - 1

print("El usuario tiene",edad,"años")


# Llama a la función recordatorio
recordatorio()
