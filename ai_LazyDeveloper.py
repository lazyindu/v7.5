import openai
from telegram.ext import Updater, MessageHandler, Filters
from info import *
openai.api_key = "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"

def generate_response(message):
    prompt = f"User: {message}\nBot:"
    response = openai.Completion.create(
        engine="text-davinci-004",
        prompt=prompt,
        temperature=0.7,
        max_tokens=60,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

def handle_message(update, context):
    message = update.message.text
    response = generate_response(message)
    update.message.reply_text(response)

updater = Updater(f"{BOT_TOKEN}", use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
updater.start_polling()
