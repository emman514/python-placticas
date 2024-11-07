print("")#implime espacio en blanco 
print("castruita soto emmanuel 1176 3w")#implime datos de alumno
print("")#implime espacio en blanco
# Definimos las variables nombre y apellido
nombre = (input("ingresa tu nombre "))# se le da valor a nombre
apellido = (input("ingresa tu apellido"))# sele da valor a apellido

# Comprobamos el nombre y apellido
if nombre == "Daniel":#sinombre es igual
    if apellido == "Ramos":#si apellido es igual
        print(nombre + apellido)  # Si el nombre y apellido son correctos, mostramos este mensaje
    else:#sino
        print("Apellido incorrecto")  # Si el apellido no coincide, mostramos este mensaje
else:#sino
    print("Usuario desconocido")  # Si el nombre no es "Daniel", mostramos este mensaje
