# SQLI-scripts

## SQLITE
- Se usa para listar las tablas de la base datos
- Se usa para listar las columnas de las tablas
  - `SqliteIColumns.py`
    -   Se usa un case, donde se lee carácter por carácter los nombres de las columnas, se itera por posición y carácter, en este caso particular cuando es verdadera la condición se hace una instrucción que simula un sleep() pero en este caso esa instrucción genera un http 500, lo que se usa para inferir en los caracteres 
