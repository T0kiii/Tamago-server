
# Tamago-server

Aplicación servidor que registra los cambios sobre una mascota virtual.

## Estructura de proyecto

Quiero que quede como indican en la [doc de Flask](https://flask.palletsprojects.com/en/2.2.x/tutorial/layout/)

```bash:
/home/user/Projects/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
├── setup.py
└── MANIFEST.in
```

He creado `setup.cfg` porque hasta en el repositorio tutorial han pasado los metadatos a `setup.cfg`. El resumen es para intentar evitar realizar import de dependencias a ciegas.
