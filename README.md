This project is a web application designed to predict the likelihood of heart disease in a patient based on various health parameters. The app utilizes a machine learning model (Logistic Regression) trained on a heart disease dataset and is built using Python with Flask as the backend framework. The frontend is implemented using HTML, CSS, and JavaScript, making the app both functional and responsive.

Features:

1. Interactive Form: Users can input their medical data, such as age, cholesterol levels, chest pain type, and more, through a user-friendly form.
2. Real-time Predictions: Upon submitting the form, the app sends the data to the backend, where the machine learning model processes the input and provides a prediction.
3. Responsive Design: The frontend is built with a clean and responsive design, ensuring usability across various devices.
4. ML Model: A logistic regression model is trained to predict the likelihood of heart disease based on the input data.

Technologies Used:
1. Frontend: HTML, CSS, JavaScript
2. Backend: Flask (Python)
3. Machine Learning: Logistic Regression (scikit-learn)
4. Model Serialization: pickle
5. Dataset: The model is trained on a heart disease dataset with features like age, cholesterol, blood pressure, and more.

How It Works:

1. The user inputs their health information in the form.
2. The data is sent to the Flask backend via a POST request.
3. The backend loads the pre-trained logistic regression model and processes the input data.
4. The model returns a prediction (either "Heart Disease Detected" or "No Heart Disease").
5. The result is displayed to the user in real-time on the web page.

Dataset:
The dataset used in this project contains the following features-
1. Age: Age of the patient
2. Sex: Gender (1 = Male, 0 = Female)
3. Chest Pain Type (cp): 0 to 3
4. Resting Blood Pressure (trestbps): mmHg
5. Serum Cholesterol (chol): mg/dl
5. Fasting Blood Sugar (fbs): 1 if >120 mg/dl, 0 otherwise
6. Resting ECG (restecg): 0, 1, or 2
7. Max Heart Rate (thalach): Maximum heart rate achieved
8. Exercise-induced Angina (exang): 1 = Yes, 0 = No
9. ST Depression (oldpeak): Relative to rest
10. Slope: Slope of peak exercise ST segment
11. Number of Major Vessels (ca): 0 to 3
12. Thalassemia (thal): 1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect
13. Target: 1 indicates presence of heart disease, 0 indicates absence
