from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from typing import TYPE_CHECKING

from models.base import Base

if TYPE_CHECKING:
    from models.service_call import ServiceCall

class Technician(Base):
    __tablename__ = "technicians"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    location_region: Mapped[int] = mapped_column(Integer)

    service_calls: Mapped[list(ServiceCall)] = relationship(back_populates="technicians")
    