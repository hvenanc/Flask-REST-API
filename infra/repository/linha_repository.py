from sqlalchemy.orm.exc import NoResultFound
from infra.configs.connection import DBConnectionHandler
from infra.entities.linhas import Linha

class LinhaRepository:

    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Linha).all()
            return data

    def insert(self, codigo, nome, tarifa,ar_condicionado,integracao):
        with DBConnectionHandler() as db:
            data = Linha(codigo = codigo,nome = nome.upper(),tarifa = tarifa, ar_condicionado = ar_condicionado.upper(),integracao = integracao.upper())
            db.session.add(data)
            db.session.commit()
    
    def delete(self, codigo):
        with DBConnectionHandler() as db:
            db.session.query(Linha).filter(Linha.codigo == codigo).delete()
            db.session.commit()

    def update(self, codigo, nome, tarifa,ar_condicionado,integracao):
        with DBConnectionHandler() as db:
            dados = {'nome': nome.upper(), 'tarifa':tarifa, 'ar_condicionado':ar_condicionado.upper(), 'integracao':integracao.upper()}
            db.session.query(Linha).filter(Linha.codigo == codigo).update(dados)
            db.session.commit()
    
    def select_codigo(self,codigo):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Linha).filter(Linha.codigo == codigo).one()
                data = {'codigo':data.codigo,'nome':data.nome,'tarifa': float(data.tarifa),'ar_condicionado':data.ar_condicionado,'integracao':data.integracao}
                return data
            except NoResultFound:
                data = {'Status':'Linha nao encrontrada'}
                return data
    
