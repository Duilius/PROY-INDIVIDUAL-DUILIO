# PROY-INDIVIDUAL-DUILIO
Proyecto Infividual - FastAPI - MySQL - SQL-Alchemy 

## OBJETIVO DEL PROYECTO:

Implementar la cadena de procesamiento de datos desde la recepción¿exploración y/o reconocimineto de la información hasta la carga en Base de Datos y posterior disposición a los usuarios o clientes del producto.

### Análisis Exploratorio
Se analizó en primer lugar el contenido de cada archivo. En particular los campos o nombres de columna.
Se pudo apreciar que para resolver las preguntas o cumplir con el Proyecto No harían falta algunos campos, de manera que las columnas que tuvieran 95% de "celdas" vacías o más, serían obviadas.

![This is an image](https://python.profeduilio.com/flujo-proyecto-duilio.html)

#### -**Archivos fuente**:
Los datos están contenidos en archivos de diversos formatos (csv, txt, excel, parquet y json). 

Para la automatización del proceso es conveniente establecer como política invariable el nombrado de los archivos.

Particular atención merecen los archivos de extensión XSLS debido a que es probable que contenga datos en más de una hoja del mismo archivo.

#### -**Procesando Datos**:
Se recomienda usar pandas y/o panel para visualizar y tratar los datos, con la ayuda complementaria de python.
El uso de PyScript es aconsejable por la capacidad de visualización que permite el entorno web.

#### -**Creando Tablas**:

Luego de "limpiar" la data y tenerla lista para convertirla en tablas, lo primero que se debe hacer es identificar las relaciones que se pueden establecer para definir la estructura de las tablas considerando las claves primarias y foráneas.

Hemos usado MySQL-Workbench para crear la Base de Datos y las tablas correspondientes.

#### -**Cargando Tablas**:
Ingestar la Base de Datos es relativamente sencillo si se usa el asistente de importaciónde MySQLWorkbench.
No obstante cuando se tiene grandes volúmenes de información se aconseja hacer la carga con un solo query para un gran número de filas y no un query por cada fila a ingestar en la Base de Datos.

## SQL para probar el PipeLine:
Si bien la normalización de la BD fue realizada en etapa anterior, es recomendable una nueva "mirada" a las tablas (datos) tratando de proporcionar una mirada de comprobación y de análisis de la información.
Es decir, no dar por terminada la tarea de normalización, revisarla y modificarla de ser necesario antes de dar por terminado el proyecto.

Los QUERYS han sido creados, ejecutados y verificados en los modulos ďe Python con SQLALchemy y servidos con la API de FastAPI a HTML/HTMLX.

### DEPLOY
Haciendo uso de la librería Jinga2 se ha podido lograr darle interactividad a la página servida por FastAPI.
Adicionalmente, con ayuda del framework Semantic-UI se puede dotar a las páginas HTML de flexibilidad.

### FASTAPI
El uso de FastAPI en el proyecto se debe a la necesidad de mostrar el proyecto en "Web".
De manera que la función principal de FastAPI ha sido la de "levantar" un servidor local para el deploy del resultado de los Querys.


### SQL-Alchemy
El uso SQL-ALquemy es fundamental para la asociación entre el servidor - local - y la Base de Datos.
En nuestro caso hemos ejecutado los querys  en los módulos Python creados para el proyecto.


#### RECOMENDACIONES
La información además de su valor intrínsico debe dotarsele de una buena presentación; necesaria para aspectos como Experiencia de Usuario y darle a los mismos la posibilidad y facilidad para la exploración o navegación entre los datos, por lo cual se aconseja el uso de tecnologías como PyScript y HTMLX.
