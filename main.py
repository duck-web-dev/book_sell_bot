from telebot import TeleBot
import telebot.types as tt
import libs.env as env
from libs.tg.handlers import add_handlers, not_registered_handler
from libs.tg.middleware import AuthMiddleware, WaitAnswerMiddleware
from libs.tg.wait_for_reply import message_handler, cancel_wait_answer
from libs.db import db


bot = TeleBot(env.get('TG_KEY') or '', parse_mode='HTML', use_class_middlewares=True)

bot.setup_middleware(WaitAnswerMiddleware(message_handler, cancel_wait_answer))
bot.setup_middleware(AuthMiddleware(lambda u: not_registered_handler(bot, u)))
add_handlers(bot)

bot.infinity_polling()