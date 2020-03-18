from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud, get_db, models, schemas
from .database import engine
from .routers import user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(user.router, prefix="/users", tags=["users"])


@app.post("/users/{user_id}/items/", response_model=schemas.Wallet)
def create_wallet_for_user(
    user_id: int, wallet: schemas.WalletCreate, db: Session = Depends(get_db)
):
    return crud.create_user_wallet(db=db, wallet=wallet, user_id=user_id)


@app.get("/wallets/", response_model=List[schemas.Wallet])
def read_wallets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    wallets = crud.get_wallets(db, skip=skip, limit=limit)
    return wallets
