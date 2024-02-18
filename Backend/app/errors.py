from fastapi import HTTPException
from models import APIError

class InvalidParamError(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail=APIError(code=400, message="Invalid parameters provided").dict())

class ResourceNotFoundError(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail=APIError(code=404, message="Specified resources(s) was not found").dict())

class UnableToCreateResourceError(HTTPException):
    def __init__(self):

        super().__init__(status_code=422, detail=APIError(code=422, message="Unable to create resource").dict())

class InternalServerError(HTTPException):
    def __init__(self):
        super().__init__(status_code=500, detail=APIError(code=500, message="Internal Server Error").dict())