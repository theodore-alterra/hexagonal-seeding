
from typing import List, Optional
import re
from fastapi import APIRouter, HTTPException, Depends, Path
from starlette import status
from business.masterProductBiller.service import *
from api.endpoints.masterProductBiller.request import *
##from api.endpoints.masterProductBiller.response import *

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
    
        