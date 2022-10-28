import os
from os.path import isfile, join
import re
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

ruta    =   r'C:\pyscript\venvM3\data2'
Xfiles   =   os.listdir(ruta)

solo_files =    [nombre for nombre in Xfiles if isfile(join(ruta, nombre)) ]

dictFiles =list()        
filePrecios=list()
listaDataF = list()
#Identifica formato de archivo: 1) precios*.*

for Fi in solo_files :
    if re.search("precios_semana", Fi) and not re.search("COPIA", Fi):
        filePrecios.append(Fi)

for F in filePrecios:
        tipoF ='csv,txt,xlsx,json,parquet'
        #Identifica y compara extensión de c/archivo
        
        extension = str(F).split(".")[1]         #Extensión/Tipo de archivo
        
        if (extension == "xlsx" ) :
            
            #Obtener Nombres de cada HOJA del archivo XLSX
            fecha1 = str(F).split(".")[0].split("_")[2]
            fecha2 = str(F).split(".")[0].split("_")[3]

            hoja1 = "precios_" + fecha1 + "_" + fecha1
            hoja2 = "precios_" + fecha2 + "_" + fecha2
            
            df_hoja1 = pd.read_excel(ruta +"\\"+ F, sheet_name= hoja1)
            df_hoja2 = pd.read_excel(ruta +"\\"+ F, sheet_name= hoja2)

            #Llenar Diccionario {'Nombre-Archivo':'Fecha-precios'}
            dictFiles.append({'nameDF': df_hoja1, 'fechaF':fecha1})
            dictFiles.append({'nameDF': df_hoja2, 'fechaF':fecha2})

            listaDataF.append(hoja1)
            listaDataF.append(hoja2)
            continue
        else:
            
            #Obtiene fecha del nombre del archivo {f}
            fechaF= str(F).split(".")[0].split("_")[2]
        
            #Llenar Diccionario {'Nombre-Archivo':'Fecha-precios'}
            dictFiles.append({'nameF': F, 'fechaF':fechaF})

"""            if extension=="csv" :
                #Crea DataFrame según {tipo} y {fechaF}
                nom_df = "df_csv_" + fechaF
                nom_df = pd.read_csv(ruta +"\\"+ F)
                listaDataF.append(nom_df)"""
"""
            if extension=="txt" :
                #Crea DataFrame según {tipo} y {fechaF}
                nom_df = "df_txt_" + fechaF
                nom_df = pd.read_csv(ruta +"\\"+ F, sep="|")
                listaDataF.append(nom_df)"""
"""
            if extension=="json" :
                #Crea DataFrame según {tipo} y {fechaF}
                nom_df = "df_json_" + fechaF
                nom_df = pd.read_json(ruta +"\\"+ F)
                listaDataF.append(nom_df)
"""
"""if extension=="parquet" :
                #Crea DataFrame según {tipo} y {fechaF}
                nom_df = "df_parquet_" + fechaF
                nom_df = pd.read_parquet(ruta +"\\"+ F)
                listaDataF.append(nom_df)               """