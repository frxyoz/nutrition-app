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
    api_key=os.getenv("OPENAI_API_KEY")
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
        'You are a nutritionist. I will provide the name of a food item. '
        'Please respond with a JSON object containing the following details:\n'
        '- **Calories**: Estimated calories per serving (whole number).\n'
        '- **RecommendedDailyIntake**: Recommended daily intake in grams (whole number).\n'
        '- **EatFrequency**: Suggested frequency of consumption per day (whole number).\n'
        '- **Description**: A brief description of the food item, including its nutritional benefits.\n'
        '- **Nutrients**: A breakdown of major nutrients, including carbohydrates, proteins, fats, vitamins, and minerals.\n\n'
        'Here is the format for your response:\n'
        '{\n'
        '  "FoodName": "<Food Name>",\n'
        '  "Calories": "<Estimated Calories>",\n'
        '  "RecommendedDailyIntake": "<Recommended Daily Intake in grams>",\n'
        '  "EatFrequency": "<Suggested Frequency per day>",\n'
        '  "Description": "<Brief Description>",\n'
        '  "Nutrients": {\n'
        '    "Carbohydrates": "<Amount in grams>",\n'
        '    "Proteins": "<Amount in grams>",\n'
        '    "Fats": "<Amount in grams>",\n'
        '    "Vitamins": ["<List of Key Vitamins>"],\n'
        '    "Minerals": ["<List of Key Minerals>"]\n'
        '  }\n'
        '}'
    )
    print(assistant_prompt)
    response_dict = get_json_response(assistant_prompt, message)
    return jsonify(response_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
