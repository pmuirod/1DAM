/*Ejercicio 1*/
/*Devuelve una lista con el nombre del producto, precio y nombre de fabricante de todos los productos de
la base de datos*/
/*SELECT producto.nombre AS nombre_producto, 
precio, 
fabricante.nombre AS nombre_fabricante
FROM producto LEFT JOIN fabricante
ON producto.id_fabricante = fabricante.id;*/

/*Ejercicio 2*/
/*Devuelve una lista con el nombre del producto, precio y nombre de fabricante de todos los productos de
la base de datos. Ordene el resultado por el nombre del fabricante, por orden alfabético*/
/*SELECT producto.nombre AS nombre_producto, 
precio, 
fabricante.nombre AS nombre_fabricante
FROM producto LEFT JOIN fabricante
ON producto.id_fabricante = fabricante.id
ORDER BY nombre_fabricante;*/

/*Ejercicio 3*/
/*Devuelve una lista con el identificador del producto, nombre del producto, identificador del fabricante y
nombre del fabricante, de todos los productos de la base de datos*/
/*SELECT producto.id AS id_producto,
producto.nombre AS nombre_producto,
fabricante.id AS id_fabricante,
fabricante.nombre AS nombre_fabricante
FROM producto LEFT JOIN fabricante
ON producto.id_fabricante = fabricante.id;*/

/*Ejercicio 4*/
/*Devuelve el nombre del producto, su precio y el nombre de su fabricante, del producto más barato*/
/*SELECT producto.nombre AS nombre_producto, 
precio, 
fabricante.nombre AS nombre_fabricante
FROM producto LEFT JOIN fabricante
ON producto.id_fabricante = fabricante.id
ORDER BY precio ASC
LIMIT 1;*/

/*Ejercicio 5*/
/*Devuelve el nombre del producto, su precio y el nombre de su fabricante, del producto más caro*/
/*SELECT producto.nombre AS nombre_producto, 
precio, 
fabricante.nombre AS nombre_fabricante
FROM producto LEFT JOIN fabricante
ON producto.id_fabricante = fabricante.id
ORDER BY precio DESC
LIMIT 1;*/

/*Ejercicio 6*/
/*Devuelve una lista de todos los productos del fabricante Lenovo*/
/*SELECT 
producto.nombre,
producto.precio,
producto.id_fabricante,
fabricante.nombre AS nombre_fabricante
FROM producto LEFT JOIN fabricante
ON producto.id_fabricante = fabricante.id
WHERE fabricante.nombre = 'Lenovo';*/

/*Ejercicio 7*/
/*Devuelve una lista de todos los productos del fabricante Crucial que tengan un precio mayor que 200€*/
/*SELECT producto.nombre,
producto.precio,
producto.id_fabricante,
fabricante.nombre AS nombre_fabricante
FROM producto LEFT JOIN fabricante
ON producto.id_fabricante = fabricante.id
WHERE fabricante.nombre = 'Crucial' AND precio>200;*/

/*Ejercicio 8*/
/*Devuelve un listado con todos los productos de los fabricantes Asus, Hewlett-Packard Seagate.
Sin utilizar el operador IN*/
/*SELECT producto.nombre,
producto.precio,
producto.id_fabricante,
fabricante.nombre AS nombre_fabricante
FROM producto LEFT JOIN fabricante
ON producto.id_fabricante = fabricante.id
WHERE fabricante.nombre = 'Asus' OR fabricante.nombre = 'Hewlett-Packard' OR fabricante.nombre = 'Seagate';*/

/*Ejercicio 9*/
/*Devuelve un listado con todos los productos de los fabricantes Asus, Hewlett-Packard, Seagate.
Utilizando el operador IN*/
/*SELECT producto.id AS id_producto,
producto.nombre,
producto.precio,
producto.id_fabricante,
fabricante.nombre AS nombre_fabricante
FROM producto LEFT JOIN fabricante
ON producto.id_fabricante = fabricante.id
WHERE fabricante.nombre IN ('Asus', 'HewLett-Packard', 'Seagate');*/

/*Ejercicio 10*/
/*Devuelve un listado con el nombre y el precio de todos los productos de los fabricantes cuyo nombre
termine por la vocal e*/
/*SELECT producto.nombre,
producto.precio,
fabricante.nombre AS nombre_fabricante
FROM producto LEFT JOIN fabricante
ON producto.id_fabricante = fabricante.id
WHERE fabricante.nombre LIKE '%e';*/

/*Ejercicio 11*/
/*Devuelve un listado con el nombre y el precio de todos los productos cuyo nombre defabricante contenga
el carácter w en su nombre*/
/*SELECT producto.nombre,
producto.precio,
fabricante.nombre AS nombre_fabricante
FROM producto LEFT JOIN fabricante
ON producto.id_fabricante = fabricante.id
WHERE fabricante.nombre LIKE '%w%';*/

/*Ejercicio 12*/
/*Devuelve un listado con el nombre de producto, precio y nombre de fabricante, de todos los productos
que tengan un precio mayor o igual a 180€. Ordene el resultado en primer lugar por el precio (en orden
descendente) y en segundo lugar por el nombre (en orden ascendente)*/
/*SELECT producto.nombre,
producto.precio,
fabricante.nombre AS nombre_fabricante
FROM producto LEFT JOIN fabricante
ON producto.id_fabricante = fabricante.id
WHERE producto.precio >=180
ORDER BY producto.precio DESC,
producto.nombre ASC;*/

/*Ejercicio 13*/
/*Devuelve un listado con el identificador y el nombre de fabricante, solamente de aquellos fabricantes que
tienen productos asociados en la base de datos*/
/*SELECT fabricante.id, fabricante.nombre
FROM fabricante JOIN producto
ON fabricante.id = producto.id_fabricante;*/