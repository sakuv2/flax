from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt import PyJWTError
from sqlalchemy.orm import Session

from flax.app import cruds, models, schemas
from flax.app.database import get_db
from flax.app.utils import decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


def get_current_account(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
) -> schemas.Account:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_token(token)
        account_name: Optional[str] = payload.get("sub")
        if account_name is None:
            raise credentials_exception
        token_data = models.TokenData(account_name=account_name)
    except PyJWTError:
        raise credentials_exception
    account = cruds.get_account_by_name(db, account_name=token_data.account_name)
    if account is None:
        raise credentials_exception
    return account
