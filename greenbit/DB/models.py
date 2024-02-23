from sqlalchemy.orm import Mapped, mapped_column
from DB.database import Base, str_256
import datetime
from typing import Annotated
from sqlalchemy import text


intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[
    datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))
]
updated_at = Annotated[
    datetime.datetime,
    mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.utcnow,
    ),
]


class UserOrm(Base):
    __tablename__ = "user"

    id: Mapped[intpk]
    user_name: Mapped[str_256] = mapped_column(nullable=False)
    email: Mapped[str_256] = mapped_column(nullable=False)
    password: Mapped[str_256] = mapped_column(nullable=False)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
