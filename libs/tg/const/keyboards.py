from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from libs.db.models import User
from typing import Type


ok = InlineKeyboardMarkup([
	[InlineKeyboardButton("OK", callback_data="deleteme"), ]
])
okmenu = InlineKeyboardMarkup([
	[InlineKeyboardButton("🎛️ Main menu", callback_data="main_menu"), ],
	[InlineKeyboardButton("OK", callback_data="deleteme"), ]
])
cancel = InlineKeyboardMarkup([
	[InlineKeyboardButton("❌ Cancel", callback_data="cancel"), ]
])
cancelok = InlineKeyboardMarkup([
	[InlineKeyboardButton("❌ Cancel", callback_data="deleteme"), ]
])
cancel_del = InlineKeyboardMarkup([
	[InlineKeyboardButton("❌ Cancel", callback_data="cancel_del"), ]
])

welcome = menu = InlineKeyboardMarkup([
	[InlineKeyboardButton("🎛️ Main menu", callback_data="main_menu"), ],
])


mainmenu = InlineKeyboardMarkup([
	[InlineKeyboardButton("👤 Personal area", callback_data="personal"), ],
	[InlineKeyboardButton("📜 Catalog", callback_data="catalog"), ],
	[InlineKeyboardButton("🧑‍💻 Support", url="tg://user?id=1969100058"), ],
])

personal = InlineKeyboardMarkup([
	[InlineKeyboardButton("💱 Top up", callback_data="topup"), ],
	[InlineKeyboardButton("📜 My books", callback_data="history"), ]
])