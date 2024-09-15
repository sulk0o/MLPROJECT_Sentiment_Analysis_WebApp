from flask import Flask, request, render_template
import joblib

# Initialize the Flask app
app = Flask(__name__)

# Load the trained logistic regression model and the TF-IDF vectorizer
model = joblib.load('logistic_regression_model_sentimentPrediction.pkl')  # Make sure the file is in your project folder
vectorizer = joblib.load('tfidf_vectorizer.pkl')  # Make sure the file is in your project folder

# Define the home route (this renders the input form)
@app.route('/')
def home():
    return render_template('index.html')  # This will serve the HTML file

# Define the route that handles form submissions and returns predictions
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the review input from the form
        review = request.form['review']  # 'review' refers to the name in the HTML form
        
        # Vectorize the user input using the saved TF-IDF vectorizer
        data = vectorizer.transform([review])
        
        # Make a prediction using the logistic regression model
        prediction = model.predict(data)[0]
        
        # Convert the numerical prediction to a human-readable format
        sentiment = "Positive" if prediction == 1 else "Negative"
        
        # Render the HTML file again but this time include the prediction result
        return render_template('index.html', prediction=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
