# PROY-INDIVIDUAL-DUILIO
Proyecto Infividual - FastAPI - MySQL - SQL-Alchemy 

## OBJETIVO DEL PROYECTO:

Implementar la cadena de procesamiento de datos desde la recepción y/o reconocimineto de la información hasta su disposición a los usuarios o clientes del producto.

### Análisis Exploratorio
Se analizó en primer lugar el contenido de cada archivo. En particular los campos o nombres de columna.
Se pudo apreciar que para resolver las preguntas o cumplir con el Proyecto No harían falta algunos campos, de manera que las columnas que tuvieran "celdas" vacías o que presenten problemas, serían obviadas.

#### -**Archivos fuente**:
Los datos están contenidos en archivos *csv y *.json. Es necesario conocer que para el caso de archivos json hay que haer uso del parámetro "lines = true" cuando se usa el método "read_json()" y el parámetro orient= dict cuando se use el método "json_normalize()".

Alternativamente y, dependiendo de la cantidad de trabajo o de las habilidades de programación, es posible acudir a PowerBI para cargar archivos JSON con estructuras anidadas, ya que son tratado y mostrados como si de una estructura simple se tratara; pudiendo descargarlo como un archivo de extensión csv.

#### -**Procesando Datos**:
Se recomienda usar pandas y/o panel para visualizar y tratar los datos, con la ayuda complementaria de python.

#### -**Creando Tablas**:

Luego de "limpiar" la data y tenerla lista para convertirla en tablas, lo primero que se debe hacer es identificar las relaciones que se pueden establecer para definir la estructura de las tablas considerando las claves primarias y foráneas.

Hemos usado MySQL-Workbench para crear la Base de Datos y las tablas correspondientes.

#### -**Cargando Tablas**:
Ingestar la Base de Datos es relativamente sencillo si se usa el asistente de importaciónde MySQLWorkbench.

## SQL para responder las Preguntas del Proyecto
Si bien la normalización de la BD fue realizada en etapa anterior, es recomendable una nueva "mirada" a las tablas (datos) tratando de resolver las preguntas del Proyecto.
Es decir, no dar por terminada la tarea de normalización, revisarla y modificarla de ser necesario antes de crear los querys.

Los QUERYS han sido creados, ejecutados y verificados en MySQL-Workbench, para luego ofrecerlos como insumo/parámetro a SQLAlchemy.

### FASTAPI
El uso de FastAPI en el proyecto se debe a la necesidad de mostrar el proyecto en "Web".
De manera que la función principal de FastAPI ha sido la de "levantar" un servidor local para el deploy del resultado de los Querys.


### SQL-Alchemy
El uso SQL-ALquemy es fundamental para la asociación entre el servidor - local - y la Base de Datos.
En nuestro caso hemos usado los mismos querys ejcutados en MySQL-Workbench para las funciones de SQL-Alchemy que FastAPI procesará y remitirá al servidor local.
