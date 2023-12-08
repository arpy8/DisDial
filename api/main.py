import os
import requests
from flask import Flask, request, jsonify

# CONSTANTS
TOKEN = os.environ.get('DD_TOKEN')
CHANNEL_ID = os.environ.get('DD_CHANNEL_ID')

send_message_url = f'https://discord.com/api/v10/channels/{CHANNEL_ID}/messages'
headers={
            'Authorization': f'Bot {TOKEN}',
            'Content-Type': 'application/json',
        }

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"NOTE": "Hi."})

@app.route("/send", methods=["POST"])
def send_data():    
    try:
        username = request.json.get("username")  
        message = request.json.get("message") 
        data = f"{username}: {message}"
        
        if not data:
            return jsonify({"error": "Data not provided"}), 400

        post_message_to_server(data)
        return jsonify({"success": True})
    except Exception as e:
        print(e)
        return jsonify({"error": "Internal server error"}), 500

def post_message_to_server(message):
    try:
        send_message_data = {
            "content": message,
        }

        response = requests.post(send_message_url, json=send_message_data, headers=headers)
        if response.status_code != 200:
            print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print("Error sending message:", str(e))

# def read_message_from_server():
#     response = requests.get(f'https://discord.com/api/v10/channels/{CHANNEL_ID}/messages', headers=headers, params={'limit': 1})
#     data = response.json()

#     if response.status_code == 200 and data:
#         last_message = data[0]['content']
#         print(f'Last Message: {last_message}')
#     else:
#         print(f'Failed to fetch last message. Status code: {response.status_code}, Response: {response.text}')
    

if __name__ == "__main__":
    app.run()