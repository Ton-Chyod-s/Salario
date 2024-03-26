from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import String, Integer, ForeignKey, Column
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

# Conectar/criar banco de dados
url_do_banco = 'sqlite+aiosqlite:///salario.db'
# Criando conexão assíncrona com banco de dados
engine = create_async_engine(url_do_banco)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

Base = declarative_base()

# Tabela salario
class Salario(Base):
    __tablename__ = 'salarioMes'
    # Colunas da tabela
    id = Column(Integer, primary_key=True, autoincrement=True)
    salario = Column(Integer, nullable=False)
    mes = Column(Integer, nullable=False)
    # Relacionamento com divSalario
    div_salarios = relationship('DivSalario', back_populates='salario')

    # Modo gráfico de representação
    def __repr__(self):
        return f'id:{self.id},salario:{self.salario},mes:{self.mes}'

# Tabela divisaoSalario
class DivSalario(Base):
    __tablename__ = 'divisaoSalario'
    # Colunas da tabela
    id = Column(Integer, primary_key=True, autoincrement=True)
    despesas = Column(Integer, nullable=False)
    investimento = Column(Integer, nullable=False)
    fundoEmergencial = Column(Integer, nullable=False)
    gastarAtoa = Column(Integer, nullable=False)

    salario_id = Column(Integer, ForeignKey('salarioMes.id'))

    # Relacionamento com porcentagem
    porc_relacionamento = relationship('Porcentagem', back_populates='div_salario')
    # Relacionamento com Salario
    salario = relationship('Salario', back_populates='div_salarios')
    
    def __repr__(self):
        return f'id:{self.id},despesas:{self.despesas},investimento:{self.investimento},fundoEmergencial:{self.fundoEmergencial},gastarAtoa:{self.gastarAtoa}'

class Porcentagem(Base):
    __tablename__ = 'porcentagemDivisao'
    id = Column(Integer,primary_key=True, autoincrement=True)
    dict_porcentagem = Column(String(100),nullable=False)

    # Relacionamento com divSalario
    salario_id = Column(Integer, ForeignKey('divisaoSalario.id'))

    div_salario = relationship('DivSalario', back_populates='porc_relacionamento')

    def __repr__(self):
        return f'dict_porc:{self.dict_porcentagem}'

# Função para criar banco de dados
async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

# Função para inserir dados de salário e divisão de salário
async def inserir_dados(salario_mes, mes, despesas, investimento, fundo_emergencial, gastar_atoa,porcentagem):
    async with SessionLocal() as session:
        salario_obj = Salario(salario=salario_mes, mes=mes)
        session.add(salario_obj)
        div_salario_obj = DivSalario(despesas=despesas, investimento=investimento, fundoEmergencial=fundo_emergencial, gastarAtoa=gastar_atoa, salario=salario_obj)
        session.add(div_salario_obj)
        await session.flush()
        
        porc = Porcentagem(dict_porcentagem=porcentagem,salario_id=str(div_salario_obj.id))
        session.add(porc)
        await session.commit()