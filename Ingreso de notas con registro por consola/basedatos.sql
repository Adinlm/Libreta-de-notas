CREATE DATABASE IF NOT EXISTS master_python;
use master_python;

CREATE TABLE usuarios(
id          int(255) auto_increment not null,
nombre      varchar(100),
apellidos   varchar(255),
email       varchar(255) not null,
password    varchar(255) not null,
fecha       date not null,

---Asigna la primary key a id
CONSTRAINT pk_usuario PRIMARY KEY(id),
---Crea una  restriccion llamada uq_email para que el email no se pueda repetir entre usuarios
CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE notas(
id          int(255) auto_increment not null,
usuario_id  int(255) not null,
titulo      varchar(255) not null,
descripcion MEDIUMTEXT,
fecha       date not null,
CONSTRAINT pk_notas PRIMARY KEY(id),
---relaciona el campo usuario id en la tabla notas con id en la tabla usuarios
CONSTRAINT fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE=InnoDb;
