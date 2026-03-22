from telethon import TelegramClient, events
import os

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
your_username = os.environ.get("USERNAME")

groups = [
    'valicante',
    'Alicantebaraholka',
    'amigosalicanteucrania',
    'spain_useful',
    'dopomogaispania',
    'spainlives',
    'costablanca_es',
    'CostaBlancaaa'
]

keywords = [
    'трансфер', 'transfer', 'такси', 'таксі',
    'переезд', 'переїзд',
    'груз', 'доставка', 'перевезення',
    'нужно', 'ищу', 'кто может'
]

client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage(chats=groups))
async def handler(event):
    text = event.raw_text.lower()

    if any(word in text for word in keywords):
        message = f"🚨 Новая заявка:\n\n{text}"
        await client.send_message(your_username, message)

client.start()
print("Бот запущен 🚀")
client.run_until_disconnected()
