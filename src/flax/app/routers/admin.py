from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from flax.app import cruds, models, schemas
from flax.app.database import get_db

from . import get_current_account

router = APIRouter()


def admin(
    db: Session = Depends(get_db),
    current_account: schemas.Account = Depends(get_current_account),
) -> Session:
    credentials_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN, detail="You need administrator account."
    )
    admin = models.Account.from_orm(current_account)
    perms = [p.name for p in admin.permissions]
    if "admin" not in perms:
        raise credentials_exception
    return db


@router.get("/accounts", response_model=List[models.Account])
def read_accounts(skip: int = 0, limit: int = 100, db: Session = Depends(admin)):
    return cruds.get_accounts(db, skip=skip, limit=limit)


@router.get("/users", response_model=List[models.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(admin)):
    return cruds.get_users(db, skip=skip, limit=limit)


@router.get("/wallets", response_model=List[models.Wallet])
def read_wallets(skip: int = 0, limit: int = 100, db: Session = Depends(admin)):
    return cruds.get_wallets(db, skip=skip, limit=limit)
