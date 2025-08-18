#### main.py
import os
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.profiles import InlineDefsJsonSchemaTransformer
from pydantic_ai.profiles.openai import OpenAIModelProfile
from pydantic_ai.providers.openai import OpenAIProvider

from dotenv import load_dotenv
import tools

load_dotenv()
base_url = os.getenv('base_url')
api_key = os.getenv('DEEPSEEK_API_KEY')
model = OpenAIModel(
    model_name="deepseek-chat",
    provider=OpenAIProvider(
        api_key=api_key,
        base_url=base_url
    )
)
agent = Agent(model,
              system_prompt="你是一名经验丰富的程序员，精通各种编程语言",
              tools=[
                  tools.read_file,
                  tools.list_files,
                  tools.rename_file
              ]
              )

def main():
    history = []#历史对话记录
    while True:
        user_input = input("Input: ")
        resp = agent.run_sync(user_input,
                              message_history=history)
        history = list(resp.all_messages())
        print(resp.output)


if __name__ == "__main__":
    main()