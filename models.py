from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Base(DeclarativeBase):
    pass

class Url(Base):
    __tablename__ = "urls"

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    initial_url: Mapped[str] = mapped_column(String(255), nullable=False)
    shortened_url: Mapped[str] = mapped_column(String(10), nullable=False)