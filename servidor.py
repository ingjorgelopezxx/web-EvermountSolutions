from flask import Flask, request, Response, jsonify, abort
import pyodbc
import mimetypes
import base64

app = Flask(__name__)

def conectar_sql():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=INGJORGELOPEZ\\SQLEXPRESS;'
        'DATABASE=FLET;'
        'UID=sa;'
        'PWD=1234'
    )

@app.route("/imagenes", methods=["GET"])
def lista_imagenes():
    con = conectar_sql()
    cursor = con.cursor()
    cursor.execute("SELECT nombre FROM Imagenes")
    filas = cursor.fetchall()
    con.close()
    return jsonify([fila[0] for fila in filas])

@app.route("/imagen/<nombre>", methods=["GET"])
def obtener_imagen(nombre):
    con = conectar_sql()
    cursor = con.cursor()
    cursor.execute("SELECT imagen FROM Imagenes WHERE nombre = ?", (nombre,))
    fila = cursor.fetchone()
    con.close()
    if fila and fila[0]:
        mime_type, _ = mimetypes.guess_type(nombre)
        return Response(fila[0], mimetype=mime_type or "image/jpeg")
    abort(404)

@app.route("/imagen/<nombre>", methods=["DELETE"])
def eliminar_imagen(nombre):
    try:
        con = conectar_sql()
        cursor = con.cursor()
        cursor.execute("DELETE FROM Imagenes WHERE nombre = ?", (nombre,))
        con.commit()
        con.close()
        return jsonify({"mensaje": f"Imagen '{nombre}' eliminada"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/upload_image", methods=["POST"])
def upload_image():
    data = request.json
    nombre = data.get("name")
    img_b64 = data.get("image_base64")

    if not nombre or not img_b64:
        return jsonify({"error": "Faltan datos"}), 400

    # Extraer solo la parte base64 (sin data:image/jpeg;base64,)
    if "," in img_b64:
        img_b64 = img_b64.split(",")[1]

    try:
        img_bin = base64.b64decode(img_b64)
    except Exception as e:
        return jsonify({"error": "Error al decodificar imagen", "detalle": str(e)}), 400

    try:
        con = conectar_sql()
        cursor = con.cursor()
        cursor.execute(
            "INSERT INTO Imagenes (nombre, imagen) VALUES (?, ?)",
            (nombre, pyodbc.Binary(img_bin))
        )
        con.commit()
        con.close()
    except Exception as e:
        return jsonify({"error": "Error al guardar en base de datos", "detalle": str(e)}), 500

    return jsonify({"message": "Imagen guardada correctamente"}), 200

if __name__ == "__main__":
    app.run(debug=True)
