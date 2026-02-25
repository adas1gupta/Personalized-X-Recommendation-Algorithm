from sqlalchemy import Column, Integer, DateTime, ForeignKey
from datetime import datetime
from config.database import Base

## Composite key of (follower_id, following_id)

class Follow(Base):
    __tablename__ = "follows"
    
    follower_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    following_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    created_at = Column(DateTime, default=datetime.now)