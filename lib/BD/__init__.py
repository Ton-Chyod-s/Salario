
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import String, Integer, select, update, delete, ForeignKey, Column, Float
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from asyncio import run

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
    posts = relationship('divSalario', backref='Salario')

    #modo grafico de representação
    def __repr__(self):
        return f'id:{self.id},salario:{self.salarioMes},mes:{self.mes}'
    

class divSalario(Base):
    __tablename__ = 'divisaoSalario'
    #colunas da tabela
    id = Column(Integer, primary_key=True)
    despesas = Column(Integer, nullable=False)
    investimento = Column(Integer, nullable=False)
    fundoEmergencial = Column(Integer, nullable=False)
    gastarAtoa = Column(Integer, nullable=False)
    autor = relationship('Salario', backref='divSalario')

    def __repr__(self):
        return f'id:{self.id},despesas:{self.despesas},investimento:{self.investimento},fundoEmergencial:{self.fundoEmergencial},gastarAtoa:{self.gastarAtoa}'
    
#função para criar banco de dados 
async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

async def salario(id,salarioMes,mes):
    async with session() as s:
        arg = Salario(id=id,salarioMes=salarioMes,mes=mes)
        s.add(arg)
        await s.commit()