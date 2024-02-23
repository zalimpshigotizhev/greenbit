from DB.database import async_session_factory, async_engine
from sqlalchemy import insert, select, text, update, delete
from DB.models import Base, UserOrm
from sqlalchemy.orm import aliased


class AsyncCoreOrm:
    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def insert_user(data: dict, table: Base):
        async with async_session_factory() as session:
            query = insert(table).values(data)
            await session.execute(query)
            await session.commit()

    async def select_user(data: dict, table: Base):
        async with async_session_factory() as session:
            query = select(table).where(table.id == data["user_id"])
            get_data = await session.execute(query)
            res = get_data.scalars().fetchall()
            return res

    async def update_user_password(data: dict, table: Base):
        async with async_session_factory() as session:
            query = (
                update(table)
                .values(password=data["data"])
                .where(table.id == data["user_id"])
            )
            await session.execute(query)
            await session.commit()

    async def delete_user(data: dict, table: Base):
        async with async_session_factory() as session:
            query = delete(table).where(table.id == data["user_id"])
            await session.execute(query)
            await session.commit()
