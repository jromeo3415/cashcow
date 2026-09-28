from base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.ATM import ATM

class Branch(Base):
    __tablename__ = "branches"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    location_region: Mapped[int] = mapped_column(Integer)
    capacity: Mapped[int] = mapped_column(Integer)
    supervisor_id: Mapped[int] = mapped_column(Integer)

    ATM: Mapped[list(ATM)] = relationship(back_populates="branches")