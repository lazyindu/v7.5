import openai
import os
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token = "5942641741:AAFyOtC2NguQFnolhE8eFQF1D2TzOabwevo")
dp = Dispatcher(bot)
openai.api_key = "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"

@dp.message_handler(commands = ['/lazyai'])
async def welcome(message: types.Message):
    await message.reply("Hello am chat Gpt feature of lazyprincess")

@dp.message_handler()
async def gpt(message: types.message):
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = message.text,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0.1,
        presence_penalty=0.0,
    )
    await message.reply(response.choices[0].text)

if __name__ == "__main__":
    executor.start_polling(dp)
    


