from functools import wraps
from typing import Callable, Dict, List, Tuple
from enum import Enum
import openai
import os

# Define roles for a conversation
class Roles(Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"

# Represents a single message within a conversation
class ChatMessage:
    def __init__(self, role: Roles, msg: str):
        self.role = role
        self.msg = msg

    @staticmethod
    def create(role: Roles, content: str):
        return ChatMessage(role, content)
# AI interface for openai
class OpenAIAgent:
    openai.api_key = os.getenv("OPENAI_API_KEY", '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')
    gpt3 = "gpt-3.5-turbo"
    gpt4 = "gpt-4"

    def __init__(self, model=gpt3, temp=0.925, top_p=1, frequency_penalty=0, presence_penalty=0, default_max_tokens=500):
        self.model = model
        self.temp = temp
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty

    def get_response(self, conversation: List[ChatMessage], max_tokens=150) -> str:
        formatted_conversation = [{"role": m.role.value, "content": m.msg} for m in conversation]
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=formatted_conversation,
            temperature=self.temp,
            max_tokens=max_tokens,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty
        )
        return response["choices"][0]["message"]["content"]

class Prompter:
    def __init__(self, systemPrefix: str, systemSuffix: str = ""):
        self.agent = OpenAIAgent()
        self.systemPrefix = systemPrefix
        self.systemSuffix = systemSuffix
        self.conversation = []

    def generate(self, user_query: str) -> str:
        self.conversation.append(ChatMessage.create(Roles.SYSTEM, self.systemPrefix))
        self.conversation.append(ChatMessage.create(Roles.USER, user_query))
        self.conversation.append(ChatMessage.create(Roles.SYSTEM, self.systemSuffix))
        return self.agent.get_response(self.conversation)

def setup_prompt(systemPrefix: str, systemSuffix: str = ""):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            prompter = Prompter(systemPrefix, systemSuffix)
            return func(prompter, *args, **kwargs)
        return wrapper
    return decorator



@setup_prompt("You are a helpful assistant tasked with helping a developer with their code.")
def query_assistant(prompter: Prompter, user_query: str) -> str:
    return prompter.generate(user_query)

if __name__ == '__main__':
    user_query = "def get_even_numbers(numbers): return [n for n in numbers if n % 2 == 0]"
    result = query_assistant(user_query)
    print(result)
