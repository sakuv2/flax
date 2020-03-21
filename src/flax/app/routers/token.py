from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from flax.app import cruds, models, schemas
from flax.app.database import get_db
from flax.app.utils import create_access_token, verify_password

router = APIRouter()


def authenticate_account(
    db: Session, account_name: str, password: str
) -> Optional[schemas.Account]:
    account = cruds.get_account_by_name(db, account_name)
    if not account:
        return None
    if not verify_password(password, account.hashed_password):
        return None
    return account


@router.post("/token", response_model=models.Token)
def login_for_access_token(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    account = authenticate_account(db, form_data.username, form_data.password)
    if account is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": account.name})
    return {"access_token": access_token, "token_type": "bearer"}
