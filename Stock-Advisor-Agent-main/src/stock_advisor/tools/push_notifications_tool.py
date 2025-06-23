from crewai.tools import BaseTool

from typing import Type, Union

from pydantic import BaseModel, Field

import os

import requests

import json

class Push_Notification(BaseModel):

    """A stock recommendation message to be sent to the user."""

    stock_recommendation_message: Union[str, dict] = Field(..., description="A stock recommendation message which is to be sent to the user")

class Push_Notification_Tool(BaseTool):

    name: str = "Push Notification Tool"

    description: str = (

        "This tool is used to send stock recommendations to the user."

    )
    args_schema: Type[BaseModel] = Push_Notification

    def _run(self, stock_recommendation_message: str | dict) -> str:

        if isinstance(stock_recommendation_message, dict):

            stock_recommendation_message = stock_recommendation_message.get("description", "No message provided")

        pushover_user = os.getenv("PUSHOVER_USERTOKEN")

        pushover_token = os.getenv("PUSHOVER_API_TOKEN")

        pushover_url = "https://api.pushover.net/1/messages.json"

        print(f"Pushing : {stock_recommendation_message}")

        push_notification_content = {
            
            "user" : pushover_user, 
            
            "token" : pushover_token, 
            
            "message" : stock_recommendation_message
            
            }

        response = requests.post(pushover_url, data = push_notification_content)

        if response.status_code == 200:

            return json.dumps(
                
                {

                "status" : "success"

              }
            
            )
        
        else:

            return json.dumps(
                
                   {
                    
                    "error": "message not sent", 
                
                    "status_code" : response.status_code
                    
                    }
                
                )