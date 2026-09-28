from typing import TYPE_CHECKING
from base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, Numeric, String
from sqlalchemy import Enum as SqlEnum
from decimal import Decimal

from enums import ATMStatus

if TYPE_CHECKING:
    from models.branch import Branch
    from models.service_call import ServiceCall

class ATM(Base):
    __tablename__ = "ATMs"

    id: Mapped[int] = mapped_column(primary_key=True)
    serial_number: Mapped[str] = mapped_column(String(150), unique=True)
    model: Mapped[str] = mapped_column(String(150))
    status: Mapped[ATMStatus] = mapped_column(SqlEnum(
        ATMStatus,
        name="atm_status",
        values_callable = lambda enum_cls: [member.value for member in enum_cls]
    ))
    cash_level: Mapped[Decimal] = mapped_column(Numeric(5, 2))
    branch_id: Mapped[int] = mapped_column(Integer, ForeignKey("branches.id"))

    branch: Mapped[Branch] = relationship(back_populates="ATMs")
    service_call: Mapped[list(ServiceCall)] = relationship(back_populates="ATMs")