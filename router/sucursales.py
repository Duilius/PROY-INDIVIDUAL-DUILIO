from unittest import result
from fastapi import APIRouter, Response, Request
from pyparsing import And         #Permite dividir las rutas de la app
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from schema.user_schema import UserSchema, DataUser
from config.db2 import engine                    #conn
from model.users import users
#from werkzeug.security import generate_password_hash, check_password_hash
from typing import List
#import panel as pn
from datetime import date

from fastapi.templating import Jinja2Templates


carga = APIRouter()
templates = Jinja2Templates(directory="templates")


"""producto		IdProducto	Producto	Precio		IdTipoProducto
sucursal		IdSucursal	Sucursal	Domicilio	IdLocalidad	Latitud		Longitud
venta			IdVenta		Fecha		Fecha_Entrega	IdSucursal	IdProducto	Precio
"""


preg1 = "SELECT Sucursal, Domicilio, IdSucursal, Latitud, Longitud FROM sucursal order by Sucursal desc"
preg2 = "SELECT Producto, Precio FROM producto order by Producto desc"
#preg2 = "select r.driverId, count(r.driverId) as total, d.driverName, d.driverSurName from results as r, drivers as d where r.points=10 and r.driverId = d.driverId group by r.driverId order by 2 desc"
#preg3 = "SELECT Sucursal, Producto FROM venta WHERE order by Sucursal desc"
#preg3 = "select c.circuitName, count(r.circuitId) as total  from circuitos as c, races as r where c.circuitId = r.circuitId group by c.circuitName order by 2 desc"
preg4 = "select d.driverName, d.driverSurName, sum(r.points) as total, c.constructorNat, c.constructorName from drivers as d, results as r, constructors as c where d.driverId = r.driverId and r.constructorId = c.constructorId and c.constructorNat in ('British','American') group by d.driverName, d.driverSurName, c.constructorNat, c.constructorName order by 3 desc"

@carga.get("/")
def root(request:Request):
    #print(dir(request))
    #return "Hola, soy DUILIO RESTUCCIA. Para probar mi trabajo DEBES ADICIONAR a la url -en la barra de direcciones - lo siguiente ===> '/api/pregN' (donde N =[1,2,3,4]) Ejm: 'https://35c5-190-234-57-194.sa.ngrok.io/api/preg4' "

        return templates.TemplateResponse("sucursales.html", {'request':request})


@carga.get("/sucursales")
def root(request:Request):
    #print(dir(request))
    #return "Hola, soy DUILIO RESTUCCIA. Para probar mi trabajo DEBES ADICIONAR a la url -en la barra de direcciones - lo siguiente ===> '/api/pregN' (donde N =[1,2,3,4]) Ejm: 'https://35c5-190-234-57-194.sa.ngrok.io/api/preg4' "
    with engine.connect() as conn:
        #result = conn.execute(users.select()).fetchall()
        result = conn.execute(preg1).fetchall()

        return templates.TemplateResponse("ver_sucursales.html", {'request':request, 'losF':result})


@carga.get("/productos/{IdSucursal}")
def pide(request:Request, IdSucursal):
    with engine.connect() as conn:
        duda= "SELECT s.Sucursal, s.Domicilio, p.Producto, p.IdTipoProducto, v.Precio FROM producto p, sucursal as s, venta as v WHERE p.IdProducto = v.IdProducto AND s.IdSucursal = v.IdSucursal AND v.IdSucursal = " + IdSucursal 
        
        resultado = conn.execute(duda).fetchall()
                
        return templates.TemplateResponse("ver_ventas_sucursal.html", {'request':request, 'produs':resultado})

    