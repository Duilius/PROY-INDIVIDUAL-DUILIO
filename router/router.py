from unittest import result
from fastapi import APIRouter, Response, Request         #Permite dividir las rutas de la app
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from schema.user_schema import UserSchema, DataUser
from config.db import engine                    #conn
from model.users import users
#from werkzeug.security import generate_password_hash, check_password_hash
from typing import List
#import panel as pn
from datetime import date

from fastapi.templating import Jinja2Templates

user = APIRouter()
templates = Jinja2Templates(directory="templates")


preg1 = "SELECT anio, count(raceId) as total FROM races group by anio order by total desc"
preg2 = "select r.driverId, count(r.driverId) as total, d.driverName, d.driverSurName from results as r, drivers as d where r.points=10 and r.driverId = d.driverId group by r.driverId order by 2 desc"
preg3 = "select c.circuitName, count(r.circuitId) as total  from circuitos as c, races as r where c.circuitId = r.circuitId group by c.circuitName order by 2 desc"
preg4 = "select d.driverName, d.driverSurName, sum(r.points) as total, c.constructorNat, c.constructorName from drivers as d, results as r, constructors as c where d.driverId = r.driverId and r.constructorId = c.constructorId and c.constructorNat in ('British','American') group by d.driverName, d.driverSurName, c.constructorNat, c.constructorName order by 3 desc"

@user.get("/")
def root(request:Request):
    #print(dir(request))
    #return "Hola, soy DUILIO RESTUCCIA. Para probar mi trabajo DEBES ADICIONAR a la url -en la barra de direcciones - lo siguiente ===> '/api/pregN' (donde N =[1,2,3,4]) Ejm: 'https://35c5-190-234-57-194.sa.ngrok.io/api/preg4' "
    return templates.TemplateResponse("sucursales.html", {'request':request})

#@user.get("/api/user", response_model=List[UserSchema])
@user.get("/api/preg1")
def get_users(request:Request):
    with engine.connect() as conn:
        #result = conn.execute(users.select()).fetchall()
        result = conn.execute(preg1).fetchall()
        result0 = result[0]
        result1 = result[1]
        result2 = result[2]

        return templates.TemplateResponse("index.html", {'request':request, 'races':result})

#        return f'''Año {result0[0]} , fue en el que más carreras de F1 se desarrollaron; en total {result0[1]}
#        El segundo Año fuen en el  {result1[0]} , se desarrollaron; en total {result1[1]} carreras de F1 
#        El tercer Año fuen en el  {result2[0]} , se desarrollaron; en total {result2[1]} carreras de F1
#        '''

@user.get("/api/preg2")
def get_users():
    with engine.connect() as conn:
        #result = conn.execute(users.select()).fetchall()
        result  = conn.execute(preg2).fetchall()
        result0 = result[0]
        result1 = result[1]
        result2 = result[2]

        return f'''Piloto con mayor cantidad de PRIMEROS PUESTOS {result0[2]} {result0[3]}, TOTAL PUNTOS: {result0[1]}
        2º  Piloto con mayor cantidad de PRIMEROS PUESTOS {result1[2]} {result1[3]}, TOTAL PUNTOS: {result1[1]}
        3er Piloto con mayor cantidad de PRIMEROS PUESTOS {result2[2]} {result2[3]}, TOTAL PUNTOS: {result2[1]}
        '''

@user.get("/api/preg3")
def get_users():
    with engine.connect() as conn:
        #result = conn.execute(users.select()).fetchall()
        result = conn.execute(preg3).fetchall()
        result0 = result[0]
        result1 = result[1]
        result2 = result[2]

        return f'''Circuito más corrido en F1: '{result0[0]}', TOTAL CARRERAS: {result0[1]}
        2º  Circuito más corrido en F1: '{result1[0]}', TOTAL CARRERAS: {result1[1]}
        3er Circuito más corrido en F1: '{result2[0]}', TOTAL CARRERAS: {result2[1]}
        '''

@user.get("/api/preg4")
def get_users():
    with engine.connect() as conn:
        #result = conn.execute(users.select()).fetchall()
        result = conn.execute(preg4).fetchall()
        result0 = result[0]
        result1 = result[1]
        result2 = result[2]

        return f'''El Piloto con MAYOR PUNTAJE de Escudería Americana/Británica en F1: '{result0[0]} {result0[1]}', TOTAL PUNTOS: {result0[2]} - Escudería: {result0[4]} ({result0[3]}) 
        2º  Piloto con MAYOR PUNTAJE de Escudería Americana/Británica en F1: '{result1[0]} {result1[1]}', TOTAL PUNTOS: {result1[2]} - Escudería: {result1[4]} ({result1[3]}) 
        3er Piloto con MAYOR PUNTAJE de Escudería Americana/Británica en F1: '{result2[0]} {result2[1]}', TOTAL PUNTOS: {result2[2]} - Escudería: {result2[4]} ({result2[3]}) 
        '''






















































































@user.get("/api/user/{user_id}", response_model=UserSchema)
def get_user(user_id: str):
    with engine.connect() as conn:
        result = conn.execute(users.select().where(users.c.id==user_id)).first()

        return result

@user.post("/api/user", status_code=HTTP_201_CREATED)
def create_user(data_user:UserSchema):
    with engine.connect() as conn:

        new_user = data_user.dict()
        new_user["user_passwd"]=generate_password_hash(data_user.user_passwd, "pbkdf2:sha256:30", 30)
        
        conn.execute(users.insert().values(new_user))

        return Response(status_code=HTTP_201_CREATED)


@user.post("/api/user/login", status_code=200)
def user_login(data_user: DataUser):
    with engine.connect() as conn:
        result = conn.execute(users.select().where(users.c.user_name== data_user.username)).first()

        if result != None:
            check_passwd = check_password_hash(result[3], data_user.user_passwd)

            if check_passwd:

                return {
                    "status"    :200,
                    "message"   :"Access Success !"
                }
            else:
                return {
                    "status"    :HTTP_401_UNAUTHORIZED,
                    "message"   :"Access Denied !"
                }
            
        print(result)

@user.put("/api/user/{user_id}", response_model=UserSchema)
def update_user(data_update:UserSchema, user_id:str):
    with engine.connect() as conn:
        encrypt_passwd = generate_password_hash(data_update.user_passwd, "pbkdf2:sha256:30", 30)

        conn.execute(users.update().values(name=data_update.name, user_name=data_update.user_name,
        user_passwd=encrypt_passwd).where(users.c.id== user_id))

        result = conn.execute(users.select().where(users.c.id== user_id)).first()

        return result

@user.delete("/api/user/{user_id}", status_code=HTTP_204_NO_CONTENT)
def delete_user(user_id:str):
    with engine.connect() as conn:
        conn.execute(users.delete().where(users.c.id==user_id))

        return Response(status_code=HTTP_204_NO_CONTENT)