USE instituto;

/*Ejercicio 1*/
SELECT * FROM alumno WHERE id = 1;

/*Ejercicio 2*/
SELECT * FROM alumno WHERE teléfono = 692735409;

/*Ejercicio 3*/
SELECT * FROM alumno WHERE es_repetidor = 'sí';

/*Ejercicio 4*/
SELECT * FROM alumno WHERE es_repetidor = 'no';

/*Ejercicio 5*/
SELECT * FROM alumno WHERE fecha_nacimiento < '1993-01-01';