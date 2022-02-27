from telethon import TelegramClient
from telethon import functions, types
import questionary

api_id = int(questionary.password('Api ID:').ask())
api_hash = questionary.password('Api hash:').ask()
session_file_name = questionary.text('session file name:').ask()



client = TelegramClient(session_file_name, api_id, api_hash)
client.start()