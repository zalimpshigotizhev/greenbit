from DB.orm.orm_crud import AsyncCoreOrm
from DB.models import Base, UserOrm
import asyncio

data = {"user_name": "John", "email": "John@gamil.com", "password": "901jjasOO"}

data_id = {"user_id": 5}

data_up = {"columns": "password", "data": "kkllTYUQ0", "user_id": 2}


async def main():
    # await AsyncCore.create_tables()
    # await AsyncCoreOrm.insert_user(user_data=data, table=UserOrm)
    # tr = await AsyncCoreOrm.select_user(data=data_id, table=UserOrm)
    # await AsyncCore.update_user_password(user_data=data_up)
    # await AsyncCore.delete_user(user_data=data_id)


asyncio.run(main())
