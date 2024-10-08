""" _summry_ """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import TenantSpecific, Auditable, Versioned
from .base import Base


class KV(Base, TenantSpecific, Auditable, Versioned):
    """ Key-Value Item entity """

    __tablename__ = "kvs"

    id: Mapped[str] = mapped_column(
        primary_key=True, nullable=False)
