import openai
openai.api_key = '<openai-key>'

def ChatBot(message,lang):
    prompt = f'"{message}" Give the result within 30 words and mainly give the result only in pure {lang} language and no other languages allowed! please dont do any gramatical errors and spelling mistakes. ur name is growa AI. Ur here to help farmers'
    messages = [{"role": "user", "content": prompt}]
    chat = openai.ChatCompletion.create(
        model="gpt-4", messages=messages
    )

    reply = chat.choices[0].message.content
    return reply