import os
import requests
from flask import Flask, request, jsonify, abort

# CONSTANTS
TOKEN = os.environ.get('DD_TOKEN')
CHANNEL_ID = os.environ.get('DD_CHANNEL_ID')
API_URL = f'https://discord.com/api/v10/channels/{CHANNEL_ID}/messages'
DD_TOKEN = os.environ.get('DD_AUTH_TOKEN')

headers={
            'Authorization': f'Bot {TOKEN}',
            'Content-Type': 'application/json',
        }


app = Flask(__name__)

@app.before_request
def check_auth():
    token = request.headers.get('Authorization')
    if token != DD_TOKEN:
        abort(401, 'Unauthorized access >:(')

@app.route("/")
def index():
    return jsonify({"NOTE": "Hi."})

from flask import request, jsonify
import requests

@app.route("/data", methods=["POST", "GET"])
def send_data():
    try:
        if request.method == "POST":
            time = request.json.get("time")
            username = request.json.get("username")
            message = request.json.get("message")
            
            data = f"[{time}] {username}: {message}"

            if not data:
                return jsonify({"error": "Data not provided"}), 400

            post_message_to_server(data)
            
            return jsonify({"status": "ok"})

        elif request.method == "GET":
            messages = []

            has_more_messages = True
            while has_more_messages:
                response = requests.get(f'https://discord.com/api/v10/channels/{CHANNEL_ID}/messages', headers=headers, params={'limit': 100})
                data = response.json()

                if response.status_code == 200 and data:
                    last_messages = [msg['content'] for msg in data]
                    messages.extend(last_messages)
                    has_more_messages = len(data) == 100
                else:
                    print(f'Failed to fetch messages. Status code: {response.status_code}, Response: {response.text}')
                    return jsonify({"error": "Couldn't fetch messages"}), 400

            return jsonify({"messages": messages})

    except Exception as e:
        print(e)
        return jsonify({"error": "Internal server error"}), 500


def post_message_to_server(message):
    try:
        send_message_data = {
            "content": message,
        }

        response = requests.post(API_URL, json=send_message_data, headers=headers)
        if response.status_code != 200:
            print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print("Error sending message:", str(e))


@app.route("/all", methods=["GET"])
def get_all_messages():
    try:
        params = {
            'limit': 100
        }

        response = requests.get(API_URL, headers=headers, params=params)
        data = response.json()

        if response.status_code == 200:
            messages = [message['content'] for message in data]
        else:
            messages = []
            
        return messages

    except Exception as e:
        print("Error sending message:", str(e))

if __name__ == "__main__":
    app.run()