import telebot.types as tt
from typing import Callable
from threading import Event


class Data:
	def __init__(self):
		self.event = Event()
		self.answer: str | None = None

users: dict[int, Data] = {}


def wait_answer(m: int | tt.Message, timeout: int | None = 120, timeout_callback: Callable | None = None) -> str | None:
	if not isinstance(m, int):
		m = m.chat.id
	if users.get(m, False):
		raise ValueError('Already waiting for answer')
	users[m] = Data()
	users[m].event.wait(timeout)
	ans = users[m].answer
	del users[m]
	if ans is None:
		if timeout_callback:
			timeout_callback()
		return None
	else:
		return ans

def cancel_wait_answer(m: int | tt.Message):
	if not isinstance(m, int):
		m = m.chat.id
	if not users.get(m, False):
		raise ValueError('Already cancelled')
	users[m].answer = None
	users[m].event.set()


def message_handler(msg: tt.Message) -> bool:
	id = msg.from_user.id
	c = users.get(id, None)
	if c is None:
		return True
	else:
		t = msg.html_text or msg.html_caption
		if not t:
			return True
		else:
			c.answer = t
			c.event.set()
			return False