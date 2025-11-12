import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from openai import OpenAI


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")


bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Привет! Я ДурачокБот \nЗадай вопрос!")

@dp.message(Command("help"))
async def help_cmd(message: types.Message):
    await message.answer("Просто напиши мне сообщение, и я отвечу")

@dp.message()
async def chat(message: types.Message):
    completion = client.chat.completions.create(
        model="google/gemini-2.0-flash-exp:free",
        messages=[{"role": "user", "content": message.text}]
    )
    await message.answer(completion.choices[0].message.content)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())