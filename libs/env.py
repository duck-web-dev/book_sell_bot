from dotenv import load_dotenv, find_dotenv
import os

if not load_dotenv(find_dotenv()):
	raise RuntimeError(".env didn't load")

def get(key: str) -> str | None:
	return os.environ.get(key, None)