"""File with format response"""
from functools import wraps
from pydantic import BaseModel,Field
from typing import Any,Optional
import json

class ResponseModel(BaseModel):
    """Class of response"""
    status_code:Optional[int] = Field(default=200)
    body:dict[str,Any]

def api_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        status_code = 200
        body = result

        if isinstance(result, ResponseModel):
            status_code = result.status_code
            body = result.body

        if isinstance(body, BaseModel):
            body = body.model_dump_json()
        else:
            body = json.dumps(body)

        return {
            "statusCode": status_code,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": body
        }

    return wrapper