
from datetime import datetime, timedelta

import jwt
from passlib.context import CryptContext
from flax import env


# to get a string like this run:
# openssl rand -hex 32
# jwtのシークレット
SECRET_KEY = env.jwt_secret_key
# jwtの署名アルゴリズム
ALGORITHM = env.jwt_algorithm
# トークンの有効期限
ACCESS_TOKEN_EXPIRE_MINUTES = env.access_token_expire_minutes


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(*, data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_token(token: str) -> dict:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload
