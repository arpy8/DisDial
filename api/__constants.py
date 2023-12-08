import os 

TOKEN = os.environ.get('DD_TOKEN')
CHANNEL_ID = os.environ.get('DD_CHANNEL_ID')

send_message_url = f'https://discord.com/api/v10/channels/{CHANNEL_ID}/messages'
headers={
            'Authorization': f'Bot {TOKEN}',
            'Content-Type': 'application/json',
        }