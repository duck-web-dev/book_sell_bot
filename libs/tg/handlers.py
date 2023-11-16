from typing import Callable, Union, Any
from libs.db.models import User
from threading import Thread
from telebot import TeleBot
import telebot.types as tt
import libs.tg.const.text as t
import libs.tg.const.keyboards as kb



class CallbackHandler:
	def __init__(self, f: Callable, supports_message = True, supports_callback_query = True):
		self.function = f
		self.supports_message = supports_message
		self.supports_callback_query = supports_callback_query

cb_ = Union[tt.Message, tt.CallbackQuery]
q_handlers: dict[str, CallbackHandler] = {}
def q(func: Callable[[tt.CallbackQuery, User], None] | Callable[[cb_, User], None],
	  supports_message = True, supports_callback_query = True):
	q_handlers[func.__name__] = CallbackHandler(func, supports_message, supports_callback_query)
	return func

def add_handlers(bot: TeleBot):
	def th(target: Callable):
		(thread := Thread(target=target)).start()
	def m(user: User, text: str, keyboard: kb.InlineKeyboardMarkup | None = None):
		return bot.send_message(user.id, text, reply_markup=keyboard)
	def d(msg: tt.Message):
		bot.delete_message(msg.chat.id, msg.id)

	@q
	def deleteme(msg: tt.CallbackQuery, user: User): d(msg.message)

	@q
	def main_menu(msg: cb_, user: User):
		m(user, t.menu, kb.mainmenu)
	
	# @q
	# def catalog(msg: cb_, user: User):
		# m(user, t.catalog, kb.catalog)

	@q
	def personal(msg: cb_, user: User):
		m(user, t.personal(user, msg.from_user.full_name), kb.personal)

	@q
	def topup(msg: cb_, user: User):
		m(user, t.broken, kb.ok)
	@q
	def history(msg: cb_, user: User):
		m(user, t.books(user), kb.ok)


	# Query handlers
	@bot.callback_query_handler(func=lambda x: True)
	def handle_callback_query(query: tt.CallbackQuery, user: User):
		cmd, *args = filter(len, query.data.split(';'))
		print(user.id, cmd, args)
		if cmd in q_handlers:
			if not (f := q_handlers[cmd]).supports_callback_query:
				raise RuntimeError('Handler does not support callback query')
			f = f.function
			if len(args) > 0:
				th(lambda: f(query, user, *args))
			else:
				th(lambda: f(query, user))


	# Message andlers
	bot.register_message_handler(callback=main_menu, chat_types=['private'], commands=['help', 'menu', 'start'])


def not_registered_handler(bot: TeleBot, user_id: int):
	u: User = User.create(id=user_id)
	bot.send_message(user_id, '👋')
	bot.send_message(user_id, t.welcome, reply_markup=kb.welcome)