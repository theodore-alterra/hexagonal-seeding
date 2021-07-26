
from __future__ import annotations
from typing import Any, List, Optional
from abc import abstractmethod, ABCMeta
from typing import TYPE_CHECKING

from modules.rcCriteria.module import *
from config.databaseConnection import mysqlConnect
from config.helperFunction import *

class DatabaseServices():
    def insert(jsonPost: jsonPost):
        return RcCriteriaModules.insert(jsonPost.__dict__)

    def update(jsonPut: jsonPut, parameterPut: parameterPut):
        condition_set, val_condition_set = filterParameter(jsonPut.__dict__)
        condition, val_condition = filterParameter(parameterPut["parameter"])
        return RcCriteriaModules.update(condition_set, condition, val_condition_set + val_condition)

    def select(parameterGet: parameterGet):
        condition, val_condition = filterParameter(parameterGet["parameter"])
        val_condition = val_condition + parameterGet["skip"]
        return RcCriteriaModules.select(condition, val_condition)
    
    
        