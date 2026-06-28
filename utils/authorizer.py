"""Archivo para authorizador de Apikey"""
import jwt
import os
import json
import boto3
from datetime import datetime,timedelta
from loguru import logger
from typing import Any

class AuthorizerModel(object):
    """Class to validate and create token"""
    def __init__(self) -> None:
        self.secret_name = os.environ.get('SECRET_NAME')
        self.region_name = os.environ.get('REGION_AWS', 'us-east-2')

    def get_secret_key(self) -> str:
        """# Function to retrieve the key used to generate authentication tokens."""
        try:
            #1.- Creat conexion with secrets manager.
            session = boto3.session.Session()
            client = session.client(
                service_name='secretsmanager',
                region_name=self.region_name
                )
            try:
                #2.- we get the secret to generating the token.
                response = client.get_secret_value(
                    SecretId=self.secret_name
                )
                secret_data = json.loads(response['SecretString'])
                clave_firma = secret_data["api_key"]
                return clave_firma
            except Exception as error:
                logger.error(f"Error obteniendo el secreto: {error}")

        except Exception as error:
            logger.error(
                f"* Ocurrio un error en obtener_clave : {error}"
                )

    def generate_token(self,service_name:str,username:str) -> dict[str,Any]:
        """# Function to retrieve the key used to generate authentication tokens."""
        try:
            #clave_firma = self.get_secret_key()
            clave_firma = "ABCDEFGHIJKLMNA01ASDASDASDABCDEFGHIJKLMNA01ASDASDASD"

            #3.- Generar token.
            payload = {
                "iss":service_name,
                "sub":username,
                "iat":datetime.now(),
                "exp":datetime.now() + timedelta(days=1),
                "scope": "read:data"
            }
            token = jwt.encode(payload,clave_firma,algorithm="HS256")
            return token
        except Exception as e:
            logger.error(f"Error obteniendo el secreto: {e}")
            return {
                'statusCode': 500,
                'headers': {'Content-Type': 'application/json',},
                'body': json.dumps({"Error":str(e)}),
            }

    def validate_token(self,bearer_token:str,method_arn:str) -> dict[str,Any]:
        """Funcion para validar el token
        beare_token -> Token enviado # "Bearer <token>"
        """
        if not bearer_token:
            return self.response_401("Falta el header de Autorización")

        token_solo = bearer_token.split(" ")[1] if " " in bearer_token else bearer_token
        #clave = self.get_secret_key()
        clave = "ABCDEFGHIJKLMNA01ASDASDASDABCDEFGHIJKLMNA01ASDASDASD"
        try:
            respuesta = self.response_401("Token no valido - credenciales erroneas")
            # Esto valida firma y fecha de expiración automáticamente
            payload = jwt.decode(token_solo,clave, algorithms=["HS256"])

            if payload.get("iss") == "Login":
                logger.debug("Token valido - Se puede invocar la lambda")
                respuesta = self.generate_policy('user', 'Allow', method_arn)

            return respuesta
        except jwt.ExpiredSignatureError:
            print("Token expirado")
            return self.generate_policy('user', 'Deny', method_arn)

    @staticmethod
    def generate_policy(principal_id:str, effect:str, resource:str) -> dict[str,Any]:
        """Funcion para generar politica"""
        return {
            'principalId': principal_id,
            'policyDocument': {
                'Version': '2012-10-17',
                'Statement': [{
                    'Action': 'execute-api:Invoke',
                    'Effect': effect,
                    'Resource': resource
                }]
            }
        }

    @staticmethod
    def response_401(mensaje:str) -> dict[str,Any]:
        """Funcion para regresar error 401"""
        return {
            'statusCode': 401,
            'body': json.dumps({"error": mensaje})
        }