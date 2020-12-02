from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from core.db import Base


class Post(Base):
    __tablename__ = "blog_posts"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(String(350))
    date = Column(DateTime)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User")
