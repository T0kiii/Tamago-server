from flask import Flask
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)

@app.route('/')


# Esta función correrá nuestro servidor en el server de Flask
def arranca_tamago_server():

    # TODO: Comprobar si existen datos previos
    # TODO: Si no existen crear fichero de datos
    # TODO: Si existen cargar datos y arrancar mascota

    # TODO: Si existen cargar datos y arrancar mascota
    # TODO: Escuchar eventos, registrar cambios

    return hola()

def hola():
    return 'holi holu!'

# Solo queremos cargar los datos al arrancar el server e ir guardando periódicamente
def cargar_datos():
    return 'holi holu!'
def guardar_datos():
    return 'holi holu!'


# FUNCIÓN MAIN
if __name__ == "__main__":
   app.run()
