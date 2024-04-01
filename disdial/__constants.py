import os
import pkg_resources

def path_converter(file_name):
    return pkg_resources.resource_filename('disdial', file_name)

TOKEN = os.environ.get('DD_TOKEN')
CHANNEL_ID = os.environ.get('DD_CHANNEL_ID')
API_URL = f'https://discord.com/api/v10/channels/{CHANNEL_ID}/messages'
DD_TOKEN = os.environ.get('DD_AUTH_TOKEN')

API_URL = f'https://disdial-5glu.onrender.com/data'
API_URL2 = f'https://disdial-5glu.onrender.com/all'

LOGS_FILE_PATH = path_converter("data/logs.txt")
JSON_FILE_PATH = path_converter("data/config.json")

HEADERS={
            'Authorization': f'Bot {TOKEN}',
            'Content-Type': 'application/json',
}

LOCALAPP_DATA = os.getenv('LOCALAPPDATA')
PACKAGE_PATH = os.path.join(LOCALAPP_DATA, 'Packages', 'Microsoft.WindowsTerminal_8wekyb3d8bbwe')
SETTINGS_PATH = os.path.join(PACKAGE_PATH, 'LocalState', 'settings.json')