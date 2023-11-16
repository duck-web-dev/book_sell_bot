from telebot.handler_backends import BaseMiddleware, SkipHandler, CancelUpdate
from libs.db.models import User
from typing import Callable
import telebot.types as tt



class AuthMiddleware(BaseMiddleware):
	def __init__(self, user_not_found_handler: Callable[[int], None]):
		# self.update_sensitive = True
		self.update_types = ['message', 'callback_query']
		self.user_not_found_handler = user_not_found_handler

	def pre_process(self, msg: tt.Message | tt.CallbackQuery, data):
		tuser = msg.from_user
		user: User | None = User.get_or_none(id=tuser.id)
		if user is None:
			if type(msg) == tt.Message:
				self.user_not_found_handler(tuser.id)
			else:
				return CancelUpdate()
		else:
			data['user'] = user

	def post_process(*args, **kwargs): ...


class WaitAnswerMiddleware(BaseMiddleware):
	def __init__(self, handler: Callable[[tt.Message], bool], cancel_wait: Callable[[int | tt.Message], None]):
		self.update_types = ['message']
		self.handler = handler
		self.cancel_wait = cancel_wait
	
	def pre_process(self, message: tt.Message, data):
		if message.chat.type == 'private':
			c = self.handler(message)
			t = message.text or message.caption
			if not c:
				return CancelUpdate()
			elif (t is None) or (message.text[0] == '/'):
				try:	self.cancel_wait(message)
				except:	pass
		
	def post_process(self, message, data, exception): ...