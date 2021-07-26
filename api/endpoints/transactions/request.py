
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field

class jsonPost(BaseModel):
    ts: Optional[int]= None
    product_id: Optional[int]= None
    id: Optional[int]= None
    
class jsonPut(BaseModel):
    ts: Optional[int]= None
    product_id: Optional[int]= None
    id: Optional[int]= None
   
async def parameterPut(ts: Optional[int]= None, product_id: Optional[int]= None, id: Optional[int]= None):
    return {
            "parameter" : {'ts' : ts, 'product_id' : product_id, 'id' : id}
    } 
    
async def parameterGet(ts: Optional[int]= None, product_id: Optional[int]= None, id: Optional[int]= None, skip: int = 0, limit: int = 100):
    return {
            "parameter" : {'ts' : ts, 'product_id' : product_id, 'id' : id},
            "skip" : [skip , limit]
    }



