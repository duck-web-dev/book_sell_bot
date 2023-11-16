from libs.db.models import User


broken = "🚧 <b>This option is unavailable now</b> 🚧"
error  = "🚧 <b>Error occured. Please try again later</b> 🚧"

welcome = "🙋 <b>Hi! Welcome to IT Books shop!</b>"
menu = "<b>Main menu</b>"

def personal(user: User, name: str):
	return f'''
<b>Hi, {name}!</b>

💸 <i>Balance:</i> <b>{user.balance:.2f}</b>
📜 <i>Purchases made:</i> <b>{len(user.purchases or [])}</b>
	'''

def books(user: User):
	return "😢 <b>You didn't buy anything yet.</b>"

# def catalog(id: int):