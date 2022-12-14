import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, Session
from sqlalchemy.orm import sessionmaker

from api.db import get_db, Base
from api.main import app

ASYNC_DB_URL = "sqlite+aiosqlite:///:memory:"


@pytest.fixture
async def async_client() -> AsyncClient:
    # create engine and session for async 
    async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
    async_session = sessionmaker(
        autocommit=False, autoflush=False, bind=async_engine, class_=Session
    )

    # sqlite on memory tables (reset for each function)
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    # use dependency injection to set db to sqlite for test
    async def get_test_db():
        async with async_session() as session:
            yield session

    app.dependency_overrides[get_db] = get_test_db

    # yield async http client for test
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

