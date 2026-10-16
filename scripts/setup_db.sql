
CREATE DATABASE IF NOT EXISTS mini_red_social
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE red_social;


CREATE TABLE perfil_acceso (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(255) NULL,
    habilitado BOOLEAN NOT NULL DEFAULT TRUE
) ENGINE=InnoDB;

CREATE TABLE usuario (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    rut VARCHAR(12) NOT NULL UNIQUE,
    nombre VARCHAR(150) NOT NULL,
    correo VARCHAR(150) NOT NULL UNIQUE,
    contrasenia VARCHAR(128) NOT NULL,
    perfil_id BIGINT NOT NULL,
    habilitado BOOLEAN NOT NULL DEFAULT TRUE,
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
        ON UPDATE CURRENT_TIMESTAMP(6),

    CONSTRAINT fk_usuario_perfil
        FOREIGN KEY (perfil_id)
        REFERENCES perfil_acceso(id)
        ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE publicacion (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    autor_id BIGINT NOT NULL,
    contenido LONGTEXT NOT NULL,
    visibilidad VARCHAR(20) NOT NULL DEFAULT 'Publica',
    estado VARCHAR(30) NOT NULL DEFAULT 'Activa',
    habilitado BOOLEAN NOT NULL DEFAULT TRUE,
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
        ON UPDATE CURRENT_TIMESTAMP(6),

    CONSTRAINT fk_publicacion_autor
        FOREIGN KEY (autor_id)
        REFERENCES usuario(id)
        ON DELETE CASCADE,

    CONSTRAINT chk_publicacion_visibilidad
        CHECK (visibilidad IN ('Publica', 'Privada')),

    CONSTRAINT chk_publicacion_estado
        CHECK (estado IN ('Activa', 'Bloqueada', 'Archivada'))
) ENGINE=InnoDB;

CREATE TABLE interaccion (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    usuario_id BIGINT NOT NULL,
    publicacion_id BIGINT NOT NULL,
    tipo_interaccion VARCHAR(20) NOT NULL,
    comentario LONGTEXT NULL,
    habilitado BOOLEAN NOT NULL DEFAULT TRUE,
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),

    CONSTRAINT fk_interaccion_usuario
        FOREIGN KEY (usuario_id)
        REFERENCES usuario(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_interaccion_publicacion
        FOREIGN KEY (publicacion_id)
        REFERENCES publicacion(id)
        ON DELETE CASCADE,

    CONSTRAINT chk_interaccion_tipo
        CHECK (
            tipo_interaccion IN ('Like', 'Comentario', 'Compartir')
        )
) ENGINE=InnoDB;

CREATE TABLE registro_auditoria (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    usuario_responsable_id BIGINT NULL,
    accion_realizada VARCHAR(100) NOT NULL,
    tabla_afectada VARCHAR(50) NOT NULL,
    id_registro_afectado INT NOT NULL,
    detalle LONGTEXT NULL,
    fecha_evento DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),

    CONSTRAINT fk_auditoria_usuario
        FOREIGN KEY (usuario_responsable_id)
        REFERENCES usuario(id)
        ON DELETE CASCADE
) ENGINE=InnoDB;
