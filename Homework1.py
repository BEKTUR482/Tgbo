from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
import asyncio
import random
from config import token

bot=Bot(token=token)
dp=Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Привет! Напиши 'Камень', 'Ножницы' или 'Бумага', чтобы начать игру.")

@dp.message()
async def randomm(message:types.Message):
    hand=random.choice(['Камень', 'Ножницы', 'Бумага'])
    user_hand=message.text
    if user_hand==hand:
        await message.answer(f'Ничья. Было сгенерировано: {hand}')
    elif user_hand=='Камень' and hand=='Ножницы':
        await message.answer(f'Победа. Было сгенерировано: {hand}')
    elif user_hand=='Ножницы' and hand=='Бумага':
        await message.answer(f'Победа. Было сгенерировано: {hand}')
    elif user_hand=='Бумага' and hand=='Камень':
        await message.answer(f'Победа. Было сгенерировано: {hand}')
    else:
        await message.answer(f'Поражение.  Было сгенерировано: {hand}')

async def main():
        await dp.start_polling(bot)
if __name__=='__main__':
    try:
         asyncio.run(main())
    except KeyboardInterrupt:
        print('Выход')

