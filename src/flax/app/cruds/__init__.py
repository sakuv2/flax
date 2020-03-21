from typing import List

from sqlalchemy.orm import Session

from flax.app import models, schemas
from flax.app.utils import get_password_hash


def create_account(db: Session, account: models.AccountCreate):
    hashed_password = get_password_hash(account.password)
    db_account = schemas.Account(name=account.name, hashed_password=hashed_password)
    for p in account.permissions:
        db_permission = schemas.Permission(name=p.name)
        db_account.permissions.append(db_permission)  # type: ignore
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account


def get_account_by_name(db: Session, account_name: str) -> schemas.Account:
    return (
        db.query(schemas.Account).filter(schemas.Account.name == account_name).first()
    )


def get_accounts(db: Session, skip: int = 0, limit: int = 100) -> List[schemas.Account]:
    return db.query(schemas.Account).offset(skip).limit(limit).all()


def create_order(db: Session, user_id: int):
    ...


def read_order(db: Session, order_id: int):
    ...


def delete_order(db: Session, order_id: int):
    ...


def create_pair(db: Session, base: models.Code, settlement: models.Code):
    """通貨ペアの登録
    base通貨をsettlement通貨で売買する
    """


def delete_pair(db: Session, pari_id: int):
    ...


def create_exchange(db: Session, exchange_id: int):
    ...


def create_currency(db: Session, currency_code: models.Code):
    ...


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(
    db: Session, db_account: schemas.Account, user: models.UserCreate
) -> schemas.User:
    db_user = schemas.User(name=user.name)
    db_user.wallet = schemas.Wallet()
    db_account.users.append(db_user)  # type: ignore
    db.commit()
    db.refresh(db_user)
    return db_user


def get_wallet(db: Session, user_id: int) -> schemas.Wallet:
    return db.query(schemas.Wallet).filter(schemas.User.id == user_id).first()


def get_wallets(db: Session, skip: int = 0, limit: int = 100) -> List[schemas.Wallet]:
    return db.query(schemas.Wallet).offset(skip).limit(limit).all()


def create_user_wallet(db: Session, wallet: models.WalletCreate, user_id: int):
    db_item = schemas.Wallet(**wallet.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
