import os
import backend
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import UserMessage
from azure.core.credentials import AzureKeyCredential

client = ChatCompletionsClient(
    endpoint="https://models.github.ai/inference",
    credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
    api_version="2024-12-01-preview",
)

def get_ai_response(userInput: str) -> str:
    response = client.complete(
        messages=[
            {"role": "developer", "content": ""},
            UserMessage(userInput),
        ],
        model="gpt-4o-mini"
    )
    return response.choices[0].message.content