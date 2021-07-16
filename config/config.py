from functools import lru_cache
from dotenv import load_dotenv,find_dotenv

@lru_cache()
def get_config():
    return load_dotenv(find_dotenv(".env"), override=True)
