
from config.databaseConnection import mysqlConnect
from datetime import datetime
        
class RcCriteriaModules():
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
            sql = """ INSERT INTO rc_criteria (%s) VALUES(%s) """%(list_field,list_value)
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
            sql = """ SELECT updated_by, error_code, active_threshold, rc_include, interval_open, updated_at, created_at, threshold_close FROM rc_criteria """
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
            sql = """ UPDATE rc_criteria SET """
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
            
    
        