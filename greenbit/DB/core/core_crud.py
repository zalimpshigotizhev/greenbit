from sqlalchemy import insert, select, text, update, delete
from DB.database import async_engine, sync_engine
from DB.models import Base, UserOrm


class SyncCore:
    @staticmethod
    def create_table(drop_table: bool = True):
        if drop_table is True:
            Base.metadata.drop_all(sync_engine)
            Base.metadata.create_all(sync_engine)
        else:
            raise Exception("давай ка ты поставишь drop_table = True")


class AsyncCore:
    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def insert_user(user_data: dict):
        async with async_engine.connect() as conn:
            stmt = text(
                "INSERT INTO \"user\" (user_name, email, password) VALUES(:user_name, :email, :passw)"
            )
            stmt = stmt.bindparams(user_name=user_data['user_name'], email=user_data['email'], passw=user_data['password'])
            await conn.execute(stmt)
            await conn.commit()

    async def select_user(user_data: dict):
        async with async_engine.connect() as conn:
            stmt = text('SELECT * FROM "user" WHERE id=:user_id')
            stmt = stmt.bindparams(user_id=user_data["user_id"])
            data = await conn.execute(stmt)
            res = data.fetchall()
            return res

    async def update_user_password(user_data: dict):
        async with async_engine.connect() as conn:
            stmt = text("UPDATE \"user\" SET password=:new_data WHERE id=:user_id")
            stmt = stmt.bindparams(new_data=user_data['data'], user_id=user_data['user_id'])
            await conn.execute(stmt)
            await conn.commit()

    async def delete_user(user_data: dict):
        async with async_engine.connect() as conn:
            stmt = text('DELETE FROM "user" WHERE id=:user_id')
            stmt = stmt.bindparams(user_id=user_data["user_id"])
            await conn.execute(stmt)
            await conn.commit()
