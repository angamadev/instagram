# Instagram Clone

Bienvenido al repositorio del proyecto **Instagram Clone**. Este proyecto es una aplicación basada en la funcionalidad principal de Instagram, que permite a los usuarios compartir imágenes, seguir a otros usuarios y explorar contenido, creado en Djago.

## 🚀 Características

- Registro e inicio de sesión de usuarios.
- Publicación de imágenes con descripciones.
- Feed principal con publicaciones de usuarios seguidos.
- Función de "Me gusta" en las publicaciones.
- Seguimiento de otros usuarios.
- Exploración de contenido popular.

---

## 📋 Requisitos previos

Asegúrate de tener los siguientes requisitos instalados en tu máquina antes de continuar:

1. **Python** (v3.8 o superior)
2. **Django** (v3.2 o superior)
3. **Git** (para clonar el repositorio)
4. **NPM** o **Yarn** (para manejar dependencias de JavaScript, si es necesario)

---

## ⚙️ Instalación

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local:

1. Clona este repositorio:

   ```bash
   git clone https://github.com/angamadev/instagram.git
   ```

2. Navega al directorio del proyecto:

   ```bash
   cd Instagram
   ```

3. Crea y activa un entorno virtual:

   ```bash
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   ```

4. Instala las dependencias de Python:

   ```bash
   pip install -r requirements.txt
   ```

5. Realiza las migraciones de la base de datos:

   ```bash
   python manage.py migrate
   ```

6. Inicia el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

7. Abre tu navegador y visita:

   ```
   http://127.0.0.1:8000
   ```

---

## 🛠️ Tecnologías utilizadas

- **Backend:** Django (framework de Python).
- **Frontend:** HTML, CSS, y JavaScript para consultas asíncronas.
- **Base de datos:** Base de datos por defecto de Django (SQLite).

---

## 🧪 Pruebas

Ejecuta las pruebas para asegurarte de que el proyecto funciona correctamente:

```bash
python manage.py test
```

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor, sigue los pasos a continuación:

1. Haz un fork del repositorio.
2. Crea una rama con tu funcionalidad o corrección:

   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```

3. Realiza los cambios y realiza un commit:

   ```bash
   git commit -m "Agrega una nueva funcionalidad"
   ```

4. Envía los cambios a tu fork:

   ```bash
   git push origin feature/nueva-funcionalidad
   ```

5. Abre un Pull Request en este repositorio.

---

## 📧 Contacto

Si tienes alguna pregunta o comentario, no dudes en ponerte en contacto:

- **GitHub:** [@angamadev](https://github.com/angamadev)
- **Correo electrónico:** angamadev@gmail.com

¡Gracias por visitar este proyecto! 🎉
