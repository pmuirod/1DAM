USE instituto;

/*Ejercicio 1*/
SELECT fecha_nacimiento,
DAY(fecha_nacimiento) AS dia,
MONTH(fecha_nacimiento) AS mes,
YEAR(fecha_nacimiento) AS año
FROM alumno;

/*Ejercicio 2*/
SELECT fecha_nacimiento,
DAYNAME(fecha_nacimiento) AS nombre_dia,
MONTHNAME(fecha_nacimiento) AS nombre_mes
FROM alumno;

/*Ejercicio 3*/
SELECT fecha_nacimiento,
- DATEDIFF(fecha_nacimiento,NOW()) AS diferencia_dias
FROM alumno;

/*Ejercicio 4*/
SELECT fecha_nacimiento,
TRUNCATE(- DATEDIFF(fecha_nacimiento,NOW())/365.25,0) AS edad
FROM alumno;