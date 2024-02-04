USE instituto;

/*Ejercicio 1*/
SELECT * FROM alumno WHERE fecha_nacimiento BETWEEN '1998-01-01' AND '1998-05-31';

/*Ejercicio 2*/
SELECT * FROM alumno WHERE fecha_nacimiento NOT BETWEEN '1998-01-01' AND '1998-05-31';