from sqlalchemy import Column, Integer, DateTime
from datetime import datetime
from config.database import Base

## Composite key of (follower_id, following_id)

class Follow(Base):
    __tablename__ = "follows"
    
    follower_id = Column(Integer, primary_key=True)
    following_id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.now)