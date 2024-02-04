USE instituto;

/*Ejercicio 1*/
SELECT nombre, REVERSE (nombre) AS nombre_invertido 
FROM alumno;

/*Ejercicio 2*/
SELECT CONCAT_WS(' ', nombre, apellido1, apellido2) AS nombre_completo, 
REVERSE (CONCAT_WS(' ', nombre, apellido1, apellido2)) AS nombre_completo_al_revés 
FROM alumno;

/*Ejercicio 3*/
SELECT UPPER(CONCAT_WS(' ', nombre, apellido1, apellido2)) AS nombre_completo_mayuscula, 
LOWER(REVERSE (CONCAT_WS(' ', nombre, apellido1, apellido2))) AS nombre_completo_al_revés_minuscula 
FROM alumno;

/*Ejercicio 4*/
SELECT CONCAT(nombre, ' ', apellido1, ' ', apellido2) AS nombre_completo, 
CHAR_LENGTH(CONCAT(nombre, ' ', apellido1, ' ', apellido2)) AS numero_caracteres, 
LENGTH(CONCAT(nombre, ' ', apellido1, ' ', apellido2)) AS bytes_caracteres 
FROM alumno;

/*Ejercicio 5*/
SELECT CONCAT_WS(' ', nombre, apellido1, apellido2) AS nombre_completo, 
LOWER(CONCAT(nombre, '.', apellido1, '@iescelia.org')) AS correo_electrónico 
FROM alumno;

/*Ejercicio 6*/
SELECT CONCAT_WS(' ', nombre, apellido1, apellido2) AS nombre_completo, 
LOWER(CONCAT(nombre, '.', apellido1, '@iescelia.org')) AS correo_electrónico, 
LOWER(CONCAT(REVERSE (apellido2), SUBSTRING(fecha_nacimiento, 1, 4))) AS contraseña 
FROM alumno;