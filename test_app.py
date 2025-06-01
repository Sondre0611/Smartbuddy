from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Tillat CORS for frontend

# Chat-endepunkt
@app.route('/v1/chat/completions', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    if not user_message:
        return jsonify({'error': 'Mangler "message" i JSON'}), 400

    # Her kan du koble på OpenAI API, men for nå sender vi tilbake en enkel respons
    response_text = f"SmartBuddy sier: {user_message}"

    return jsonify({'response': response_text})

# Feedback-endepunkt
@app.route('/v1/feedback', methods=['POST'])
def feedback():
    data = request.json
    message = data.get('message')
    response = data.get('response')
    feedback_type = data.get('feedback')
    improved_answer = data.get('improved_answer', None)

    if not all([message, response, feedback_type]):
        return jsonify({'error': 'Mangler data i tilbakemelding'}), 400

    log_entry = {
        'message': message,
        'response': response,
        'feedback': feedback_type,
        'improved_answer': improved_answer
    }

    filename = 'feedback_log.json'

    # Les eksisterende logg hvis den finnes
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                logs = []
    else:
        logs = []

    # Legg til ny tilbakemelding
    logs.append(log_entry)

    # Lagre fil
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)

    return jsonify({'status': 'OK'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
