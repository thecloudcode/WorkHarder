from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from firebase_admin import credentials, db
from firebase_admin import initialize_app

# Initialize Firebase Admin SDK
cred = credentials.Certificate("firebase-admin-sdk.json")  # Replace with your Firebase Admin SDK JSON file
initialize_app(cred, {
    'databaseURL': 'https://your-database-url.firebaseio.com'
})

# Initialize FastAPI
app = FastAPI()

# Firebase Database Reference
ref = db.reference('users')


# Data Model
class User(BaseModel):
    unique_id: str
    likes: int


# Increase Likes Endpoint
@app.put("/increase_likes/{unique_id}")
async def increase_likes(unique_id: str, likes_increase: int):
    user_ref = ref.child(unique_id)
    user = user_ref.get()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    current_likes = user.get('likes', 0)
    new_likes = current_likes + likes_increase

    user_ref.update({'likes': new_likes})
    return {"message": "Likes increased successfully"}


# Decrease Likes Endpoint
@app.put("/decrease_likes/{unique_id}")
async def decrease_likes(unique_id: str, likes_decrease: int):
    user_ref = ref.child(unique_id)
    user = user_ref.get()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    current_likes = user.get('likes', 0)

    if current_likes < likes_decrease:
        raise HTTPException(status_code=400, detail="Likes cannot be decreased below zero")

    new_likes = current_likes - likes_decrease

    user_ref.update({'likes': new_likes})
    return {"message": "Likes decreased successfully"}
