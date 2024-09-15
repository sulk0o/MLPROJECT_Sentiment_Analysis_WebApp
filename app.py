from flask import Flask, request, render_template
import joblib
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Initialize the Flask app
app = Flask(__name__)

# Load the trained logistic regression model and the TF-IDF vectorizer
model = joblib.load('logistic_regression_model_sentimentPrediction.pkl')  # Make sure the file is in your project folder
vectorizer = joblib.load('tfidf_vectorizer.pkl')  # Make sure the file is in your project folder

# Clean, same as in ipynb
def clean(review):
    # Remove digits
    rem_dig = ''.join([i for i in review if not i.isdigit()])
    
    # Strip leading/trailing whitespace
    rem_ws = rem_dig.strip()
    
    # Convert text to lowercase
    rem_c = rem_ws.lower()
    
    # Tokenize the text
    tokenized_review = word_tokenize(rem_c)
    
    # Remove stopwords
    stopwords_set = set(stopwords.words("english"))
    rem_stopwords = ' '.join([word for word in tokenized_review if word not in stopwords_set])
    
    # Remove punctuation, allowing "!" and "-"
    rem_punctuation = re.sub(r'[^\w\s\!-]', "", rem_stopwords)
    
    # Replace hyphens ("-") with spaces
    rem_punctuation = re.sub(r'[-]', " ", rem_punctuation)
    
    return rem_punctuation

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
        
        # Clean the user input using the modified clean function
        cleaned_review = clean(review)
        
        # Vectorize the user input using the saved TF-IDF vectorizer
        data = vectorizer.transform([review])
        
        # Make a prediction using the logistic regression model
        prediction = model.predict(data)[0]
        
        # Convert the numerical prediction to a human-readable format
        sentiment = "Positive" if prediction == 1 else "Negative"
        
        # Render the HTML file again but this time include the prediction result
        return render_template('index.html', prediction=sentiment)

if __name__ == '__main__':
    app.run()
