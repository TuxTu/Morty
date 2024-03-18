import curses
import anthropic
from llama_cpp import Llama

class Morty:
    def __init__(self, model_path_or_api, params, model_name):
        # Instanciate the model
        self.messages = []
        self.requirement = "You are a good listener. If you think I didn't finish my words, just output exactly \"**skip**\" to skip an immediate reply(four stars, four characters, no any other reply). In most case in this conversation, you need skip the reply."
        if model_name == "llama":
            self.model_name = "llama"
            self.model = Llama(model_path=model_path_or_api, chat_format="llama-2", n_ctx=2048)
            self.messages.append({"role": "system", "content": self.requirement})
            self.params = params
        elif model_name == "claude":
            self.model_name = "claude"
            with open(model_path_or_api, 'r', encoding='utf-8') as file:
                api = file.read()
            self.model = anthropic.Anthropic(
                api_key=api,
            )

    def skip(self, text):
        return "**skip**" in text.lower()

    def listen(self):
        while True:
            print("\n\nYou>")
            prompt = input()
            if prompt == 'Q':
                break
            self.messages.append({"role": "user", "content": prompt})

            if self.model_name == "llama":
                response = self.model.create_chat_completion(messages = self.messages, **self.params)['choices'][0]['message']['content']
            if self.model_name == "claude":
                response = self.model.messages.create(
                    # model="claude-3-opus-20240229",
                    model="claude-2.1",
                    system=self.requirement,
                    max_tokens=2048,
                    messages=self.messages
                ).content[0].text

            self.messages.append({"role": "assistant", "content": response})

            if(self.skip(response)):
                continue
            print("\n\nMorty>")
            print(response)
