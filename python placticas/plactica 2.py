print("")#implime espacio en blanco 
print("castruita soto emmanuel 1176 3w")#implime datos de alumno
print("")#implime espacio en blanco
# Definimos una variable con la nota
nota =int(input("ingresa tu calificacion"))# Ejemplo de nota

# Comprobamos en qué rango se encuentra la nota y mostramos el resultado correspondiente
if 0 <= nota < 5:#sino
    print("SUSPENSO")#implime el siguiente mensaje 
elif 5 <= nota < 6:#sino
    print("SUFICIENTE")#implime el siguiente mensaje 
elif 6 <= nota < 7:#sino
    print("BIEN")#implime el siguiente mensaje 
elif 7 <= nota < 9:#sino
    print("NOTABLE")#implime el siguiente mensaje 
elif 9 <= nota <= 10:#sino
    print("SOBRESALIENTE")#implime el siguiente mensaje 
else:#sino
    print("NOTA NO VÁLIDA")  # Si la nota no está en los rangos válidos, mostramos este mensaje
