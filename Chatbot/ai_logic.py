import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import UserMessage
from azure.core.credentials import AzureKeyCredential

client = ChatCompletionsClient(
    endpoint="https://models.github.ai/inference",
    credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
    api_version="2024-12-01-preview",
)

userChat = input("Enter your message to the AI: ")
print("Ai is responding...")

response = client.complete(
    messages=[
        {"role": "developer", "content": ""},
        UserMessage(userChat),
    ],
    model="gpt-4o-mini"
)

print(response.choices[0].message.content)