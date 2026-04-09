#Centro de Adopción "Huellitas"
[imagenes del proyecto](./imagenes/)



Aplicación web para gestionar la adopción de perros. Permite visualizar un catálogo de perros disponibles, registrar adoptantes y llevar un historial de adopciones, todo conectado a una base de datos MySQL.

## Tecnologías utilizadas

- **Python 3.12**
- **Flask 3.1** — framework web
- **MySQL / mysql-connector-python** — base de datos relacional
- **Jinja2** — motor de plantillas HTML
- **HTML + CSS** — frontend 

## Estructura del proyecto


### Estructura del Proyecto

```text
doggis/
├── config.py          # Configuración y conexión a la base de datos
├── database.py        # Funciones de acceso a datos (queries SQL)
├── models.py          # Clases del dominio: Dog y Adopter
├── routes.py          # Rutas Flask (controlador principal)
├── main.py            # Punto de entrada de la app
├── setup_db.py        # Script de inicialización de la base de datos
├── templates/
│   ├── catalogo.html      # Vista principal: perros disponibles + historial
│   ├── confirmacion.html   # Vista del formulario de adopción
│   └── historial.html      # Vista del historial de adopciones
└── static/
    └── style.css      # Estilos globales




## Base de datos

La base de datos se llama `centroAtencion` y contiene tres tablas:

- **Dog** — perros disponibles para adopción (`id`, `name`, `age`, `breed`, `adopted`)
- **Adopter** — personas que adoptan (`adopter_id`, `name`, `lastName`, `address`, `id_card`)
- **Adoption** — relación entre perros y adoptantes con fecha (`dog_id`, `adopter_id`, `date`)

---

## Instalación y uso

### 1. Clonar el repositorio


git clone https://github.com/IsaacMrtz/POO.git
cd POO/doggis


### 2. Crear y activar el entorno virtual


python -m venv .venv
source .venv/bin/activate        # Linux / Mac
.venv\Scripts\activate           # Windows


### 3. Instalar dependencias


pip install flask mysql-connector-python


### 4. Configurar la base de datos

Edita el archivo `config.py` con tus credenciales de MySQL:


DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "tu_usuario",
    "password": "tu_contraseña",
    "database": "centroAtencion"
}


Luego crea la base de datos y las tablas ejecutando `setup_db.py` (si está implementado) o manualmente en MySQL.

### 5. Ejecutar la aplicación


python routes.py


La app estará disponible en:  http://127.0.0.1:5000 o http://10.11.132.186:5000


## ✨ Funcionalidades

- Catálogo de perros disponibles (solo los no adoptados)
- Formulario de adopción con datos del adoptante
- Registro transaccional: si algo falla, se revierte toda la operación
- Historial de adopciones ordenado por fecha
- Interfaz sencilla y responsiva

- El proyecto incluye la carpeta `.venv/` en el ZIP; al clonar desde GitHub, instala las dependencias manualmente con `pip instal
