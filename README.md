This project is a web application designed to predict the likelihood of heart disease in a patient based on various health parameters. The app utilizes a machine learning model (Logistic Regression) trained on a heart disease dataset and is built using Python with Flask as the backend framework. The frontend is implemented using HTML, CSS, and JavaScript, making the app both functional and responsive.

Features:

->Interactive Form: Users can input their medical data, such as age, cholesterol levels, chest pain type, and more, through a user-friendly form.
->Real-time Predictions: Upon submitting the form, the app sends the data to the backend, where the machine learning model processes the input and provides a prediction.
->Responsive Design: The frontend is built with a clean and responsive design, ensuring usability across various devices.
->ML Model: A logistic regression model is trained to predict the likelihood of heart disease based on the input data.

Technologies Used:

->Frontend: HTML, CSS, JavaScript
->Backend: Flask (Python)
->Machine Learning: Logistic Regression (scikit-learn)
->Model Serialization: pickle
->Dataset: The model is trained on a heart disease dataset with features like age, cholesterol, blood pressure, and more.

How It Works:

1. The user inputs their health information in the form.
2. The data is sent to the Flask backend via a POST request.
3. The backend loads the pre-trained logistic regression model and processes the input data.
4. The model returns a prediction (either "Heart Disease Detected" or "No Heart Disease").
5. The result is displayed to the user in real-time on the web page.
