from flask import Flask, request, jsonify
import os

app = Flask(__name__)

OPENROUTER_API_KEY = os.environ['OPENROUTER_API_KEY']
MODEL = os.environ['MODEL']
openai_client = OpenAI(
  base_url=MODEL,
  api_key=OPENROUTER_API_KEY,
)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    model = data['model']
    messages = data['messages']
    response = openai_client.chat.completions.create(

        model=model,
        messages=messages,
    )
    return jsonify(response.choices[0].message.content)

if __name__ == '__main__':
    app.run(debug=True)