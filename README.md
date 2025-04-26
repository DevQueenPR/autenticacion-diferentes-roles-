# Proyecto: Gestión de Usuarios con Roles en Flask

## Descripción
Aplicación web desarrollada en Python Flask que permite el manejo de usuarios con diferentes roles (Admin y User).  
El administrador tiene acceso especial para visualizar una tabla de usuarios, mientras que los usuarios estándar solo pueden acceder a su propio dashboard.

## Características
- **Autenticación de usuarios** con nombre de usuario y contraseña.
- **Autorización basada en roles** (Admin y User).
- **Control dinámico de la interfaz** (el administrador puede ver opciones ocultas para usuarios normales).
- **Protección de rutas en el back-end** para evitar accesos no autorizados.
- **Mensajes de error** para credenciales incorrectas o accesos prohibidos.

## Tecnologías Utilizadas
- Python 3
- Flask
- Flask-Login 
- HTML / Jinja2 / Boostrap (para las plantillas)

## Flujograma del proyecto

![image](https://github.com/user-attachments/assets/7614bc34-9504-4051-a57b-40e8ab521689)


## Funcionalidades 

### Home 
Pide que el usuario inicie sessión.

![image](https://github.com/user-attachments/assets/527ce5dd-f078-4652-a8d0-853a21a30e62)

### Login 
Lugar donde se inicia session, se pide nombre y password.

![image](https://github.com/user-attachments/assets/ba5f7f24-e962-4d81-a5da-e14716057283)

Mensaje de credenciales incorectas. 

![image](https://github.com/user-attachments/assets/e5bb7376-db4e-44d7-a849-b43edac3d13c)

### Dashboard 
Autenticación de un usuario.

![image](https://github.com/user-attachments/assets/1761843b-4ff3-472f-a710-f6d29e9ee68d)

Autenticación de un admin.

![image](https://github.com/user-attachments/assets/3e2bf736-668f-47db-bc04-d0be4b9666af)


## Logout
Libera credenciales guardadas en la sessión.

![image](https://github.com/user-attachments/assets/efed2808-f52a-4759-b3d1-0200375a14c2)
