from datetime import datetime

from sqlalchemy.orm import Session

from app.api.v1.improvements.improvement_schemas import (
    PostImprovementRequest,
    PutImprovementRequest,
)
from app.database.models.improvement import Improvement


class ImprovementRepository:
    async def get_all_improvements(self, user_id: int, db: Session):
        return (
            db.query(Improvement)
            .filter(Improvement.user_id == user_id, Improvement.deleted_at == None)
            .all()
        )

    async def get_improvement_by_id(
        self, db: Session, user_id: int, improvement_id: int
    ):
        return (
            db.query(Improvement)
            .filter(
                Improvement.id == improvement_id,
                Improvement.user_id == user_id,
                Improvement.deleted_at == None,
            )
            .first()
        )

    async def post_improvement(
        self, db: Session, user_id: int, improvement: PostImprovementRequest
    ):
        improvement = Improvement(
            user_id=user_id,
            description=improvement.description,
            created_at=datetime.now(),
            deleted_at=None,
            last_modified=datetime.now(),
        )
        db.add(improvement)
        db.commit()
        db.refresh(improvement)
        return improvement

    async def update_improvement(
        self,
        db: Session,
        existing_improvement: Improvement,
        improvement: PutImprovementRequest,
    ):
        existing_improvement.description = (
            improvement.description if improvement.description else existing_improvement.description  # type: ignore
        )
        existing_improvement.last_modified = datetime.now()  # type: ignore

        db.commit()
        db.refresh(existing_improvement)
        return existing_improvement

    async def delete_improvement(self, db: Session, improvement: Improvement):
        improvement.deleted_at = datetime.now()  # type: ignore
        improvement.last_modified = datetime.now()  # type: ignore
        # db.delete(improvement)
        db.commit()
        return improvement
