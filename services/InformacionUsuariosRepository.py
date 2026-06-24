from typing import Any
from repositories.InformacionUsuariosRepositor import InformacionPersonalRepository

class InformacionPersonalService(object):
    """Servicio para reglas de negocio para informacion personal usuarios"""
    
    def __init__(self,uow:Any):
        self.uow = uow
        self.informacion_repository = InformacionPersonalRepository