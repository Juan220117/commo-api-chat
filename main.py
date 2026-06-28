
"""Clase de prueba"""
from loguru import logger
from typing import Any
from unit_of_work.main_uow import get_uow
from services.UsersServices import UserService

#Test
from decorators.time_decorator import medir_tiempo

@medir_tiempo
def create_user():
    with get_uow() as uow:
        #TEst request
        diccionario = {
                "first_name":"Juan Ramon",
                "paternal_surname":"Lopez",
                "maternal_surname":"Gomez",
                "cell_phone":5574744550,
            }
        
        #Get unit of work.
        user_service = UserService(uow=uow)
        resultado = user_service.create_user(
            username="Juan2201",
            password="12345",
            email="juanitocb2@gmail.com",
            personal_information = diccionario
        )
        logger.info(f"resultado : {resultado}")

@medir_tiempo
def validate_user():
    with get_uow() as uow:
        user_service = UserService(uow=uow)
        valido = user_service.login_user(
            username="Juan2201",
            password="12345"
            )
        return valido

if __name__ == '__main__':
    #create_user()
    logger.debug(validate_user())
