import os
from flask import Flask, jsonify, request
from . import db
from . import mascota
# from dotenv import load_dotenv

# load_dotenv()  # take environment variables from .env.

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'src.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    db.init_app(app)
    
    # Meter blueprints hace que no compile la aplicación al perder el app_context en db.py
    # from . import mascota
    # app.register_blueprint(mascota.bp)
    
    @app.route('/', methods=["GET"])
    def mostrar_masc():
        mascota_principal = mascota.get_mascota(mascota.NOMBRE_MASCOTA)
        
        if mascota_principal == None:
            return "No existe ninguna mascota"
        else:
            return mascota_principal
    
    # @app.route('/mascota', methods=["GET"])
    # def mostrar_mascotas():
    #     mascotas = mascota.get_all_mascotas()
    #     return mascotas
    
    @app.route('/mascota', methods=["GET"])
    def mostrar_mascotas():
        miMascota = mascota.get_mascota(mascota.NOMBRE_MASCOTA)
        return miMascota

    @app.route("/mascota", methods=["POST"])
    def recuperar_accion():
        peticion  = request.get_json()
        accion = peticion["accion"]
        return mascota.realizar_accion(accion)
    
    # @app.route("/mascota", methods=["POST"])
    # def crear_mascota():
    #     detalles_mascota  = request.get_json()
    #     nombre_mascota = detalles_mascota["nombre"]
    #     result = mascota.insert_mascota(nombre_mascota)
    #     return jsonify(result)

    # @app.route("/mascota", methods=["PUT"])
    # def update_masc():
    #     detalles_mascota  = request.get_json()
    #     masc = mascota.Mascota(
    #         detalles_mascota["nombre"],
    #         detalles_mascota["estaVivo"],
    #         detalles_mascota["salud"],
    #         detalles_mascota["hambre"],
    #         detalles_mascota["felicidad"],
    #         detalles_mascota["stamina"],
    #         detalles_mascota["higiene"],
    #         detalles_mascota["mood"]
    #     )
    #     result = mascota.update_mascota(masc)
    #     return jsonify(result)
    
    # @app.route("/mascota/<id>", methods=["DELETE"])
    # def borrar_masc():
    #     detalles_mascota  = request.get_json()
    #     id_mascota = detalles_mascota["id"]
    #     result = mascota.delete_mascota(id_mascota)
    #     return jsonify(result)
    
    """
    Enable CORS. Disable it if you don't need CORS
    """
    @app.after_request
    def after_request(response):
        response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
        response.headers["Access-Control-Allow-Credentials"] = "true"
        # response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
        response.headers["Access-Control-Allow-Methods"] = "POST, GET"
        response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
        return response
    
    return app


# FUNCIÓN MAIN
if __name__ == "__main__":
    app = create_app(test_config=None)
    app.run()
