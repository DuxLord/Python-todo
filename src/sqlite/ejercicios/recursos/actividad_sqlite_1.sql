# sqlite3
# .open lenguas.db
# .read actividad_sqlite_1.sql
# .tables
# .schema LENGUA_MATERNA
# .schema PERSONA

create table LENGUA_MATERNA(
    abreviatura TEXT,
    nombre TEXT,
    descripcion TEXT,
    PRIMARY KEY(abreviatura)
);

create table PERSONA(
    dni INTEGER,
    nombre TEXT,
    edad INTEGER,
    ciudad TEXT,
    altura INTEGER,
    lengua TEXT,
    PRIMARY KEY(dni),
    FOREIGN KEY(lengua) REFERENCES LENGUA_MATERNA(abreviatura)
);