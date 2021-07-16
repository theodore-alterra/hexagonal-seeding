from config.databaseConnection import mysqlConnect
def seeding():
    sql = """ 
    SELECT TABLE_NAME, GROUP_CONCAT(COLUMN_NAME SEPARATOR ', ' ) as  COLUMN_NAME,
    GROUP_CONCAT(dt_type SEPARATOR ', ' ) as DATA_TYPE,GROUP_CONCAT(value SEPARATOR ', ' ) as VALUE from (
        SELECT c.TABLE_NAME as TABLE_NAME,COLUMN_NAME,concat("dt.",COLUMN_NAME) as value,
        if(DATA_TYPE in ("bigint","int","double","decimal","float"),'%d',"'%s'") dt_type
        FROM INFORMATION_SCHEMA.COLUMNS c
        inner join information_schema.tables t on (c.TABLE_NAME = t.TABLE_NAME and t.TABLE_TYPE = 'base table')
        WHERE c.TABLE_SCHEMA = 'miliothe' and EXTRA != 'auto_increment'
        GROUP BY c.TABLE_NAME, COLUMN_NAME
        order by ORDINAL_POSITION asc
        ) dt
    GROUP BY TABLE_NAME"""
    conn = mysqlConnect()
    mycursor = conn.mydb.cursor(dictionary=True)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mycursor.close()
    return myresult
myresult = seeding()

f = open("modules/module/default.py", "w")
f.write("""
from typing import Optional, List
from databaseConnection import mysqlConnect
from datetime import datetime

""")

for i in myresult:
    f.write("""class """+i['TABLE_NAME'].title().replace("_", "")+"""Modules():
    def insert(dt):
        result = {
            "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
            "status" : "",
            "return" : "",
        }
        try:
            sql = """ + '''""" INSERT INTO ''' + i['TABLE_NAME'] + """ (""" +i['COLUMN_NAME'] + """) VALUES("""+ i['DATA_TYPE']+ ''') """%('''+ i['VALUE'] +""")
            conn = mysqlConnect()
            mycursor = conn.mydb.cursor(dictionary=True)
            mycursor.execute(sql)
            conn.mydb.commit()
            if mycursor._executed:
                result["status"] = "Success"
                result["return"] = mycursor._executed
        except Exception as e:
            result["status"] = "Failed"
            result["return"] = e

        mycursor.close()
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
            
""")

f.close()

