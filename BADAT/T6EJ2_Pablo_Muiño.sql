/*Ejercicio 1*/
/*Calcula la suma del presupuesto de todos los departamentos*/
SELECT SUM(presupuesto) AS suma_presupuestos
FROM departamento;

/*Ejercicio 2*/
/*Calcula la media del presupuesto de todos los departamentos*/
SELECT AVG(presupuesto) AS media_presupuestos
FROM departamento;

/*Ejercicio 3*/
/*Calcula el valor mínimo del presupuesto de todos los departamentos*/
SELECT MIN(presupuesto) AS min_presupuestos
FROM departamento;

/*Ejercicio 4*/
/*Calcula el nombre del departamento y el presupuesto que tiene asignado, del departamento con menor presupuesto*/
SELECT nombre, presupuesto
FROM departamento
WHERE presupuesto = (SELECT MIN(presupuesto) FROM departamento);

/*Ejercicio 5*/
/*Calcula el valor máximo del presupuesto de todos los departamentos*/
SELECT MAX(presupuesto) AS max_presupuestos
FROM departamento;

/*Ejercicio 6*/
/*Calcula el nombre del departamento y el presupuesto que tiene asignado, del departamento con mayor presupuesto*/
SELECT nombre, presupuesto
FROM departamento
WHERE presupuesto = (SELECT MAX(presupuesto) FROM departamento);

/*Ejercicio 7*/
/*Calcula el número total de empleados que hay en la tabla empleado*/
SELECT COUNT(*) AS num_empleados
FROM empleado;

/*Ejercicio 8*/
/*Calcula el número de empleados que no tienen NULL en su segundo apellido*/
SELECT COUNT(apellido2) AS empleados_sin_2_apellido
FROM empleado;

/*Ejercicio 9*/
/*Calcula el número de empleados que hay en cada departamento. Tienes que devolver dos columnas, una con el nombre 
del departamento y otra con el número de empleados que tiene asignados*/
SELECT departamento.nombre, COUNT(id_departamento) AS num_empleados
FROM departamento, empleado
WHERE id_departamento = departamento.id
GROUP BY departamento.nombre;

/*Ejercicio 10*/
/*Calcula el nombre de los departamentos que tienen más de 2 empleados. El resultado debe tener dos columnas, 
una con el nombre del departamento y otra con el número de empleados que tiene asignados*/
SELECT departamento.nombre, COUNT(empleado.id) AS num_empleados
FROM departamento LEFT JOIN empleado
ON departamento.id = empleado.id_departamento
GROUP BY departamento.nombre
HAVING COUNT(empleado.id) > 2;

/*Ejercicio 11*/
/*Calcula el número de empleados que trabajan en cada uno de los departamentos. El resultado de esta consulta también
tiene que incluir aquellos departamentos que no tienen ningún empleado asociado*/


/*Ejercicio 12*/
/*Calcula el número de empleados que trabajan en cada unos de los departamentos que tienen un presupuesto mayor a 200000 euros*/
