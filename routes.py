from flask import Flask, render_template, request, redirect, url_for
import database
import models

app = Flask(__name__)

# --- RUTA PRINCIPAL (CATÁLOGO + HISTORIAL) ---
@app.route('/')
def index():
    # 1. Obtenemos los perros disponibles para el catálogo
    dogs_data = database.get_available_dogs()
    available_dogs = [models.Dog(row[0], row[1], row[2], row[3]) for row in dogs_data]
    
    # 2. Obtenemos el historial de adopciones para el panel del menú
    adoptions_history = database.get_adoption_history()
    
    # 3. Enviamos AMBAS listas al mismo template: catalogo.html
    return render_template('catalogo.html', dogs=available_dogs, adoptions=adoptions_history)


# --- RUTA PARA VER EL FORMULARIO DE UN PERRO ESPECÍFICO ---
@app.route('/adoptar/<int:dog_id>')
def adoptar(dog_id):
    dog_data = database.get_dog_by_id(dog_id)
    if dog_data:
        dog = models.Dog(dog_data[0], dog_data[1], dog_data[2], dog_data[3])
        return render_template('confirmacion.html', dog=dog)
    return redirect(url_for('index'))


# --- RUTA PARA PROCESAR EL FORMULARIO (POST) ---
@app.route('/confirmar_adopcion', methods=['POST'])
def confirmar_adopcion():
    # Recolectamos los datos del formulario
    dog_id = request.form['dog_id']
    name = request.form['name']
    lastname = request.form['lastname']
    id_card = request.form['id_card']
    address = request.form['address']

    # Intentamos registrar la transacción en MariaDB
    success = database.register_adoption_transactional(dog_id, name, lastname, address, id_card)
    
    if success:
        # Si sale bien, redirigimos al inicio para ver el historial actualizado
        return redirect(url_for('index') + '?adopted=1')
    else:
        return "<h1>❌ Error al procesar la adopción</h1><a href='/'>Volver al inicio</a>"


# --- BLOQUE DE EJECUCIÓN ---
if __name__ == '__main__':
    # Usamos host 0.0.0.0 para que puedas probarlo desde la IP de tu laptop
    app.run(debug=True, host='0.0.0.0', port=5000)