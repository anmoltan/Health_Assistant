from textbase import bot, Message
from textbase.models import OpenAI
from typing import List

# Load your OpenAI API key
OpenAI.api_key = "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"

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """"Welcome to your Personal Health and Fitness Coach! Let's kickstart your journey to a healthier you. To get started, please share some key details: 
1. Your age and gender.
2. Current weight and height.
3. Your fitness goals (e.g., lose weight, gain muscle, maintain).
4. Any dietary restrictions or preferences.
5. How many days a week you can commit to workouts.
6. Any existing medical conditions or injuries (if applicable).
Let's work together to create a tailored plan just for you!"

Provide the output in a well structured points.
"""

@bot()
def on_message(message_history: List[Message], state: dict = None):

    # Generate GPT-3.5 Turbo response
    bot_response = OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history, # Assuming history is the list of user messages
        model="gpt-3.5-turbo",
    )

    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }