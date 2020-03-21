from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from flax.app import cruds, models
from flax.app.database import get_db

router = APIRouter()


@router.post("/accounts", response_model=models.Account)
def create_account(account: models.AccountCreate, db: Session = Depends(get_db)):
    return cruds.create_account(db=db, account=account)


@router.get("/ping")
def ping():
    return {"status": "ok"}
