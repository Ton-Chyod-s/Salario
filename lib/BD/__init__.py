
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import String, Integer, select, update, delete, ForeignKey, Column, Float
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from asyncio import run
import time

#conectar/criar banco de dados
url_do_branco = 'sqlite+aiosqlite:///salario.db'
#criando conecção asincrona com bando de dados
engine = create_async_engine(url_do_branco)

session = sessionmaker(
    engine,
    expire_on_commit = False,
    future = True,
    #se não declara a sessão é sincrona
    class_ = AsyncSession,
)

Base = declarative_base()
#tablea salario  
class Salario(Base):
    __tablename__ = 'salarioMes'
    #coluna da tabela
    id =  Column(Integer, primary_key=True)
    salarioMes = Column(Integer, nullable=False)
    mes = Column(Integer, nullable=False)
    posts = relationship('Venda', backref='cliente')

    #modo grafico de representação
    def __repr__(self):
        return f'id:{self.id},salario:{self.salarioMes},mes:{self.mes}'
    

class divSalario(Base):
    __tablename__ = 'divisaoSalario'
    #colunas da tabela
    id = Column(Integer, primary_key=True)
    despesas = Column(Integer, nullable=False)
    