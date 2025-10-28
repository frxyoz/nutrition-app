# Nutrition App

A demo Android application that helps users make informed and healthier dietary choices by scanning food items and receiving detailed nutritional information.

## Overview

The Nutrition App combines computer vision, natural language processing, and real-time data storage to provide comprehensive nutritional analysis of food items. Users can scan food via images, and the app identifies the food category using TensorFlow Lite, then leverages the OpenAI API to provide detailed nutritional information including calorie count, macronutrient breakdown, and other nutrition facts.

## Features

- **Image-Based Food Scanning**: Scan food items via camera or image gallery
- **AI-Powered Food Identification**: Uses TensorFlow Lite to identify food categories
- **Intelligent Nutritional Analysis**: Leverages OpenAI GPT API to analyze and interpret food descriptions
- **Comprehensive Nutrition Facts**: Displays calorie count, macronutrient breakdown (carbs, proteins, fats), vitamins, and minerals
- **Scan History Tracking**: Track scan history for each user
- **User Authentication**: Secure authentication with Firebase Auth
- **Cloud Data Storage**: Store and retrieve data using Firebase Firestore

## Technology Stack

- **Frontend**: Flutter (Dart)
- **Backend/API**: Flask (Python), OpenAI GPT API
- **ML Model**: TensorFlow Lite
- **Database & Authentication**: Firebase (Firestore and Firebase Auth)
- **Platform**: Android

## Project Structure

```
nutrition-app/
├── app.py                 # Flask backend API server
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not tracked)
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

Note: The Flutter frontend code is maintained in a separate repository.

---

## Backend (Flask API)

The backend is a Flask REST API that provides nutritional information for food items using the OpenAI GPT API.

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- OpenAI API key

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/frxyoz/nutrition-app.git
   cd nutrition-app
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. **Create a `.env` file** in the root directory:
   ```bash
   touch .env
   ```

2. **Add your OpenAI API key** to the `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

   > ⚠️ **Important**: Never commit your `.env` file to version control. It's already included in `.gitignore`.

### Running the Backend

1. **Start the Flask development server**:
   ```bash
   python app.py
   ```

   The server will start on `http://0.0.0.0:5000` with debug mode enabled.

2. **For production deployment**, use gunicorn:
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

### API Endpoints

#### 1. Test Endpoint

**GET** `/test/<message>`

A simple test endpoint to verify the server is running.

**Parameters**:
- `message` (string, path parameter): Any test message

**Example Request**:
```bash
curl http://localhost:5000/test/hello
```

**Example Response**:
```json
{
  "message": "hello"
}
```

#### 2. Nutritional Information Endpoint

**GET** `/convo/<message>`

Retrieves comprehensive nutritional information for a given food item using OpenAI GPT.

**Parameters**:
- `message` (string, path parameter): Name of the food item

**Example Request**:
```bash
curl http://localhost:5000/convo/apple
```

**Example Response**:
```json
{
  "FoodName": "Apple",
  "Calories": "95",
  "RecommendedDailyIntake": "200",
  "EatFrequency": "2",
  "Description": "Apples are a nutritious fruit rich in fiber, vitamin C, and various antioxidants. They support heart health, aid digestion, and may help with weight management.",
  "Nutrients": {
    "Carbohydrates": "25",
    "Proteins": "0.5",
    "Fats": "0.3",
    "Vitamins": ["Vitamin C", "Vitamin A", "Vitamin K"],
    "Minerals": ["Potassium", "Calcium", "Magnesium"]
  }
}
```

**Response Fields**:
- `FoodName`: Name of the food item
- `Calories`: Estimated calories per serving (whole number)
- `RecommendedDailyIntake`: Recommended daily intake in grams (whole number)
- `EatFrequency`: Suggested frequency of consumption per day (whole number)
- `Description`: Brief description including nutritional benefits
- `Nutrients`: Detailed breakdown of macronutrients, vitamins, and minerals

**Error Response**:
```json
{
  "error": "Error description"
}
```

### Testing the Backend

1. **Using curl**:
   ```bash
   # Test endpoint
   curl http://localhost:5000/test/working
   
   # Get nutrition info for an apple
   curl http://localhost:5000/convo/apple
   
   # Get nutrition info for chicken breast
   curl http://localhost:5000/convo/chicken%20breast
   ```

