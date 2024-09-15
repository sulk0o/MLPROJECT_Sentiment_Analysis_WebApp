# MLPROJECT_Sentiment_Analysis_WebApp

**Created:** 9/14/24  
**Purpose:** First ML project focused on cleaning data, training a basic model, and deploying locally.

This project was coded entirely by me, except for the `index.html` file in the `templates` folder. The HTML file was generated with ChatGPT, as I don't know HTML and am lazy.
A quick note, I just realized in all my files, I spelled IMDB "IMBD", thats embarrassing...

### **About the Project**:
The goal of this project was simple: 
- Get a dataset (IMDB movie reviews)
- Clean the data
- Train a basic machine learning model
- Deploy it locally using Flask for testing

This is my first-ever ML project, so it was mainly a learning exercise to understand the basic workflow of an ML project, from data cleaning to model deployment.

### **Model Information**:
- I tested a few different **sklearn** models using the `testing.ipynb` file. 
- The **Logistic Regression** model worked the best on this dataset, with **L1 regularization** to combat overfitting.
- The model’s accuracy dropped slightly from **89% to 87%** with regularization, suggesting some overfitting was present initially.
- The **FinalModel.ipynb** contains the final model I used with the Flask app.

### **Generalization**:
While the dataset was based on **IMDB reviews**, the model seems fairly accurate when tested on generalized product reviews, suggesting some transferability.

### **How to Try it Out**:

If you want to test this project locally (even though it's a basic learning exercise), you can follow these steps:

1. git clone https://github.com/sulk0o/MLPROJECT_Sentiment_Analysis_WebApp.git
2. cd MLPROJECT_Sentiment_Analysis_WebApp
3. pip install -r requirements.txt
4. python app.py
5. Visit http://127.0.0.1:5000/
6. Profit.
