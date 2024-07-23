from flask import Flask, request, jsonify
import json
import dotenv
import os

app = Flask(__name__)

dotenv.load_dotenv()

openrouter_api_key = os.environ['OPENROUTER_API_KEY']
your_site_url = os.environ['YOUR_SITE_URL']
your_site_name = os.environ['YOUR_SITE_NAME']

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    messages = data['messages']
    response = {
        "role": "system",
        "content": (
            "Você é um assistente que sempre responde em portugues, muito educado que sempre responde de forma amigavel "
 "
        )
    }

    for message in messages:
        if message['role'] == 'user':
            response['content'] += f"\n{message['content']}"

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5020)