import os
import errno 
from config.databaseConnection import mysqlConnect

def seeding():
    sql = """ 
SELECT TABLE_NAME, 
GROUP_CONCAT(COLUMN_NAME SEPARATOR ', ' ) as  COLUMN_NAME,
    GROUP_CONCAT(dt_type SEPARATOR ', ' ) as DATA_TYPE,
    GROUP_CONCAT(paramter SEPARATOR ', ' ) as PARAMETERS,
    GROUP_CONCAT(dict_param SEPARATOR ', ' ) as DICT
    from (
        SELECT c.TABLE_NAME as TABLE_NAME,
        COLUMN_NAME,
        if(DATA_TYPE in ("bigint","int","double","decimal","float"),'%d',"'%s'") dt_type,
        concat( COLUMN_NAME,": Optional[", if(DATA_TYPE in ("bigint","int","double","decimal","float"),'int','str') ,"]= None") as paramter,
        concat( "'",COLUMN_NAME,"' : ",COLUMN_NAME) as dict_param
        FROM INFORMATION_SCHEMA.COLUMNS c
        inner join information_schema.tables t on (c.TABLE_NAME = t.TABLE_NAME and t.TABLE_TYPE = 'base table')
        WHERE c.TABLE_SCHEMA = 'miliothe' and EXTRA != 'auto_increment'
        GROUP BY c.TABLE_NAME, COLUMN_NAME
        order by paramter ASC
        ) dt
    GROUP BY TABLE_NAME
    
    """
    conn = mysqlConnect()
    mycursor = conn.mydb.cursor(dictionary=True)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mycursor.close()
    return myresult
myresult = seeding()
myresult

def folderName(st):
    output = ''.join(x for x in st.title() if x.isalnum())
    return output[0].lower() + output[1:]

def className(st):
    return st.title().replace("_","")

def funcName(st):
    return st.replace(" ","_")

def urlName(st):
    return st.replace("_","-")

def name(st):
    return st.title().replace("_"," ")


dirr  = os.getcwd()
for i in myresult:
    filename = "%s/api/endpoints/%s/controller.py"%(dirr,folderName(i["TABLE_NAME"]))
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write("""
from typing import List, Optional
import re
from fastapi import APIRouter, HTTPException, Depends, Path
from starlette import status
from business.%s.service import *
from api.endpoints.%s.request import *
##from api.endpoints.%s.response import *

router = APIRouter()

@router.post("/")
async def insert_data(jsonPost: jsonPost):
    return DatabaseServices.insert(jsonPost)
    
@router.put("/")
async def update_data(jsonPut: jsonPut, parameterPut: dict = Depends(parameterPut)):
    return DatabaseServices.update(jsonPut, parameterPut)
    
@router.get("/")
async def select_data(parameterGet: dict = Depends(parameterGet)) :
    return DatabaseServices.select(parameterGet)
    
        """%(folderName(i["TABLE_NAME"]),folderName(i["TABLE_NAME"]),folderName(i["TABLE_NAME"])))
        
for i in myresult:
    filename = "%s/business/%s/service.py"%(dirr,folderName(i["TABLE_NAME"]))
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write("""
from __future__ import annotations
from typing import Any, List, Optional
from abc import abstractmethod, ABCMeta
from typing import TYPE_CHECKING

from modules.%s.module import *
from config.databaseConnection import mysqlConnect
from config.helperFunction import *

class DatabaseServices():
    def insert(jsonPost: jsonPost):
        return %sModules.insert(jsonPost.__dict__)

    def update(jsonPut: jsonPut, parameterPut: parameterPut):
        condition_set, val_condition_set = filterParameter(jsonPut.__dict__)
        condition, val_condition = filterParameter(parameterPut["parameter"])
        return %sModules.update(condition_set, condition, val_condition_set + val_condition)

    def select(parameterGet: parameterGet):
        condition, val_condition = filterParameter(parameterGet["parameter"])
        val_condition = val_condition + parameterGet["skip"]
        return %sModules.select(condition, val_condition)
    
    
        """%(folderName(i["TABLE_NAME"]),className(i["TABLE_NAME"]),className(i["TABLE_NAME"]),className(i["TABLE_NAME"])))


        
