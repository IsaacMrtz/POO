import mysql.connector
import config

# --- FUNCIÓN PARA EL CATÁLOGO (PERROS DISPONIBLES) ---
def get_available_dogs():
    conn = config.get_db_connection()
    cur = conn.cursor()
    # Solo seleccionamos los perros que NO han sido adoptados (adopted = FALSE)
    cur.execute("SELECT id, name, age, breed FROM Dog WHERE adopted = FALSE")
    dogs_data = cur.fetchall()
    conn.close()
    return dogs_data

# --- FUNCIÓN PARA VER DETALLES DE UN PERRO ANTES DE ADOPTAR ---
def get_dog_by_id(dog_id):
    conn = config.get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, age, breed FROM Dog WHERE id = %s", (dog_id,))
    dog = cur.fetchone()
    conn.close()
    return dog

# --- FUNCIÓN TRANSACCIONAL (REGISTRA ADOPTANTE Y ADOPCIÓN AL MISMO TIEMPO) ---
def register_adoption_transactional(dog_id, name, lastname, address, id_card):
    conn = config.get_db_connection()
    cur = conn.cursor()
    try:
        # 1. Insertamos al adoptante en la tabla Adopter
        # Usamos 'name' y 'lastName' para que coincida con el SELECT del historial
        cur.execute("""
            INSERT INTO Adopter (name, lastName, address, id_card) 
            VALUES (%s, %s, %s, %s)
        """, (name, lastname, address, id_card))
        adopter_id = cur.lastrowid

        # 2. Registramos la relación en la tabla Adoption
        cur.execute("""
            INSERT INTO Adoption (dog_id, adopter_id, date) 
            VALUES (%s, %s, NOW())
        """, (dog_id, adopter_id))

        # 3. Actualizamos el estado del perro a adoptado (TRUE)
        cur.execute("UPDATE Dog SET adopted = TRUE WHERE id = %s", (dog_id,))

        # Si todo salió bien, guardamos los cambios permanentemente
        conn.commit()
        return True
    except Exception as e:
        # Si algo falla (ej: error de conexión), deshacemos los cambios parciales
        conn.rollback()
        print(f"Error en la transacción: {e}")
        return False
    finally:
        conn.close()

# --- FUNCIÓN PARA EL PANEL DE HISTORIAL (EL MENÚ EN EL CATÁLOGO) ---
def get_adoption_history():
    conn = config.get_db_connection()
    cur = conn.cursor()
    # Esta consulta une las 3 tablas para mostrar nombres en lugar de IDs
    # d.name = nombre perro | a.name = nombre adoptante | a.lastName = apellido
    query = """
        SELECT d.name, a.name, a.lastName, ad.date 
        FROM Adoption ad
        JOIN Dog d ON ad.dog_id = d.id
        JOIN Adopter a ON ad.adopter_id = a.adopter_id
        ORDER BY ad.date DESC
    """
    try:
        cur.execute(query)
        history = cur.fetchall()
        return history
    except Exception as e:
        print(f"Error al obtener historial: {e}")
        return []
    finally:
        conn.close()