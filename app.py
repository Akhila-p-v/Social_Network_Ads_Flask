import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the trained model
def load_model(filename):
    with open(filename, 'rb') as file:
        model = pickle.load(file)
        return model

rf_model = load_model('model.pkl')  # Load the Random Forest model

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get form input values
        age = float(request.form['age'])
        salary = float(request.form['salary'])
        gender = request.form['gender']  # Get gender as string
        
        # Encode Gender using One-Hot Encoding
        gender_male = 1 if gender == 'Male' else 0
        gender_female = 1 if gender == 'Female' else 0
        
        # Prepare the input for prediction
        input_data = np.array([[age, salary, gender_male, gender_female]])  # Include both Gender features
        
        print("Input Data Shape:", input_data.shape)  # Print shape for debugging
        
        # Make prediction
        prediction = rf_model.predict(input_data)
        
        # Convert prediction to human-readable form
        result = "Will Purchase" if prediction[0] == 1 else "Will Not Purchase"
        
        return render_template('prediction.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)


