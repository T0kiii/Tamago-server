import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from src.db import get_db

bp = Blueprint('mascota', __name__, url_prefix='/')

NOMBRE_MASCOTA = "Michi"
ACCIONES_MASCOTA = ["ALIMENTAR", "JUGAR", "LIMPIAR", "CREAR", "BORRAR"]

class Mascota():
    """
    Objeto donde se manejan los datos de la mascota.
    Las funciones que modifican los atributos guardan los cambios en BD
    Atributos:
        a: an integer
        b: an integer
        nombre: str. Nombre de la masctoa
        estaVivo: sqlite3 int boolean: 0 false(muerta), 1 true(viva) 
        salud: int. Puntos de vida de la mascota. Si llega a 0, muere.
        hambre: int. Hambre de la mascota. Si llega a 100, muere.
        felicida: int. Felicidad de la mascota
        stamina: int. Energía de la mascota.
        higiene: int. Grado de limpieza de la mascota
        mood: int.
    Funciones importantes:
        realizar_accion(accion): Según la acción recibida, llama a las funciones correspondientes.
    """

    nombre: str = NOMBRE_MASCOTA
    estaVivo: int = 0 # sqlite3 boolean: 0 false, 1 true
    salud: int = 0
    hambre: int = 0
    felicidad: int = 0
    stamina: int = 0
    higiene: int = 0
    mood: int = 0

    #Constructor de la clase por defecto
    def  __init__ (self):
        self.estaVivo = 1
        self.salud = 100
        self.hambre = 0
        self.felicidad = 100
        self.stamina = 100
        self.higiene = 100
        self.mood = 100
    
    #Constructor de la clase con nombre
    def  __init__ (self, nombre: str):
        self.nombre = nombre
        self.estaVivo = 1
        self.salud = 100
        self.hambre = 0
        self.felicidad = 100
        self.stamina = 100
        self.higiene = 100
        self.mood = 100
    
    # toString de la clase
    def __str__(self):
        respuesta = '''
        nombre: {nombre}
        estaVivo: {estaVivo}
        salud: {salud}
        hambre: {hambre}
        felicidad: {felicidad}
        stamina: {stamina}
        higiene: {higiene}
        mood: {mood}
        '''.format(
            nombre = self.nombre,
            estaVivo = self.estaVivo,
            salud = self.salud,
            hambre = self.hambre,
            felicidad = self.felicidad,
            stamina = self.stamina,
            higiene = self.higiene,
            mood = self.mood
        )
        return respuesta

    
    # ACCIONES de la mascota
    
    def alimentar(self):
        self.hambre -= 10

        update_mascota(self)
    
    def jugar(self):
        if(self.stamina <= 10):
            print("Está muy cansada")
            return "Está muy cansada"
        if(self.stamina >= 10 and  self.felicidad <= 10):
            self.stamina -= 10
            self.felicidad += 10
        
        update_mascota(self)
    
    def limpiar(self):
        self.higiene += 10
        
        update_mascota(self)


def arrancar_mascota():
    #TODO: comprobar si existen datos previos de mascota. Si no hay, crear una nueva
    mascota_bd = get_mascota(NOMBRE_MASCOTA)
    
    # TODO: comprobar en qué formato @mascBd 
    # Si no existe la mascota, se crea una
    if len(mascota_bd) == 0:
        mascota = Mascota()
        exito = insert_mascota(mascota)
        
        if not exito:
            print("No se ha creado la mascota")
    else:
        mascota = Mascota(
            mascota_bd["mas_nombre"],
            mascota_bd["mas_estaVivo"],
            mascota_bd["mas_salud"],
            mascota_bd["mas_hambre"],
            mascota_bd["mas_felicidad"],
            mascota_bd["mas_stamina"],
            mascota_bd["mas_higiene"],
            mascota_bd["mas_mood"]
        )
    
    return mascota


def insert_mascota(mascota: Mascota):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO mascota(mas_nombre, mas_estaVivo, mas_salud, mas_hambre, mas_felicidad, mas_stamina, mas_higiene, mas_mood) VALUES (?, ?, ?, ?,?, ?, ?, ?)"
    cursor.execute(statement,
                   [
                    mascota.nombre,
                    mascota.estaVivo,
                    mascota.salud,
                    mascota.hambre,
                    mascota.felicidad,
                    mascota.stamina,
                    mascota.higiene, 
                    mascota.mood
                   ]
                   )
    db.commit()
    return True


def update_mascota(mascota: Mascota):
    db = get_db()
    cursor = db.cursor()
    # statement = "UPDATE mascota SET name = ?, price = ?, rate = ? WHERE mas_id = ?"
    statement = "UPDATE mascota SET mas_nombre = ?, mas_estaVivo = ?, mas_salud = ?, mas_hambre = ?, mas_felicidad = ?, mas_stamina = ?, mas_higiene = ?, mas_mood = ? WHERE mas_nombre = ?"
    cursor.execute(statement,
                [mascota.nombre,
                mascota.estaVivo,
                mascota.salud,
                mascota.hambre,
                mascota.felicidad,
                mascota.stamina,
                mascota.higiene,
                mascota.mood,
                mascota.nombre]
                )
    db.commit()
    return True


def delete_mascota(nombre_mascota):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM mascota WHERE mas_nombre = ?"
    cursor.execute(statement, [nombre_mascota])
    db.commit()
    return True


def get_mascota(nombre_mascota) -> Mascota:
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT mas_nombre, mas_estaVivo, mas_salud, mas_hambre, mas_felicidad, mas_stamina, mas_higiene, mas_mood FROM mascota WHERE mas_nombre = ?"
    cursor.execute(statement, [nombre_mascota])
    mas_nombre, mas_estaVivo, mas_salud, mas_hambre, mas_felicidad, mas_stamina, mas_higiene, mas_mood = cursor.fetchone()
    
    mascota_bd = Mascota(mas_nombre)
    mascota_bd.estaVivo = mas_estaVivo
    mascota_bd.salud = mas_salud
    mascota_bd.hambre = mas_hambre
    mascota_bd.felicidad = mas_felicidad
    mascota_bd.stamina = mas_stamina
    mascota_bd.higiene = mas_higiene
    mascota_bd.mood = mas_mood
    
    return mascota_bd


def get_all_mascotas():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM mascota"
    cursor.execute(query)
    return cursor.fetchall()


def realizar_accion(accion: str):
    if accion not in ACCIONES_MASCOTA:
        print("Acción inválida")
        return "Acción inválida"
    
    match accion:
        case "ALIMENTAR":
            print("Mascota alimentada")
            # TODO: Llamar a alimentar()
            return "Mascota alimentada"
        case "JUGAR":
            print("Has jugado con la mascota")
            # TODO: Llamar a jugar()
            return "Has jugado con la mascota"
        case "LIMPIAR":
            print("La mascota está limpita")
            # TODO: Llamar a limpiar()
            return "La mascota está limpita"
        case "CREAR":
            print("Mascota creada")
            # TODO: Llamar a insert_mascota()
            return "Mascota creada"
        case "BORRAR":
            print("Mascota borrada")
            # TODO: Llamar a delete_mascota()
            return "Mascota borrada"
