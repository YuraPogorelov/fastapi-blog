from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import get_db
from . import service
from .shemas import PostCreate, PostList

router = APIRouter()


@router.get("/", response_model=List[PostList])
def post_list(db: Session = Depends(get_db)):
    posts = service.get_post_list(db)
    return posts


@router.post("/")
def post_list(item: PostCreate, db: Session = Depends(get_db)):
    posts = service.create_post(db, item)
    return posts
