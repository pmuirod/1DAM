USE instituto

/*Ejercicio 1*/
SELECT LOWER(CONCAT_WS(' ', nombre, apellido1, apellido2)) AS nombre_completo FROM alumno;

/*Ejercicio 2*/
SELECT UPPER(CONCAT_WS(' ', nombre, apellido1, apellido2)) AS nombre_completo FROM alumno;

/*Ejercicio 3*/
SELECT UPPER(CONCAT(nombre, apellido1)) AS nombre_completo FROM alumno WHERE apellido2 IS NULL;
SELECT CONCAT_WS(' ', nombre, apellido1, apellido2) AS nombre_completo FROM alumno WHERE apellido2 IS NOT NULL;