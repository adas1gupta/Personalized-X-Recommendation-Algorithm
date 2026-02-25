from sqlalchemy import Column, Integer, DateTime, ForeignKey
from datetime import datetime
from config.database import Base

## Composite key of (user_id, tweet_id)

class Repost(Base):
    __tablename__ = "reposts"
    
    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    tweet_id = Column(Integer, ForeignKey("tweets.tweet_id"), primary_key=True)
    created_at = Column(DateTime, default=datetime.now)
        