/*Ejercicio 1*/
/*Determinar el salario máximo para el conjunto de todos los empleados*/
SELECT MAX(SALAR) AS salario_maximo
FROM temple;

/*Ejercicio 2*/
/*Averiguar el salario máximo para los empleados del departamento 100*/
SELECT MAX(SALAR) AS salario_maximo
FROM temple
WHERE NUMDE = 100;

/*Ejercicio 4*/
/*Hallar el nombre, la fecha de ingreso y los días trabajados hasta la fecha
actual de cada empleado del departamento 110, de mayor a menor*/
SELECT NOMEM,
FECIN,
DATEDIFF(NOW(),FECIN) AS dias_trabajados
FROM temple
WHERE NUMDE = 110
ORDER BY NOMEM DESC;

/*Ejercicio 5*/
/*Averiguar, de cada empleado del departamento 110: el nombre, la fecha
de ingreso y los días trabajados hasta el 01-11-2010, ordenados de más a
menos antigüedad*/
SELECT NOMEM,
FECIN,
DATEDIFF('2010-11-01',FECIN) AS dias_trabajados
FROM temple
WHERE NUMDE = 110
ORDER BY FECNA ASC;

/*Ejercicio 6*/
/*Obtener el número de semanas de diferencia entre el empleado que entró
primero y el que entró último en 1988*/
SELECT DATEDIFF(MAX(FECIN),MIN(FECIN))/7 AS semanas_diferencia
FROM temple;

/*Ejercicio 7*/
/*Determinar la edad en años cumplidos del empleado más viejo del
departamento 110*/
SELECT YEAR(NOW())-YEAR(MIN(FECNA)) AS años_cumplidos
FROM temple
WHERE NUMDE = 110;

/*Ejercicio 8*/
/*Contar el número de empleados de la empresa*/
SELECT COUNT(NOMEM) AS num_empleados
FROM temple;

/*Ejercicio 9*/
/*Hallar el número de empleados y de extensiones telefónicas (téngase en
cuenta que muchos empleados comparten teléfono) del departamento 112*/
SELECT COUNT(NOMEM) AS num_empleados,
COUNT(EXTEL) AS num_extensiones
FROM temple
WHERE NUMDE = 112;

/*Ejercicio 10*/
/*Calcular cuántos empleados hay cuya fecha de nacimiento sea anterior al año 1980*/
SELECT COUNT(NOMEM) AS num_empleados
FROM temple
WHERE FECNA < '1980-00-00';

/*Ejercicio 11*/
/*Conseguir del departamento 112: el número de empleados, cuántos
cobran comisión, y la suma y la media de sus comisiones*/
SELECT COUNT(NOMEM) AS num_empleados,
COUNT(COMIS) AS num_comisionados,
SUM(COMIS) AS suma_comisiones,
AVG(COMIS) AS media_comisiones
FROM temple;

/*Ejercicio 12*/
/*Calcular cuántas comisiones diferentes hay y su valor medio*/


/*Ejercicio 13*/
/*Determinar la edad media de los empleados del departamento 100*/
SELECT AVG(SUM(YEAR(NOW())-YEAR(MIN(FECNA)))) AS media_años_empleados
FROM temple
WHERE NUMDE = 100;

/*Ejercicio 14*/
/*Obtener la media del nº de hijos de los empleados del departamento 123*/
SELECT AVG(NUMHI) AS media_hijos
FROM temple
WHERE NUMDE = 123;