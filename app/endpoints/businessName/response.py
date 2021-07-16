from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field

class responseSpecTransactionBillers(BaseModel):
    id :str
    transaction_id :str
    error_code  :str
    status      :str
    created_at  :int
    updated_at  :int
    ts          :int
    biller_id   :int
    price       :float
    response    :str

class responseSpecTransactions(BaseModel):
    id          :str
    ts          :int
    product_id  :int
    response    :str
