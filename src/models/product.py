from .base import Base, Mapped, mapped_column, String


class Product(Base):
    __tablename__ = "products"
    name: Mapped[str] = mapped_column(String(30))