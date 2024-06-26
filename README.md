# Building a Predictive Web Application using Flask

Hosted website_link:
https://akhila-flask-2.onrender.com/

1. Introduction
   
In this project, we aimed to develop a web application using Flask to predict whether a user would purchase a product based on demographic features: age, salary, and gender. The application leverages a machine learning model trained on a dataset of social network ads.

2. Dataset Description
   
Source: The dataset (social_network_ads.csv) contains demographic information and a binary target variable (Purchased).

Features:

Age: Age of the user.
Salary: Estimated salary of the user.
Gender: Gender of the user (categorical: Male/Female).
Target Variable:
Purchased: Binary variable indicating whether the user purchased the product (1) or not (0).

3. Methodology

Data Preprocessing:

Checked for missing values and handled them appropriately (if any).
Encoded categorical variables (Gender) into numerical format if necessary.
Split the data into training and testing sets for model evaluation.
Model Selection and Training:
Chose a suitable machine learning algorithm (e.g., Logistic Regression, Decision Tree).
Trained the model on the training data to predict Purchased based on Age, Salary, and Gender.

Model Evaluation:

Evaluated model performance using metrics such as accuracy, precision, recall, and F1-score.
Selected the model with the best performance metrics for deployment.

4. Flask Application Development
   
Flask Setup:

Developed a Flask application (app.py) to handle HTTP requests and responses.
Created routes for:

Rendering an HTML form (index.html) to collect user inputs (age, salary, gender).
Processing form submission to make predictions using the trained model.
Displaying the prediction result (Will Purchase or Will Not Purchase) to the user (result.html).
HTML and CSS Integration:

Designed HTML templates (index.html for input form, result.html for prediction result) to provide a user-friendly interface.
Styled the templates using CSS for consistent and visually appealing presentation.

5. Deployment
   
Deployed the Flask application on a web server (Render).
Ensured all necessary files (app.py, HTML templates, CSS styles) were included and configured correctly.
Tested the deployed application to ensure functionality and performance.

