from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from datetime import datetime
from config.database import Base        

class Tweet(Base):
    __tablename__ = "tweets"

    tweet_id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("users.user_id"))
    text = Column(String)
    media_url = Column(String)
    parent_tweet_id = Column(Integer, ForeignKey("tweets.tweet_id"))
    created_at = Column(DateTime, default=datetime.now)
        