from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.core.settings import setting


async_engine = create_async_engine(
    setting.SQLALCHEMY_DATABASE_URL
)

asyncLocalSession = async_sessionmaker(autocommit=False, autoflush=False, bind=async_engine)


async def get_database_session():
    db = asyncLocalSession()
    try:
        yield db
    finally:
        await db.close()