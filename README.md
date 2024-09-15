# MLPROJECT_Sentiment_Analysis_WebApp
Created 9/14/24, first ML project, wanted to clean data, train a very basic model, and deploy locally to use. This project was coded completely by me, except the index.html file in templates. This was generated with chatGPT, as I do not know html, and am lazy. The purpose of this project was, as I already said, to simply get a dataset, clean it, train a basic model on it, and deploy it locally for me to test. This is my first ever ML project of some sort, and was mainly just to learn the very basics of things. The testing ipynb file was to test a few different sklearn models to see which ones worked better. Overall, a logistic regression model seemed to work best for the dataset, and I used L1 regularization to fight overfitting. This reduced the model accurazy from 89% to 87% suggesting there might have been some overfitting going on. The FinalModel ipynb has just the final model in it that I used with the flask app. I played around with it, and it seems fairly accurate with more generalized reviews of products, not just from IMBD reviews. I doubt anyone wants to try this out briefly, theres not much to do, and as stated previously it's mainly for learning purposes. If you do though, you can:

1. git clone https://github.com/sulk0o/MLPROJECT_Sentiment_Analysis_WebApp.git
2. cd MLPROJECT_Sentiment_Analysis_WebApp
3. pip install -r requirements.txt
4. python app.py
5. Visit http://127.0.0.1:5000/
6. Profit.
