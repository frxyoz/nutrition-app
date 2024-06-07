import os
from flask import Flask, jsonify, request, json
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

load_dotenv()
# Set up OpenAI API key
client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)

def get_json_response(system_prompt, user_prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        # Extract and parse JSON content
        response_content = response.choices[0].message.content
        if response_content:
            return json.loads(response_content)  # Assuming response content is a valid JSON string
        else:
            return {"error": "Error retrieving response from OpenAI API."}
    except Exception as e:
        return {"error": str(e)}

@app.route('/test/<message>')
def test(message):
    print(message)
    return jsonify({"message": message})

@app.route('/convo/<message>', methods=['GET'])
def conversation(message):
    assistant_prompt = (
        'You are a nutritionist. I will give you a name of a food. '
        'Please reply with the following: Calories, recommended daily intake, eat frequency (how many units to eat daily), and a description. '
        'Estimate the numbers and give a whole number for all the numbers.'
        'Respond in a json form!'

    )
    print(assistant_prompt)
    response_dict = get_json_response(assistant_prompt, message)
    return jsonify(response_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)