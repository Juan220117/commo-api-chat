"""Clase que contiene las unidades de trabajo"""
from contextlib import contextmanager
from config.database import SessionLocal

class SQLAlchemyUnitOfWork:
    """
    Unidad de Trabajo usando SQLAlchemy.
    Gestiona el ciclo de vida de la sesión de base de datos.
    """
    def __init__(self):
        self.session = None
    
    def __enter__(self):
        """Iniciar la sesión al entrar al contexto"""
        self.session = SessionLocal()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Cerrar la sesión al salir del contexto"""
        if self.session:
            if exc_type is not None:
                # Si hubo una excepción, hacer rollback
                self.session.rollback()
            self.session.close()
    
    def commit(self):
        """Confirmar los cambios en la base de datos"""
        if self.session:
            self.session.commit()
    
    def rollback(self):
        """Deshacer los cambios en la base de datos"""
        if self.session:
            self.session.rollback()

# Context manager para usar con 'with' - más simple
@contextmanager
def get_uow():
    """
    Context manager para obtener una unidad de trabajo.
    Uso: with get_uow() as uow:
             user = User(email="test@example.com")
             uow.session.add(user)
             uow.commit()
    """
    uow = SQLAlchemyUnitOfWork()
    with uow:
        yield uow
