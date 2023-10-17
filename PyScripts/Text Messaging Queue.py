from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from firebase_admin import credentials, db
from firebase_admin import initialize_app
from typing import List

# Initialize Firebase Admin SDK
cred = credentials.Certificate("firebase-admin-sdk.json")  # Replace with your Firebase Admin SDK JSON file
initialize_app(cred, {
    'databaseURL': 'https://your-database-url.firebaseio.com'
})

# Initialize FastAPI
app = FastAPI()

# Firebase Database Reference
ref = db.reference('messages')

# Data Model
class Message(BaseModel):
    text: str
    user_id: str

# Queue to hold incoming messages
message_queue = []

# Endpoint to receive and queue messages
@app.post("/add_messages")
async def add_messages(messages: List[Message]):
    for message in messages:
        message_queue.append(message)

    return {"message": "Messages added to the queue for processing"}

# Endpoint to process and store messages in Firebase
@app.post("/process_messages")
async def process_messages():
    while message_queue:
        message = message_queue.pop(0)

        # Process the message (e.g., validation, modification)
        # For demonstration, we are directly storing messages in Firebase
        message_data = {
            "text": message.text,
            "user_id": message.user_id
        }
        ref.push().set(message_data)

    return {"message": "Messages processed and stored in Firebase"}

# Endpoint to check the current message queue
@app.get("/message_queue")
async def get_message_queue():
    return message_queue
