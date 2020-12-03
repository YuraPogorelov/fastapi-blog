from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/")
def post_list(db: Session = Depends()):
    pass
