from sqlalchemy.orm import Session

from flax.app import models, schemas

from typing import List


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    # 財布を作る
    db_wallet = models.Wallet(owner_id=db_user.id)
    db.add(db_wallet)
    db.commit()
    return db_user


def get_wallet(db: Session, user_id: int):
    return db.query(models.Wallet).filter(models.User.id == user_id).first()


def get_wallets(db: Session, skip: int = 0, limit: int = 100) -> List[models.Wallet]:
    return db.query(models.Wallet).offset(skip).limit(limit).all()


def create_user_wallet(db: Session, wallet: schemas.WalletCreate, user_id: int):
    db_item = models.Wallet(**wallet.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
