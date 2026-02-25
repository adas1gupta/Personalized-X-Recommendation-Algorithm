from sqlalchemy import Column, Integer, DateTime
from datetime import datetime
from config.database import Base

## Composite Key of (user_id, tweet_id)

class Like(Base):
    __tablename__ = "likes"

    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    tweet_id = tweet_id = Column(Integer, ForeignKey("tweets.tweet_id"), primary_key=True)
    created_at = Column(DateTime, default=datetime.now)
        