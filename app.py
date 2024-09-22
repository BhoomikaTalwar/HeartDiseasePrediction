from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Loading machine learning model 
model = joblib.load('model.pkl')

# Defining prediction route
@app.route('/predict', methods=['POST']) 
def predict():
    # Getting the input data from the request
    data = request.get_json()
    
    # Converting to a DataFrame 
    input_data = pd.DataFrame([data], 
                              columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
                                       'thalach','exang', 'oldpeak', 'slope', 'ca', 'thal' ])
    
    # Making a prediction
    prediction = model.predict(input_data)[0]
    # Returning the result as JSON
    return jsonify({'prediction': int(prediction)})
    
# Defining route to render the main web page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
