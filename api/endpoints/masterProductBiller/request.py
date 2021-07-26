
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field

class jsonPost(BaseModel):
    biller_id: Optional[int]= None
    product_id: Optional[int]= None
    updated_at: Optional[str]= None
    created_at: Optional[str]= None
    price: Optional[int]= None
    
class jsonPut(BaseModel):
    biller_id: Optional[int]= None
    product_id: Optional[int]= None
    updated_at: Optional[str]= None
    created_at: Optional[str]= None
    price: Optional[int]= None
   
async def parameterPut(biller_id: Optional[int]= None, product_id: Optional[int]= None, updated_at: Optional[str]= None, created_at: Optional[str]= None, price: Optional[int]= None):
    return {
            "parameter" : {'biller_id' : biller_id, 'product_id' : product_id, 'updated_at' : updated_at, 'created_at' : created_at, 'price' : price}
    } 
    
async def parameterGet(biller_id: Optional[int]= None, product_id: Optional[int]= None, updated_at: Optional[str]= None, created_at: Optional[str]= None, price: Optional[int]= None, skip: int = 0, limit: int = 100):
    return {
            "parameter" : {'biller_id' : biller_id, 'product_id' : product_id, 'updated_at' : updated_at, 'created_at' : created_at, 'price' : price},
            "skip" : [skip , limit]
    }



