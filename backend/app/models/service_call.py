from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.enums import ServiceCallPriority, ServiceCallStatus

if TYPE_CHECKING:
    from models.ATM import ATM
    from models.diagnostic_report import DiagnosticReport
    from models.technician import Technician

class ServiceCall(Base):
    __tablename__ = "service_calls"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    priority: Mapped[ServiceCallPriority] = mapped_column(SqlEnum(
        ServiceCallPriority,
        name="service_call_priority",
        values_callable = lambda enum_cls: [member.value for member in enum_cls]
    ))
    status: Mapped[ServiceCallStatus] = mapped_column(SqlEnum(
        ServiceCallStatus,
        name="service_call_status",
        values_callable = lambda enum_cls: [member.value for member in enum_cls]
    ))
    atm_id: Mapped[int] = mapped_column(Integer, ForeignKey("ATMs.id"))
    technician_id = Mapped[int] = mapped_column(Integer, ForeignKey("technicians.id"))

    atm: Mapped[ATM] = relationship(back_populates="service_calls")
    technician: Mapped[Technician] = relationship(back_populates="service_calls")
    diagnostic_report: Mapped[list(DiagnosticReport)] = relationship(back_populates="service_calls")