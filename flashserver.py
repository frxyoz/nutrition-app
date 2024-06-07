from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from openai import OpenAI
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

load_dotenv()
client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)

def get_json_response(system_prompt, user_prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response.choices[0].message.content

def get_standard_response(system_prompt, user_prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response.choices[0].message.content

@app.route('/convo/<message>', methods=['GET'])
def conversation(message):
    # Start the conversation with the Assistant
    assistant_prompt = (
        'You are a nutritionist. I will give you a name of a food. '
        'Please reply with the following: Calories, recommended daily intake, eat frequency, and a description. '
        'Estimate the numbers and give a whole number for all the numbers.'
    )
    response = get_json_response(assistant_prompt, message)
    return {"response": response}

if __name__ == '__main__':
    app.run(host='0.0.0.0')
