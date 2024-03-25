
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