from fastapi import FastAPI, HTTPException
import requests
from pydantic import BaseModel

# Initialize FastAPI
app = FastAPI()

# Define a data model for the notification
class Notification(BaseModel):
    title: str
    body: str
    expo_token: str

# Endpoint to send a push notification
@app.post("/send_notification")
async def send_notification(notification: Notification):
    expo_token = notification.expo_token

    # Define the notification payload
    notification_data = {
        "to": expo_token,
        "title": notification.title,
        "body": notification.body,
        "sound": "default",
    }

    # Replace with your Firebase Cloud Messaging server key
    firebase_cloud_messaging_server_key = "YOUR_SERVER_KEY"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"key={firebase_cloud_messaging_server_key}",
    }

    try:
        response = requests.post(
            "https://exp.host/--/api/v2/push/send",
            headers=headers,
            json=notification_data,
        )

        if response.status_code == 200:
            return {"message": "Notification sent successfully"}
        else:
            raise HTTPException(
                status_code=response.status_code,
                detail="Failed to send notification to Expo",
            )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Failed to send notification: " + str(e),
        )
