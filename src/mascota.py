import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from src.db import get_db

bp = Blueprint('mascota', __name__, url_prefix='/')

class Mascota():

    nombre = "Paco"
    estaVivo = 1
    salud = 0.00
    hambre = 0.00
    felicidad = 0.00
    stamina = 0.00
    higiene = 0.00
    mood = 0.00

    #Constructor de la clase por defecto
    def  __init__ (self):
        self.estaVivo = 1
        self.salud = 100.00
        self.hambre = 0.00
        self.felicidad = 100.00
        self.stamina = 100.00
        self.higiene = 100.00
        self.mood = 100.00
    
    #Constructor de la clase con nombre
    def  __init__ (self, nombre):
        self.nombre = nombre
        self.estaVivo = 1
        self.salud = 100.00
        self.hambre = 0.00
        self.felicidad = 100.00
        self.stamina = 100.00
        self.higiene = 100.00
        self.mood = 100.00
    
    def alimentar(self):
        self.hambre -= 10.00
    
    def jugar(self):
        if(self.stamina <= 10.00):
            print()
            return
        if(self.stamina >= 10.00 and  self.felicidad <= 10.00):
            self.stamina -= 10.00
            self.felicidad += 10.00
    
    def limpiar(self):
        self.higiene += 10.00


def insert_mascota(masc_nombre):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO mascota(mas_nombre, mas_estaVivo, mas_salud, mas_hambre, mas_felicidad, mas_stamina, mas_higiene, mas_mood) VALUES (?, ?, ?, ?,?, ?, ?, ?)"
    cursor.execute(statement,
                   [masc_nombre,
                    1,
                    100,
                    0,
                    70,
                    70,
                    80,
                    50]
                   )
    db.commit()
    return True

def crear_masc_test():
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO mascota(mas_nombre, mas_estaVivo, mas_salud, mas_hambre, mas_felicidad, mas_stamina, mas_higiene, mas_mood) VALUES (?, ?, ?, ?,?, ?, ?, ?)"
    cursor.execute(statement,
                   ["Paco",
                    1,
                    0.00,
                    0.00,
                    0.00,
                    0.00,
                    0.00,
                    0.00]
                   )
    db.commit()
    return True


def update_mascota(mascota, ID_MASCOTA):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE mascota SET name = ?, price = ?, rate = ? WHERE mas_id = ?"
    statement = "UPDATE mascota SET mas_nombre = ?, mas_estaVivo = ?, mas_salud = ?, mas_hambre = ?, mas_felicidad = ?, mas_stamina = ?, mas_higiene = ?, mas_mood = ? WHERE mas_id = ?"
    cursor.execute(statement,
                [mascota.nombre,
                mascota.estaVivo,
                mascota.salud,
                mascota.hambre,
                mascota.felicidad,
                mascota.stamina,
                mascota.higiene,
                mascota.mood,
                ID_MASCOTA]
                )
    db.commit()
    return True

def delete_mascota(ID_MASCOTA):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM mascota WHERE mas_id = ?"
    cursor.execute(statement, [ID_MASCOTA])
    db.commit()
    return True

def get_by_id(ID_MASCOTA):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT mas_nombre, mas_estaVivo, mas_salud, mas_hambre, mas_felicidad, mas_stamina, mas_higiene, mas_mood FROM mascota WHERE mas_id = ?"
    cursor.execute(statement, [ID_MASCOTA])
    return cursor.fetchone()

def get_mascota_id(nombre_mascota):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT mas_id FROM mascota WHERE mas_nombre = ?"
    cursor.execute(statement, [nombre_mascota])
    return cursor.fetchone()

def get_mascotas():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM mascota"
    cursor.execute(query)
    return cursor.fetchall()

