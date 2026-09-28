from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Text, DateTime, func
from datetime import datetime

from models.base import Base

if TYPE_CHECKING:
    from models.service_call import ServiceCall

class DiagnosticReport(Base):
    __tablename__ = "diagnostic_reports"
    id: Mapped[int] = mapped_column(primary_key=True)
    file_url: Mapped[str] = mapped_column(Text)
    notes: Mapped[str] = mapped_column(Text)
    timestamp: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    service_call: Mapped[ServiceCall] = relationship(back_populates="diagnostic_reports")