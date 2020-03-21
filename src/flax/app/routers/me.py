from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from flax.app import cruds, models, schemas
from flax.app.database import get_db

from . import get_current_account

router = APIRouter()


@router.get("/me", response_model=models.Account)
def read_me(current_account: schemas.Account = Depends(get_current_account)):
    return current_account


@router.post("/me/users", response_model=models.User)
def create_me_user(
    user: models.UserCreate,
    db: Session = Depends(get_db),
    current_account: schemas.Account = Depends(get_current_account),
):
    me = models.Account.from_orm(current_account)
    if user.name in [u.name for u in me.users]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"name='{user.name}' already exists.",
        )
    return cruds.create_user(db=db, db_account=current_account, user=user)


@router.get("/me/users", response_model=List[models.User])
def read_me_users(current_account: schemas.Account = Depends(get_current_account)):
    return current_account.users


@router.get("/me/wallets", response_model=List[models.Wallet])
def read_me_wallets(current_account: schemas.Account = Depends(get_current_account)):
    return ...
