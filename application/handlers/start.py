from aiogram import Router, types, F

router = Router()

@router.message(F.text == "/start")
async def start(message: types.Message):
    await message.answer("Привет, я бот")