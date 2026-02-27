from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from datetime import datetime
from config.database import Base

## Composite key of (user_id, interest)

class Interest(Base):
    __tablename__ = "interests"
    
    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    interest = Column(String, primary_key=True)
    created_at = Column(DateTime, default=datetime.now)