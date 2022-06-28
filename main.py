import socket
import sys
import getpass
from clienteregistro import registro
from clientelogin import login
from clienteverfacultades import facultades
from clientevermenus import vermenusfacultad
from clientedetallemenu import verdetallemenu
from clientesoporte import soporte
from clienteresena import crearresena
def main():
    opcion=0
    while(opcion!=9):
        print("----------------Bienvenido al sistema de menus UDP--------------------\n")
        print("1.Registrarse\n")
        print("2.Iniciar sesión\n")
        print("9.Salir\n")
        opcion=int(input("Seleccione una opción: "))

        if opcion==1:
            correo=str(input('Ingrese correo: '))
            clave=getpass.getpass('Ingresa clave: ')
            registro(correo,clave)
            print('\n')

        if opcion==2:
            print("\n")
            correo=str(input('Ingrese correo: '))
            clave=getpass.getpass('Ingresa clave: ')
            log=login(correo,clave)

            if log[0]==True and log[1]=='0':
                opcioncliente=None
                while(opcioncliente!=9):
                    print("-------------------------------Menu cliente------------------------------------")
                    print("1. Ver facultades\n")
                    print("2. Contactar a soporte técnico\n")
                    print("9. Salir\n")
                    opcioncliente=int(input("ingrese una opcion: \n"))
                    if opcioncliente==1:

                        facultades()

                        opcion=int(input("Seleccione una facultad o presione 9 para salir: \n"))
                        if opcion==9:
                            break
                        else:
                            vermenusfacultad(opcion)

                        menu=int(input("Seleccione un menú: \n"))

                        verdetallemenu(menu)

                        print("1. Crear reseña\n")
                        print("9. Salir\n")

                        opcionmenu=int(input("Seleccione una opcion: "))

                        if opcionmenu==1:

                            texto=str(input("Ingrese comentario sobre el menú: \n"))

                            puntuacion=str(input("Ingrese una puntuación del 1 al 5: \n"))

                            crearresena(puntuacion,texto,correo,opcionmenu)

                        elif opcion==9:
                            break

                    elif opcioncliente==2:
                        mensaje=str(input("ingrese mensaje para el soporte tecnico o presione 9 para salir: "))
                        if mensaje==9:
                            break
                        else:
                            soporte(correo,mensaje)
                        print("\n")

                    elif opcioncliente==9:
                        break




            elif log[0]==True and log[1]=='1':
                print("-------------------------------Menu administrador------------------------------")
                print("1. Agregar menú\n")
                print("2. Editar/eliminar menú\n")
                print("3. Agregar facultad")
                print("4. Editar/eliminar usuario\n")
                print("9. Salir")

            elif log[0]==True and log[1]=='2':
                print("-------------------------------Menu soporte------------------------------------")
                print("1. Bandeja de mensajes\n")
                print("2. Editar información de cuentas de usuario\n")
                print("9. Salir")
main()