for i in myresult:
    filename = "%s/modules/%s/module.py"%(dirr,folderName(i["TABLE_NAME"]))
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write("""
from config.databaseConnection import mysqlConnect
from datetime import datetime
        
class """+(className(i["TABLE_NAME"])+"""Modules():
    def insert(dt):
        result = {
            "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
            "status" : "",
            "return" : "",
        }
        try:
            list_field = ", ".join(list(dt.keys()))
            list_value = ", ".join(['%s'] * len(dt.keys()))
            value      = list(dt.values())
            sql = """ + '''""" INSERT INTO ''' + i['TABLE_NAME'] + """ (%s) VALUES("""+ '''%s) """%(list_field,list_value)''' +"""
            conn = mysqlConnect()
            mycursor = conn.mydb.cursor(dictionary=True)
            mycursor.execute(sql,tuple(value))
            conn.mydb.commit()
            if mycursor._executed:
                result["status"] = "Success"
                result["return"] = mycursor._executed
            mycursor.close()
        except Exception as e:
            result["status"] = "Failed"
            result["return"] = e


        return result
            
            
    def select(condition, value):
        result = {
            "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
            "status" : "",
            "return" : "",
        }
        
        try:
            sql = """ + '''""" SELECT ''' +i['COLUMN_NAME'] + """ FROM """ + i['TABLE_NAME']+''' """''' +"""
            if condition != [] :
                sql += " WHERE " + ' and '.join(condition)
            sql += "LIMIT %s, %s"
            conn = mysqlConnect()
            mycursor = conn.mydb.cursor(dictionary=True)
            mycursor.execute(sql,tuple(value))
            if mycursor._executed:
                result["status"] = "Success"
                result["return"] = mycursor.fetchall()
            mycursor.close()
        except Exception as e:
            result["status"] = "Failed"
            result["return"] = e
        return result
    
    def update(set_condition, condition, value):
        result = {
            "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
            "status" : "",
            "return" : "",
        }
        
        try:
            sql = """ + '''""" UPDATE ''' +i['TABLE_NAME'] +''' SET """''' + """
            sql += ' , '.join(set_condition)
            if condition != [] :
                sql += " WHERE " + ' and '.join(condition)
            conn = mysqlConnect()
            mycursor = conn.mydb.cursor(dictionary=True)
            mycursor.execute(sql,tuple(value))
            conn.mydb.commit()
            if mycursor._executed:
                result["status"] = "Success"
                result["return"] = mycursor._executed
            mycursor.close()
        except Exception as e:
            result["status"] = "Failed"
            result["return"] = e
        return result
            
    
        """))
def jsonBody(st):
    st = st.split(", ")
    return """
    """.join(st)
    
        
for i in myresult:
    filename = "%s/api/endpoints/%s/request.py"%(dirr,folderName(i["TABLE_NAME"]))
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write("""
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field

class jsonPost(BaseModel):
    %s
    
class jsonPut(BaseModel):
    %s
   
async def parameterPut(%s):
    return {
            "parameter" : {%s}
    } 
    
async def parameterGet(%s, skip: int = 0, limit: int = 100):
    return {
            "parameter" : {%s},
            "skip" : [skip , limit]
    }



"""%(jsonBody(i["PARAMETERS"]),jsonBody(i["PARAMETERS"]),i["PARAMETERS"],i["DICT"],i["PARAMETERS"],i["DICT"]))
  
list1 = []
list2 = []

for i in myresult:
    list1.append("""from api.endpoints."""+folderName(i["TABLE_NAME"])+""".controller import router as """+folderName(i["TABLE_NAME"]))
    list2.append("""api_router.include_router("""+folderName(i["TABLE_NAME"])+""", prefix="/"""+urlName(i["TABLE_NAME"])+"""", tags=[" """+name(i["TABLE_NAME"])+""" "])""")
    
f = open("api/api.py", "w")
f.write("""
from fastapi import APIRouter
"""+'''
'''.join(list1)+"""

api_router = APIRouter()

"""+'''
'''.join(list2)+"""
""")
f.close()