
from fastapi import APIRouter
from api.endpoints.masterProductBiller.controller import router as masterProductBiller
from api.endpoints.rcCriteria.controller import router as rcCriteria
from api.endpoints.transactions.controller import router as transactions
from api.endpoints.transactionBillers.controller import router as transactionBillers

api_router = APIRouter()

api_router.include_router(masterProductBiller, prefix="/master-product-biller", tags=[" Master Product Biller "])
api_router.include_router(rcCriteria, prefix="/rc-criteria", tags=[" Rc Criteria "])
api_router.include_router(transactions, prefix="/transactions", tags=[" Transactions "])
api_router.include_router(transactionBillers, prefix="/transaction-billers", tags=[" Transaction Billers "])
