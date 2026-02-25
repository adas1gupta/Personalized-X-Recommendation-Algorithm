from sqlalchemy import Column, Integer, DateTime, Boolean, Enum, ForeignKey
from datetime import datetime
from config.database import Base
import enum

# notification type
class NotificationType(enum.Enum):
    LIKE = "like"
    FOLLOW = "follow"
    REPOST = "repost"
    REPLY = "reply"

class Notification(Base):
    __tablename__ = "notifications"
    
    notification_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    actor_id = Column(Integer, ForeignKey("users.user_id")) # who triggered the notification
    notification_type = Column(Enum(NotificationType, name="notification_type"))
    tweet_id = Column(Integer, ForeignKey("tweets.tweet_id"))
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)