from flask import Flask, request, jsonify
from api import key  
from bot import chat1

app = Flask(__name__)

@app.route('/process_message', methods=['POST'])
def process_message():
    try:
        data = request.get_json()
        user_message = data['message']

        response_message = chat1(user_message)

        return jsonify({'response': response_message})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
