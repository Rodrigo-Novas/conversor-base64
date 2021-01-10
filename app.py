from utils import base_to_text, text_to_base

from flask import Flask, render_template, request, url_for, jsonify
from werkzeug.utils import redirect
from werkzeug.exceptions import abort

import json

#la aplicacion se encargara de efectuar de convertir texto plano a base64

app = Flask(__name__)
app.config["SECRET_KEY"] = "llave_secreta"

@app.route("/", methods=['GET', "POST"])
@app.route("/home", methods=["GET", "POST"])
def inicio():
    app.logger.info("Pagina inicio")
    return render_template("home.html")


@app.route("/convertedbase", methods=["POST"])
def convertedBase():
    app.logger.info("Ingresa a post")
    if request.method == "POST":
        texto = request.form["texto"]
        app.logger.info(texto)
        converted_base64 = text_to_base(texto)
        return jsonify(Respuesta="Texto satisfactoriamente convertido a base64", Texto=texto, Base64=converted_base64)
    else:
        return jsonify(Respuesta="No puedo convertirse", excepcion=e)
    
@app.route("/convertedtext", methods=["POST"])
def convertedText():
    app.logger.info("Ingresa a post")
    try:
        if request.method == "POST":
            base = request.form["base"]
            app.logger.info(base)
            converted_base64 = base_to_text(base)
            return jsonify(Respuesta="Base64 convertido satisfactoriamente a texto", Texto=base, Base64=converted_base64)
    except Exception as e:
        return jsonify(Respuesta="No pudo convertirse")


@app.route("/converted")
def conversor():
    return render_template("converted.html")



if __name__ == "__main__":
    app.run(debug=True, port =4000)



