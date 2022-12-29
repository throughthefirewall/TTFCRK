"""
Autor:      ThroughTheFirewall  
Fecha:      29/12/2022
Descripción:

    Python: Ataques de Diccionario IV

    Librería que contiene los scripts para
    generar el diccionario con las posibles
    contraseñas.

Redes:
    YouTube:    @throughthefirewall
    Twitter:    @FirewallThrough
    Web:        www.throug-the-firewall.com
"""

lista_cadena = []

#Creamos los métodos que usaremos

def crear_diccionario(nombre_diccionario:str, longitud_lista:int, lista:list):
    lista_generada = generar_diccionario(longitud_lista, lista)
    contador = 0

    archivo = open(nombre_diccionario, 'w')
    
    for valores in lista_generada:
        archivo.write(valores + '\n')
        contador += 1

    return f"\n[+]Archivo {nombre_diccionario} generado.\n[+]Palabras Generadas: {contador}\n"


def generar_diccionario(longitud_lista:int, lista:list):
    if(longitud_lista == 1):
        cadena = ""
        #Agregamos los valores a la lista
        for valores in lista:
            cadena += str(valores)
        lista_cadena.append(cadena)
    else:
        for i in range(longitud_lista):
            generar_diccionario(longitud_lista - 1, lista)
            #Reemplazamos valores en la lista
            if(longitud_lista):
                lista[i], lista[longitud_lista - 1] = lista[longitud_lista - 1], lista[i]
            else:
                lista[0], lista[longitud_lista - 1] = lista[longitud_lista - 1], lista[0]
        return lista_cadena
