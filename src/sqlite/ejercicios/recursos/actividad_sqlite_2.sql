# sqlite3
# .open lenguas.db
# .read actividad_sqlite_2.sql

insert into LENGUA_MATERNA
values('cs', 'castellano', 'España');
insert into LENGUA_MATERNA(descripcion, nombre, abreviatura)
values('valenciano', 'C. Valenciana', 'va');
insert into LENGUA_MATERNA
values('en', 'inglés', 'Reino Unido');
insert into LENGUA_MATERNA
values('fr', 'Francés', 'Francia');

insert into PERSONA
values(111111111, 'Ana', 15, 'Morella', 165.0, 'cs');
insert into PERSONA
values(222222222, 'Pepito', 8, 'Elche', 132.0, 'cs');
insert into PERSONA
values(333333333, 'Mireia', 8, 'Manises', 170.0, 'va');
insert into PERSONA
values(444444444, 'Joan', 82, 'Oliva', 170.0, 'va');