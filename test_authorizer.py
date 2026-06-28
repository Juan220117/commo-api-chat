from utils.authorizer import AuthorizerModel
from loguru import logger

def main():
    autorizador = AuthorizerModel()
    token = autorizador.generate_token(
        service_name="Login",
        username="Juanv220117"
    )
    logger.warning(token)
    response = autorizador.validate_token(bearer_token=token,method_arn="as")
    logger.warning(response)

if __name__ == '__main__':
    main()