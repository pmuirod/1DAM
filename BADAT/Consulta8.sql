/*Ejercicio 1*/
/*Devuelve una lista con el nombre del producto, precio y nombre de fabricante de todos los productos de la base de datos.*/
/*SELECT producto.nombre, precio, fabricante.nombre AS nombre_fabricante
FROM producto LEFT JOIN fabricante
ON producto.id_fabricante = fabricante.id;

/*Ejercicio 2*/
/*Devuelve una lista con el nombre del producto, precio y nombre de fabricante de todos los productos de
la base de datos. Ordene el resultado por el nombre del fabricante, por orden alfabético.*/
SELECT producto.nombre, precio, fabricante.nombre AS nombre_fabricante
FROM producto LEFT JOIN fabricante
ON producto.id_fabricante = fabricante.id
ORDER BY producto.nombre;