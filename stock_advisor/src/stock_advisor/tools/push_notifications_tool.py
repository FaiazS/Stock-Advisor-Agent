from crewai.tools import BaseTool

from typing import Type

from pydantic import BaseModel, Field

import os

import requests

class Push_Notification(BaseModel):

    """A stock recommendation message to be sent to the user."""

    stock_recommendation_message: str = Field(..., description="A stock recommendation message which is to be sent to the user")

class Push_Notification_Tool(BaseTool):

    name: str = "Push Notification Tool"

    description: str = (

        "This tool is used to send stock recommendations to the user."

    )
    args_schema: Type[BaseModel] = Push_Notification

    def _run(self, stock_recommendation_message: str) -> str:

        pushover_user = os.getenv("PUSHOVER_USERTOKEN")

        pushover_token = os.getenv("PUSHOVER_API_TOKEN")

        pushover_url = "https://api.pushover.net/1/messages.json"

        print(f"Pushing : {stock_recommendation_message}")

        push_notification_payload = {"user" : pushover_user, "token" : pushover_token, "message" : stock_recommendation_message}

        requests.post(pushover_url, payload = push_notification_payload)

        return '{"notification" : "success"}'

        
