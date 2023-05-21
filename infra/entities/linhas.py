from infra.configs.base import Base
from sqlalchemy import Column,String, Integer, DECIMAL

class Linha(Base):

    __tablename__ = 'linhas'

    codigo = Column(Integer, primary_key = True)
    nome = Column(String, nullable = False)
    tarifa = Column(DECIMAL(4,2), nullable = False)
    ar_condicionado = Column(String, nullable = False)
    integracao = Column(String, nullable = False)

    def __repr__(self):
        return f'{self.codigo}/{self.nome}' 