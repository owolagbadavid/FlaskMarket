from market import db
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, Integer, ForeignKey
from market import bcrypt, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
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

    @property
    def password(self):
        self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(
            plain_text_password).decode("utf-8")

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    @property
    def prettier_budget(self):
        return f"{self.budget:,}$"


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
