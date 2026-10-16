--Crear base de datos
CREATE DATABASE IF NOT EXISTS mini_red_social CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

--Crear usuario específico para el proyecto (reemplaza 'tu_password' si lo deseas)
CREATE USER IF NOT EXISTS 'admin_red_social'@'localhost' IDENTIFIED BY 'admin1234';

--Asignar permisos completos del usuario sobre la base de datos
GRANT ALL PRIVILEGES ON mini_red_social.* TO 'admin_red_social'@'localhost';

--Aplicar los cambios de privilegios
FLUSH PRIVILEGES;