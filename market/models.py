from market import db
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, Integer, ForeignKey


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username = mapped_column(type_=String(length=30),
                             nullable=False, unique=True
                             )
    email_address = mapped_column(type_=String(
        length=50), nullable=False, unique=True
    )
    password_hash = mapped_column(type_=String(length=60), nullable=False)
    budget = mapped_column(type_=Integer(), nullable=False, default=1000)
    items = relationship('Item', backref='owned_user', lazy=True)


class Item(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name = mapped_column(String(length=30), nullable=False, unique=True)
    price = mapped_column(Integer(), nullable=False)
    barcode = mapped_column(String(length=12), nullable=False, unique=True)
    description = mapped_column(
        String(length=1024), nullable=False, unique=True
    )
    owner: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=True)

    def __repr__(self) -> str:
        return f'Item {self.name}'
