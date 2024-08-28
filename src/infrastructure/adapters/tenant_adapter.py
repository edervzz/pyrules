"""_summary_
    """
from sqlalchemy import select
from sqlalchemy.orm import Session
from domain.entities import Tenants
from domain.ports import TenantRepository


class TenantAdapter(TenantRepository):
    """ Tenant Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def read(self, tenantid: int,  _id: int) -> Tenants:
        with Session(self.engine) as session:
            stmt = select(Tenants).where(
                Tenants.id == tenantid
            )
            rule = session.scalar(stmt)
            return rule
