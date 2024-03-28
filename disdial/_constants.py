import os
from disdial.__utils import path_converter

TOKEN = os.environ.get('DD_TOKEN')
CHANNEL_ID = os.environ.get('DD_CHANNEL_ID')
API_URL = f'https://discord.com/api/v10/channels/{CHANNEL_ID}/messages'
DD_TOKEN = os.environ.get('DD_AUTH_TOKEN')

API_URL = f'https://arpy8.pythonanywhere.com/data'
API_URL2 = f'https://disdial.onrender.com/all'

LOGS_FILE_PATH = path_converter("data/logs.txt")
JSON_FILE_PATH = path_converter("data/config.json")

HEADERS={
            'Authorization': f'Bot {TOKEN}',
            'Content-Type': 'application/json',
}
