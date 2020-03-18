from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from flax.app.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    wallet = relationship("Wallet", uselist=False, back_populates="owner")


class Wallet(Base):
    __tablename__ = "wallet"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))

    owner = relationship("User", back_populates="wallet")
    balancies = relationship("Balance", back_populates="wallet")


class Balance(Base):
    __tablename__ = "balance"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, index=True)
    amount = Column(Float)
    wallet_id = Column(Integer, ForeignKey("wallet.id"))

    wallet = relationship("Wallet", back_populates="balancies")
