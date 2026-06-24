"""Timing decorator"""
import time
from functools import wraps
from loguru import logger

def medir_tiempo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()

        resultado = func(*args, **kwargs)

        fin = time.perf_counter()
        logger.debug(
            f"{func.__name__} tardó "
            f"{fin - inicio:.6f} segundos"
        )

        return resultado

    return wrapper
