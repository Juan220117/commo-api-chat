"""TEST DECORATOR"""
from loguru import logger
from pydantic import BaseModel,Field
from typing import Any

#Decorator
from decorators.validate_request import validate_request
from responses.response import success_response

#Decorador con informacion requerida
class TestDecoratorRequest(BaseModel):
    numero1:int
    numero2:int = Field(default=0)

class TestDecoratorResponse(BaseModel):
    message:str

@validate_request(TestDecoratorRequest)
def main(data:dict[str,Any]):
    try:
        #import pdb; pdb.set_trace()
        logger.warning(data)
        logger.warning(data.numero1)
        
        response = TestDecoratorResponse(
            message="HOla"
        )
        return response
        
    except Exception as error:
        logger.error(f"Error in main : {error}")
        
if __name__ == '__main__':
    logger.debug(
        main(
            {
                "body": {
                    "numero1":1,
                    #"numero2":2
                }
            }
            )
        )