import os
from dotenv import load_dotenv
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage, AssistantMessage
from azure.core.credentials import AzureKeyCredential

load_dotenv()

client = ChatCompletionsClient(
    endpoint="https://models.github.ai/inference",
    credential=AzureKeyCredential(os.environ["ApiKey"]),
    api_version="2024-12-01-preview",
)

messages=[
    SystemMessage("You are a helpful assistant that is called Skrotnissen."),
    SystemMessage("You answer in a friendly and concise manner.")
]

def get_ai_response(userInput: str) -> str:
    global messages

    messages.append(UserMessage(userInput))

    response = client.complete(
        messages=messages,
        model="gpt-4o-mini"
    )

    ai_response = response.choices[0].message.content

    messages.append(AssistantMessage(ai_response))

    return ai_response