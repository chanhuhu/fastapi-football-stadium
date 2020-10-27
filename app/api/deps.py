from fastapi import Header, HTTPException, status

from app.database import SessionLocal


async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="X-Token header invalid")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
