
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field

class jsonPost(BaseModel):
    transaction_id: Optional[int]= None
    price: Optional[int]= None
    error_code: Optional[str]= None
    biller_id: Optional[int]= None
    ts: Optional[int]= None
    id: Optional[int]= None
    updated_at: Optional[int]= None
    created_at: Optional[int]= None
    status: Optional[str]= None
    latency: Optional[int]= None
    
class jsonPut(BaseModel):
    transaction_id: Optional[int]= None
    price: Optional[int]= None
    error_code: Optional[str]= None
    biller_id: Optional[int]= None
    ts: Optional[int]= None
    id: Optional[int]= None
    updated_at: Optional[int]= None
    created_at: Optional[int]= None
    status: Optional[str]= None
    latency: Optional[int]= None
   
async def parameterPut(transaction_id: Optional[int]= None, price: Optional[int]= None, error_code: Optional[str]= None, biller_id: Optional[int]= None, ts: Optional[int]= None, id: Optional[int]= None, updated_at: Optional[int]= None, created_at: Optional[int]= None, status: Optional[str]= None, latency: Optional[int]= None):
    return {
            "parameter" : {'transaction_id' : transaction_id, 'price' : price, 'error_code' : error_code, 'biller_id' : biller_id, 'ts' : ts, 'id' : id, 'updated_at' : updated_at, 'created_at' : created_at, 'status' : status, 'latency' : latency}
    } 
    
async def parameterGet(transaction_id: Optional[int]= None, price: Optional[int]= None, error_code: Optional[str]= None, biller_id: Optional[int]= None, ts: Optional[int]= None, id: Optional[int]= None, updated_at: Optional[int]= None, created_at: Optional[int]= None, status: Optional[str]= None, latency: Optional[int]= None, skip: int = 0, limit: int = 100):
    return {
            "parameter" : {'transaction_id' : transaction_id, 'price' : price, 'error_code' : error_code, 'biller_id' : biller_id, 'ts' : ts, 'id' : id, 'updated_at' : updated_at, 'created_at' : created_at, 'status' : status, 'latency' : latency},
            "skip" : [skip , limit]
    }



