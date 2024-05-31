import os
import openai
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from logger import get_logger
from models.user_info import UserInfo
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
        # user_table.put_info(UserInfo.attach_random_id(company_name=company_name, ideal_user=ideal_user, product_name=product_name))

        #user_input = "My product is called " + product_name +". Write a PRD of a feature " + feature_name +"for my product. An overview for the feature is: " + overview
        get_logger("experiment").info(message_history)
        #gpt_resp = chat(user_input, message_history)
        #splitted_gpt_resp = gpt_resp.split('\n')
        #   print(splitted_gpt_resp)
        resp = jsonify({'tweets': get_tweets(company_name, product_name, ideal_user), 'posts': get_posts(company_name, product_name, ideal_user), 'blogs': get_blogs(company_name, product_name, ideal_user)})
        print(resp)
        #for i in splitted_gpt_resp:
            #resp = jsonify({'output': i})
        return resp
    return render_template('new.html')

#@app.route("/admin")
# def card_view():
#     get_logger("card_view").info("card_view()")
#     data = user_table.get_all_info()
#     return render_template('user_info.html', data=data)


#@app.route("/test")
def exeriment():
    get_logger("experiment").info("experiment()")
    return "works"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))


#Liftoff
#Generating tech startups
#students wanting to learn how to deploy side projects