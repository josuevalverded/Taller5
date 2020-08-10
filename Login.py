import Usuario
import Contraseña

correcto=False
while correcto==False:
        nombre=input("Ingrese nombre de usuario: ")
        if Usuario.nickname(nombre) == True:
            print("Usuario creado exitosamente")
            correcto=True

while correcto==True:
    contrasenia=input("Ingrese su Password: ")
    if Contraseña.clave(contrasenia)==True:
        print("Contraseña creada exitosamente")
        correcto=False