2. **Using a web browser**:
   - Navigate to `http://localhost:5000/test/hello`
   - Navigate to `http://localhost:5000/convo/banana`

3. **Using Python**:
   ```python
   import requests
   
   response = requests.get('http://localhost:5000/convo/orange')
   print(response.json())
   ```

---

## Frontend (Flutter/Android)

The frontend is a Flutter-based Android application that provides the user interface for scanning and viewing nutritional information.

### Prerequisites

- Flutter SDK (latest stable version)
- Android Studio or VS Code with Flutter extensions
- Android SDK and emulator or physical Android device
- Firebase project with Firestore and Authentication enabled

### Installation

1. **Install Flutter**: Follow the official Flutter installation guide for your operating system:
   - https://docs.flutter.dev/get-started/install

2. **Verify Flutter installation**:
   ```bash
   flutter doctor
   ```

3. **Clone the frontend repository** (if separate):
   ```bash
   # Replace with actual frontend repository URL
   git clone <frontend-repo-url>
   cd <frontend-directory>
   ```

4. **Install dependencies**:
   ```bash
   flutter pub get
   ```

### Configuration

1. **Firebase Setup**:
   - Create a Firebase project at https://console.firebase.google.com
   - Add an Android app to your Firebase project
   - Download the `google-services.json` file
   - Place it in the `android/app/` directory
   - Enable Firestore and Firebase Authentication in the Firebase console

2. **TensorFlow Lite Model**:
   - Place your trained TensorFlow Lite model file in the `assets/` directory
   - Update the model path in the app configuration

3. **Backend API Configuration**:
   - Update the API base URL in the app configuration to point to your Flask backend
   - Example: `http://your-server-ip:5000` or `https://your-domain.com`

### Running the Frontend

1. **Connect an Android device** or start an emulator:
   ```bash
   flutter devices
   ```

2. **Run the app**:
   ```bash
   flutter run
   ```

3. **For release build**:
   ```bash
   flutter build apk --release
   ```

   The APK will be generated at `build/app/outputs/flutter-apk/app-release.apk`

### Frontend Features

- **Camera Integration**: Take photos of food items directly from the app
- **Gallery Selection**: Choose existing photos from the device gallery
- **Real-time Analysis**: Get instant nutritional information after scanning
- **History View**: Browse through previously scanned food items
- **User Profile**: Manage user account and preferences
- **Offline Support**: Cache nutritional data for offline access

---

## Troubleshooting

### Backend Issues

**Problem**: `ModuleNotFoundError: No module named 'flask'`
- **Solution**: Ensure you've activated the virtual environment and installed dependencies:
  ```bash
  source venv/bin/activate  # or venv\Scripts\activate on Windows
  pip install -r requirements.txt
  ```

**Problem**: `openai.OpenAIError: The api_key client option must be set`
- **Solution**: Verify your `.env` file exists and contains the correct OpenAI API key:
  ```
  OPENAI_API_KEY=sk-...
  ```

**Problem**: CORS errors when accessing from frontend
- **Solution**: The Flask app already has CORS enabled via `Flask-Cors`. Ensure the frontend is making requests to the correct backend URL.

**Problem**: Port 5000 already in use
- **Solution**: Either stop the process using port 5000 or run the Flask app on a different port:
  ```bash
  python app.py --port 8080
  ```
  Or modify `app.py` to use a different port.

### Frontend Issues

**Problem**: `google-services.json` not found
- **Solution**: Download the configuration file from your Firebase project and place it in `android/app/`

**Problem**: TensorFlow Lite model fails to load
- **Solution**: Verify the model file exists in the `assets/` directory and the path is correctly specified in the app configuration

**Problem**: Network request failed
- **Solution**: 
  - Check that the Flask backend is running
  - Verify the API base URL is correctly configured in the frontend
  - For Android emulator, use `http://10.0.2.2:5000` instead of `localhost`
  - For physical device, ensure both device and server are on the same network

---

## Contributing

This is a demo project developed for educational purposes. Feel free to fork and modify for your own learning.

## License

This project is for educational purposes only.

## Author

Developed by **Olric Zeng**, Coding Minds intern 2024.
