from typing import List, Optional
import re
from fastapi import APIRouter, HTTPException, Depends, Path
from starlette import status
from business.dataStream.service import *
from api.endpoints.dataStream.request import *
from api.endpoints.dataStream.response import *
from modules.default.helperFunction import *

router = APIRouter()

@router.post("/transaction_billers", response_model=responseSpecTransactionBillers)
async def get_data_transaction_billers(parameterRequest: parameterSpecTransactionBillers) -> responseSpecTransactionBillers:
    return TransactionBillers.stream_data(parameterRequest)

@router.post("/transactions", response_model=responseSpecTransactions)
async def get_data_transaction(parameterRequest: parameterSpecTransactions) -> responseSpecTransactions:
    return Transactions.stream_data(parameterRequest)

@router.get("/items")
async def get_data_transaction(rc_include: Optional[int]= None, error_code:Optional[str]= None, c: Optional[str]= None, d: Optional[int]= None) :
    params = dict(rc_include=rc_include, error_code=error_code, c=c)
    condition, val_condition = filterParameter(params)
    val_condition.append(skip,limit)
    return condition, val_condition
    

