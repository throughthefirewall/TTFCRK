"""
Autor:      ThroughTheFirewall
Fecha:      16/12/2022
Descripción:

    Python:Ataques de Diccioanario I

    En esta primera parte crearemos el menu con
    el cual podremos dar las opciones para 
    realizar el ataque de diccionario

Redes:
    YouTube:    @throughthefirewall
    Twitter:    @FirewallThrough
    Web:        www.throughthefirewall.com
"""

#Importamos las librerias que usaremos
import sys

#Crearemos el mensaje que contiene el modo de uso del programa
mensaje = """
Uso:    python ttfcrk.py -h
        python ttfcrk.py -s smtp -e email.email@email.com -d diccionario.txt
        python ttfcrk.py -s ssh -p 22 -u admin -d diccionario

    --servicio/-s        ->Servicio sobre el cual realizaremos el ataque de diccionario
    --help/-h           ->Despliega el menu con el modo de uso del programa

SMTP:

    --email/-e          ->Email de la cuenta a la cual realizaremos el ataque de diccionario
    --diccionario/-d    ->Diccionario que contiene la posible clave del email

SSH:
    --puerto/-p         ->Puerto del protocolo SSH
    --usuario/-u           ->Usuario al cual nos conectaremos por medio del protocolo SSH
    --diccionario/-d    ->Diccionario que contiene la posible clave del email
"""

def main():
    #Creamos las opciones sobre los servicios que usaremos
    try:
        if(sys.argv[1] == "-s" or sys.argv[1] == "--servicio"):
            if(sys.argv[2] == "smtp"):
                if(sys.argv[3] == "-e" or sys.argv[3] == "--email" and
                        sys.argv[5] == "-d" or sys.argv[5] == "--diccionario"):
                    print(f"Datos Ingresados: {sys.argv[4]} {sys.argv[6]}")
            elif(sys.argv[1] == "ssh"):
                if(sys.argv[3] == "-p" or sys.argv[3] == "--puerto" and
                        sys.argv[5] == "-u" or sys.argv[5] == "--usuario" and
                        sys.argv[7] == "-d" or sys.argv[7] == "--diccionario"):
                    print(f"Datos Ingresados: {sys.argv[4]} {sys.argv[6]} {sys.argv[8]}")
            else:
                print(mensaje)
                exit()
        elif(sys.argv[1] == "--help" or sys.argv[1] == "-h"):
            print(mensaje)
            exit()
        else:
            print("El servicio no se encuentra disponible...\n",mensaje)
            exit()
    #Con esta excepción manejos los parametros que no fueron completados correctamente.
    except IndexError:
        print("Parametros incompletos...\n",mensaje)
        exit()

if __name__ == "__main__":
    #Si los parametros asignados por el usuario son menores a 2, cerramos el programa
    if(len(sys.argv) < 2):
        pass
        exit()
    main()


