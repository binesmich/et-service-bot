import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from fastapi import FastAPI
import asyncio

BOT_TOKEN = "8627625987:AAHAG-4_nr7yDkbKIhR5F_6hZgKxOlGlS_w"
https://et-service-bot.onrender.com

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
app = FastAPI()

@dp.message(CommandStart())
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🚀 ET-Service አፕ ክፈት",
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ]
        ]
    )
    await message.answer(
        f"ሰላም {message.from_user.first_name}! ወደ ET-Service እንኳን ደህና መጡ።\n"
        "አገልግሎት ለመጠየቅ ወይም በሰራተኛነት ለመመዝገብ ከታች ያለውን ቁልፍ ይጫኑ።",
        reply_markup=keyboard
    )

@app.post("/api/register-worker")
async def register_worker(data: dict):
    print("አዲስ ሰራተኛ ተመዝግቧል:", data)
    return {"status": "success", "message": "ምዝገባው ተሳክቷል!"}

async def main():
    import uvicorn
    config = uvicorn.Config(app, host="0.0.0.0", port=8000)
    server = uvicorn.Server(config)
    
    await asyncio.gather(
        dp.start_polling(bot),
        server.serve()
    )

if __name__ == "__main__":
    asyncio.run(main())
