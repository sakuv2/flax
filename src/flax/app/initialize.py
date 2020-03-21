from flax import env

from . import cruds, models, schemas
from .database import SessionLocal, engine


def init():
    db = SessionLocal()

    schemas.Base.metadata.create_all(bind=engine)

    # create admin user
    db_admin = cruds.get_account_by_name(db, account_name="admin")
    if db_admin is None:
        permissons = [models.PermissionCreate(name="admin")]
        admin = models.AccountCreate(
            name="admin", password=env.admin_password, permissions=permissons
        )
        cruds.create_account(db, admin)

    db.close()


if __name__ == "__main__":
    init()
