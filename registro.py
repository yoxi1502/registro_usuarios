import os
os.system('cls')
import re
usuarios={}
def passwd_valida(passwd):
    if ' ' in passwd:
        return False
    if len(passwd)<6 or not re.search(r'[A-Z]',passwd) or not re.search(r'[0-9]',passwd):
        return False
    return True
def menu():
    while True:
        print("1.Registrar usuario")
        print("2.Consultar usuario")
        print("3.Eliminar usuario")
        print("4.Salir")
        try:
            opcion=int(input("Ingrese una opcion: "))
        except ValueError:
            print("Opcion no valida.")
            continue
        if opcion==1:
            nombre=input("Ingrese su nombre: ")
            if nombre in usuarios:
                print("El nombre ya se encuentra registrado.")
                continue
            edad=int(input("Ingrese su edad: "))
            passwd=input("Ingrese su contraseña: ")
            if edad<18:
                print("El usuario debe ser mayor a 18.")
            elif not passwd_valida (passwd):
                print("La contraseña es invalida.")
            else:
                usuarios[nombre]={"edad":edad,
                                "passwd":passwd}
                print("Usuario agregado correctamente.")

        elif opcion==2:
            nombre=input("Ingrese el nombre que desea consultar:")
            if nombre in usuarios:
                print(f"edad:{usuarios[nombre]['edad']},contraseña{usuarios[nombre]['passwd']}")
            else:
                print("Nombre no encontrado")

        elif opcion==3:
            nombre=input("Ingrese el nombre del usuario que desea eliminar: ")
            if nombre in usuarios:
                del usuarios[nombre]
                print("Usuario eliminado correctamente.")
            else:
                print("Usuario no encontrado")
        elif opcion==4:
            print("Adios.")
            break

        
menu()
    
