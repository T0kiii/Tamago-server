-- Script para generar esctructura de la base de datos

DROP TABLE IF EXISTS mascota;
-- DROP TABLE IF EXISTS post;

CREATE TABLE mascota (
  -- mas_id INTEGER PRIMARY KEY AUTOINCREMENT,
  mas_nombre TEXT PRIMARY KEY,
  -- SQLite does not have a separate Boolean storage class. Instead, Boolean values are stored as integers 0 (false) and 1 (true).
  mas_estaVivo INTEGER UNIQUE NOT NULL,
  mas_salud REAL UNIQUE NOT NULL,
  mas_hambre REAL UNIQUE NOT NULL,
  mas_felicidad REAL UNIQUE NOT NULL,
  mas_stamina REAL UNIQUE NOT NULL,
  mas_higiene REAL UNIQUE NOT NULL,
  mas_mood REAL NOT NULL
);

INSERT INTO mascota(
  mas_nombre, mas_estaVivo, mas_salud, mas_hambre, mas_felicidad, mas_stamina, mas_higiene, mas_mood
  ) 
VALUES ("Michi", 1, 100.00, 10.00, 70.00, 70, 80.00, 70)

-- CREATE TABLE post (
--   id INTEGER PRIMARY KEY AUTOINCREMENT,
--   author_id INTEGER NOT NULL,
--   created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
--   title TEXT NOT NULL,
--   body TEXT NOT NULL,
--   FOREIGN KEY (author_id) REFERENCES user (id)
-- );

