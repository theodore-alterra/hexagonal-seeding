
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field

class jsonPost(BaseModel):
    updated_by: Optional[int]= None
    error_code: Optional[str]= None
    active_threshold: Optional[str]= None
    rc_include: Optional[str]= None
    interval_open: Optional[int]= None
    updated_at: Optional[str]= None
    created_at: Optional[str]= None
    threshold_close: Optional[int]= None
    
class jsonPut(BaseModel):
    updated_by: Optional[int]= None
    error_code: Optional[str]= None
    active_threshold: Optional[str]= None
    rc_include: Optional[str]= None
    interval_open: Optional[int]= None
    updated_at: Optional[str]= None
    created_at: Optional[str]= None
    threshold_close: Optional[int]= None
   
async def parameterPut(updated_by: Optional[int]= None, error_code: Optional[str]= None, active_threshold: Optional[str]= None, rc_include: Optional[str]= None, interval_open: Optional[int]= None, updated_at: Optional[str]= None, created_at: Optional[str]= None, threshold_close: Optional[int]= None):
    return {
            "parameter" : {'updated_by' : updated_by, 'error_code' : error_code, 'active_threshold' : active_threshold, 'rc_include' : rc_include, 'interval_open' : interval_open, 'updated_at' : updated_at, 'created_at' : created_at, 'threshold_close' : threshold_close}
    } 
    
async def parameterGet(updated_by: Optional[int]= None, error_code: Optional[str]= None, active_threshold: Optional[str]= None, rc_include: Optional[str]= None, interval_open: Optional[int]= None, updated_at: Optional[str]= None, created_at: Optional[str]= None, threshold_close: Optional[int]= None, skip: int = 0, limit: int = 100):
    return {
            "parameter" : {'updated_by' : updated_by, 'error_code' : error_code, 'active_threshold' : active_threshold, 'rc_include' : rc_include, 'interval_open' : interval_open, 'updated_at' : updated_at, 'created_at' : created_at, 'threshold_close' : threshold_close},
            "skip" : [skip , limit]
    }



