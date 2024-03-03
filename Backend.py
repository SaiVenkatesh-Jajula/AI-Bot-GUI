from openai import OpenAI


class Chatbot:
    def __init__(self):
        self.client = OpenAI(api_key='ENTER YOUR OPENAI API_KEY')

    def get_result(self, question):
        result = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": question}]
        ).choices[0].message.content
        return result


if __name__ == "__main__":
    cb = Chatbot()
    print(cb.get_result("Who are indians 2 words?"))

# !/usr/bin/env -S poetry run python
#
# from openai import OpenAI
#
# # gets API Key from environment variable OPENAI_API_KEY
# client = OpenAI(api_key='Enter your open ai api key')
#
# # Streaming:
# stream = client.chat.completions.create(
#     model="gpt-4",
#     messages=[
#         {
#             "role": "user",
#             "content": "what is germany in 2 words?",
#         },
#     ],
#     stream=True,
# )
# for chunk in stream:
#     if not chunk.choices:
#         continue
#
#     print(chunk.choices[0].delta.content, end="")
# print()
