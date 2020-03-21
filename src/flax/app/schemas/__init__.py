from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

account_permission = Table(
    "account_permission",
    Base.metadata,
    Column("account_id", Integer, ForeignKey("account.id")),
    Column("permission_id", Integer, ForeignKey("permission.id")),
)


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    hashed_password = Column(String)

    users = relationship("User", back_populates="account")
    permissions = relationship("Permission", secondary=account_permission)


class Permission(Base):
    __tablename__ = "permission"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class User(Base):
    __tablename__ = "user"
    __table_args__ = (UniqueConstraint("account_id", "name"),)

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    account_id = Column(Integer, ForeignKey("account.id"))

    wallet = relationship("Wallet", uselist=False, back_populates="owner")
    account = relationship("Account", back_populates="users")


class Wallet(Base):
    __tablename__ = "wallet"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))

    owner = relationship("User", back_populates="wallet")
    balancies = relationship("Balance", back_populates="wallet")


class Balance(Base):
    __tablename__ = "balance"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, ForeignKey("currency.code"), index=True)
    amount = Column(Float)
    wallet_id = Column(Integer, ForeignKey("wallet.id"))

    wallet = relationship("Wallet", back_populates="balancies")


class Currency(Base):
    __tablename__ = "currency"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, index=True, unique=True)
