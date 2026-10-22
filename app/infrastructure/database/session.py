from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.core.settings import setting


async_engine = create_async_engine(
    setting.SQLALCHEMY_DATABASE_URL
)

AsyncSessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=async_engine, expire_on_commit=False)

async def get_session_database():
    async with AsyncSessionLocal() as session:
        yield session