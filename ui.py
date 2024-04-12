import openai
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from logger import get_logger
from models.chat import chat

load_dotenv()
print(load_dotenv())

message_history = []
def get_tweets(company_name, product_name, ideal_user):
    user_input = "Write the first 30 Tweets for my company" + company_name + "Our main product revolves around" + product_name + "and the ideal user is" + ideal_user + ". Rules: 1. No hashtags 2. Tweet 1-5 should be about the launch 3. Tweet 6-10 should be about the problem the product solves 4. Tweet 11-15 should be about how the product solves the problem 5. Tweet 16-20 should be about testimonials 6. Tweet 21-25 should be funny and engaging content 7. Tweet 26-30 should be about the roadmap of the company's product. Make sure you give each tweet in a new line."
    return chat(user_input, message_history)
def get_posts(company_name, product_name, ideal_user):
    user_input = "Write the first 10 Instagram posts for my company in the format 1. Caption 2. Slide 1 Content 3. Slide 2 Content" + company_name + "Our main product revolves around" + product_name + "and the ideal user is" + ideal_user + ". Make sure you give each post in a new line."
    return chat(user_input, message_history)

def get_blogs(company_name, product_name, ideal_user):
    user_input = "Write the first 10 blogs for my company" + company_name + "Our main product revolves around" + product_name + "and the ideal user is" + ideal_user + ". Make sure you give each blog in a new line."
    return chat(user_input, message_history)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        company_name = request.form['question1']
        product_name = request.form['question2']
        ideal_user = request.form['question3']
        get_logger("experiment").info(message_history)
        resp = jsonify({'tweets': get_tweets(company_name, product_name, ideal_user), 'posts': get_posts(company_name, product_name, ideal_user), 'blogs': get_blogs(company_name, product_name, ideal_user)})
        print(resp)
        return resp
    return render_template('index.html')

@app.route('/old', methods=['GET', 'POST'])
def home_old():
    return render_template('new.html')

if __name__ == '__main__':
    app.run(debug=True)