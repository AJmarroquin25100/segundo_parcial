mail = input("Ingrese un mail:")
cantidad = 0  

x = 0  
while x < len(mail):  
    if mail[x] == "@":
        cantidad += 1  
    x += 1  

if cantidad == 1:
    print("Contiene solo un caracter @ el mail ingresado")  
else:
    print(" el numero es incorrecto Incorrecto")


 #Cambiar == a = en la asignación de mail para almacenar la entrada del usuario correctamente.
#Asignar 0 a la variable cantidad inicialmente.
#Asignar 0 a la variable x inicialmente.
#Cambiar leng a len para obtener la longitud de la cadena mail.
#Corregir la sintaxis en la condición del bucle while.
#Usar += para incrementar la variable cantidad y x.
#Corregir la condición if para comparar correctamente si mail[x] es igual a "@".
#Corregir la impresión en los casos de salida.