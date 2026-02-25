from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from datetime import datetime
from config.database import Base        

class User(Base):
    __tablename__ = "users"
    
    user_id = Column(Integer, primary_key=True)
    email = Column(String)
    username = Column(String) 
    password = Column(String) 
    profile_picture = Column(String)
    bio = Column(String, default="")
    pinned_tweet_id = Column(Integer, ForeignKey("tweets.tweet_id"))
    created_at = Column(DateTime, default=datetime.now)