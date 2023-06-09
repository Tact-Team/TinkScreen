import sqlalchemy as sa
import sqlalchemy.orm as so

from database.base import Base


class Result(Base):
    __tablename__ = "result"
    is_violation: so.Mapped[bool]
    violation: so.Mapped[str]
    score: so.Mapped[int]
    type_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey("violation_types.id"))
    type: so.Mapped["ViolationType"] = so.relationship("ViolationType")
    check_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey("checks.id"))
    check: so.Mapped["Check"] = so.relationship(back_populates="results")

    def __repr__(self):
        return f"<Result> {self.id} {self.is_violation} {self.violation} {self.score} {self.type_id} {self.check_id}"


class ViolationType(Base):
    __tablename__ = "violation_types"
    name: so.Mapped[str]
    blocking_score: so.Mapped[float]
    moderate_score: so.Mapped[float]
