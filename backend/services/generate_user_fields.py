import os
import json
from openai import OpenAI
from models.User import User 
from models.Interest import Interest
from config.database import SessionLocal

client = OpenAI(api_key=os.environ["LLM_KEY"])
db = SessionLocal()

response = client.responses.create(
        model="gpt-4.1-mini",
        input=
        """
        Generate 20 random emails in the form of something@gmail.com.
        Generate 20 random usernames. 
        Generate 20 random passwords.
        Generate 20 random bios.
        Generate any number of social media interests from 1 to 5 randomly.  
        After you've finished generating all of this, return a list of JSON objects in the form of:
        \'
        [{"email": first_email, "username": first_username, "password": first_password, "bio": first_bio, "interests": [first_user_interests]}, 
        {"email": second_email, "username": second_username, "password": second_password, "bio": second_bio, "interests": [second_user_interests]}, and so on]
        '
        """
    )
list_of_users = json.loads(response.output_text)

for u_id in range(20):
    user_id = u_id + 1
    current_user = list_of_users[u_id]
    profile_picture = f"https://api.dicebear.com/7.x/avataaars/svg?seed={user_id}"

    new_user = User(
        user_id=user_id, 
        email=current_user["email"], 
        username=current_user["username"],
        password=current_user["password"], 
        profile_picture=profile_picture,
        bio=current_user["bio"]
    )
    
    db.add(new_user)

    current_interests = current_user["interests"]
    for interest in current_interests:
        new_interest = Interest(
            user_id=user_id,
            interest=interest
        )

        db.add(new_interest)

    

try:
    db.commit()
except:
    db.rollback()
finally:
    db.close() 