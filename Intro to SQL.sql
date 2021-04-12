-- INTRO A SQL!!!

-- Un query es la manera de pedirle información a una base de datos. A continuación voy a listar las palabras claves básicas
-- para SQL junto con su sintaxis ya que dichas palabras obedecen un orden particular :) .



SELECT name FROM people;  -- Nos permite seleccionar datos de una tabla. En este caso, selecciono la columna name de la tabla people.

SELECT name, birthdate 
FROM people  --- Esta es la manera para seleccionar varias columnas. Separándolas con una coma!!

SELECT * 
FROM people LIMIT 10  -- La * nos permite seleccionar TODAS las columnas, mientras que la palabra clave LIMIT justamente limita la cantidad.

SELECT DISTINCT language 
FROM films  -- la palabra clave DISTINCT restinge los valores repetidos y solo devuelve uno. Si hay más de un valor listado como inglés, solo me devuelve uno.

SELECT COUNT(*) 
FROM people;  -- la palabra clave COUNT() va a contar cuántas filas, o elementos, posee una columna que le damos como argumento. En este caso, la * indica que contará TODO!!

SELECT title 
FROM films WHERE title = 'Metropolis';  -- la palabra clabe WHERE permite filtrar información y que en este caso debe ser igual a Metropolis.

SELECT title FROM films WHERE relase_year > 1994
AND release_year < 2000;  -- La palabra clave AND me permite agregar más condiciones. Siempre hay que volver a repetir el nombre de la columna!!

SELECT title 
FROM films WHERE release_year = 1994 OR 2000;  -- OR es otra palabra clave que nos permite tomar datos de una u otra columna.

SELECT title
FROM films
WHERE release_year
BETWEEN 1994 AND 2000;  -- la palabra clave BETWEEN me permite incluir un rango.

SELECT name
FROM kids
WHERE age IN (2, 4, 6, 8, 10);  -- El operador IN permite especificar más de un valor.

SELECT COUNT(*)
FROM people
WHERE birthdate IS NULL;  -- NULL es la palabra clave que nos permite filtrar cuando tenemos datos vacíos

SELECT name
FROM people
WHERE birthdate IS NOT NULL;  -- Contrario al código anterior, esto nos devuelve datos siempre y cuando no haya espacios vacíos.

SELECT name
FROM companies
WHERE name LIKE 'Data%';  -- El operador LIKE nos permite introducir un patrón cuando no estamos seguros de cómo se llamen los valores de las columnas o las filas
                          --  El % va a matchear cualquier secuencia de caracteres

SELECT name
FROM companies
WHERE name LIKE 'DataC_mp';  -- El _ , en cambio, va a matchear solo un solo caracter.

SELECT AVG(budget)  -- AVG me permite calcular el promedio de los valores de la columna seleccionada.
FROM films;

SELECT MAX(budget)  -- Me devuelve el valor máximo de la columna.
FROM films;

SELECT SUM(budget)  -- Me devuelve la suma de todos los valores de esa columna.
FROM films;

SELECT MAX(budget) AS max_budget,  -- la palabra clave AS va a generar un nombre provisorio para el resultado que arroja este código.
       MAX(duration) AS max_duration
FROM films;

SELECT title
FROM films
ORDER BY release_year DESC;  -- la palabra clave ORDER BY me permite ordenar el contenido de la columna en orden creciente. Pero si agregamos DESC al final ese orden cambia por el decreciente.

SELECT sex, count(*)  -- GROUP BY nos permite agrupar datos de una columna. Se puede combinar con operaciones como COUNT, MAX o MIN.
FROM employees
GROUP BY sex;

SELECT release_year
FROM films
GROUP BY release_year
WHERE COUNT(title) > 10;  -- Esto arroja error porque no podemos incluir operaciones de cálculo dentro del dominio de WHERE.

SELECT release_year
FROM films
GROUP BY release_year
HAVING COUNT(title) > 10;  -- Para solventar los problemas del código de más arriba, tenemos HAVING!!  


SELECT country, avg(budget) AS avg_budget, avg(gross) AS avg_gross 
FROM films GROUP BY country HAVING count(country) > 10 
ORDER BY country LIMIT 5  -- Ejemplo de un query extenso donde las palabras claves obedecen un orden determinado.