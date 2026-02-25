from fastapi import FastAPI
from models.Follow import Follow 
from models.Like import Like 
from models.Notification import Notification
from models.Repost import Repost 
from models.Tweet import Tweet 
from models.User import User
from config.database import Base, engine

app = FastAPI()
Base.metadata.create_all(bind=engine)

# Define a path operation (an example route)
@app.get("/")
def read_root():
    return {"Hello": "World"}
