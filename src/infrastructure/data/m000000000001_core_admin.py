""" migration file """

from datetime import datetime
from sqlalchemy import Column, Integer, BigInteger, String, Boolean, BINARY
from sqlalchemy import MetaData, Table,  CheckConstraint, Engine, select
from sqlalchemy.orm import Session
from domain.entities import Migrations
from .audit import set_auditable, set_version


def core_tables(engine: Engine) -> str:
    """000000000001_core_tables"""

    name = "000000000001_core_tables"

    metadata_obj = MetaData()

    stms = select(Migrations).where(Migrations.id == name)
    with Session(engine) as session:
        result = session.scalar(stms)
        if result is not None:
            return result.id

    # XObject Storage ----------------------------------------------
    variant = Table(
        "xobjects",
        metadata_obj,
        Column(
            "id", BigInteger, primary_key=True, autoincrement=True, comment="ID for Variants, Rules, Workflow, Actions, KVS"),
        Column(
            "object_name", String(50), nullable=False, comment="Rules / Workflows / Actions / KVS"),
        comment="Variant is a container for many Key-Values"
    )
    set_auditable(variant)

    metadata_obj.create_all(engine)

    with Session(engine) as session:
        m = Migrations()
        m.id = name
        m.exec_date = datetime.now()
        session.add(m)
        session.commit()
        return name
