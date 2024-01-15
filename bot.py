import asyncio
import logging

from aiogram import  Dispatcher

from handlers.echo import echo_router
from handlers.start import start_router
from handlers.get_id import get_id_router
from handlers.menu import menu_router
from loader import bot, db

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
       
    )

    logger.info("Starting bot")

    try:
        db.create_table_users()
    except Exception as err:
        print(err)

    dp: Dispatcher = Dispatcher()

    dp.include_routers(
        start_router,
        menu_router,
        get_id_router,

        echo_router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")
