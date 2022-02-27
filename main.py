import asyncio
import random
import os

from telethon import TelegramClient
from telethon import functions, types

from report_text import generate_text

api_id = 1
api_hash = "empty-session-hash"
session_files_folder_relaive_path = "session_files"

client_list = []

print('Bot started, loading session profiles....')

session_files_list= [file for file in os.listdir(session_files_folder_relaive_path) if file.endswith('.session')]

for session_file in session_files_list:
    print(f"loading session for {session_file}...")
    client = TelegramClient(f"{session_files_folder_relaive_path}/{session_file}", api_id, api_hash)
    client.start()
    client_list.append(client)




async def main():
    number_of_channels_rep = 150

    telegram_list = open('telegram_db', 'r').readlines()
    random.shuffle(telegram_list)

    for (i,telegram_channel) in enumerate(telegram_list[:number_of_channels_rep]):
        if "https://" in telegram_channel:
            telegram_channel = telegram_channel.split('/')[-1]
        elif '@' in telegram_channel:
            telegram_channel = telegram_channel[1:]
        print(i+1, telegram_channel.strip())
        try:
            result = await client(functions.account.ReportPeerRequest(
                peer=telegram_channel,
                reason=types.InputReportReasonOther(),
                message=str(generate_text())
            ))
            print(result)
        except ValueError:
            print("Channel not found")
        await asyncio.sleep(10 + 2 * random.random())

for client in client_list:
    with client:
        client.loop.run_until_complete(main())

