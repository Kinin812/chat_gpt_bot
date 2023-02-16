import os
import openai
import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()

# Initialize the Telegram Bot API
bot = Bot(token=os.getenv('API_TOKEN'))
dp = Dispatcher(bot)

# Initialize the OpenAI API
openai.api_key = os.getenv('OPENAI')

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.answer('Hi there! How can I help you today?')


@dp.message_handler()
async def handle_message(message: types.Message):
    # Get the user's message
    text = message.text

    # Generate a response using OpenAI
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text

    # Send the response back to the user
    await message.answer(response)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
