import os
from time import sleep
from flask import Flask, render_template, request, jsonify
from logger import get_logger
from models.chat import chat

# message_history = []
def get_tweets(company_name, product_name, ideal_user):
    user_input = f"Write the first 30 Tweets for my company {company_name}. Our main product revolves around {product_name} and the ideal user is {ideal_user}. Rules: 1. No hashtags 2. Tweet 1-5 should be about the launch 3. Tweet 6-10 should be about the problem the product solves 4. Tweet 11-15 should be about how the product solves the problem 5. Tweet 16-20 should be about testimonials 6. Tweet 21-25 should be funny and engaging content 7. Tweet 26-30 should be about the roadmap of the company's product. Format the tweets in markdown numbered list and use emojis. Dont write anything before or after the list"
    return chat(user_input)

def get_posts(company_name, product_name, ideal_user):
    user_input = f"Write the first 10 Instagram posts for my company in the format 1. Caption 2. Slide 1 Content 3. Slide 2 Content {company_name} Our main product revolves around {product_name} and the ideal user is {ideal_user}. Format the posts in markdown numbered list and use emojis. Dont write anything before or after the list"
    return chat(user_input)

def get_blogs(company_name, product_name, ideal_user):
    user_input = f"Write the first 10 blogs for my company {company_name} Our main product revolves around {product_name} and the ideal user is {ideal_user}. Format the tweets in markdown numbered list and use emojis. Dont write anything before or after the list"
    return chat(user_input)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    # if request.method == 'POST':
    #     company_name = request.form['question1']
    #     product_name = request.form['question2']
    #     ideal_user = request.form['question3']

    #     user_table.put_info(UserInfo.attach_random_id(company_name=company_name, ideal_user=ideal_user, product_name=product_name))
    #     user_input = "My product is called " + product_name +". Write a PRD of a feature " + feature_name +"for my product. An overview for the feature is: " + overview
    #     get_logger("experiment").info(message_history)
    #     gpt_resp = chat(user_input, message_history)
    #     splitted_gpt_resp = gpt_resp.split('\n')
    #     print(splitted_gpt_resp)
    return render_template('index.html')

#@app.route("/admin")
# def card_view():
#     get_logger("card_view").info("card_view()")
#     data = user_table.get_all_info()
#     return render_template('user_info.html', data=data)


# @app.route("/test")
# def exeriment():
#     get_logger("experiment").info("experiment()")
#     return "works"


@app.route('/tweets', methods=['POST'])
def getTweets():
    company_name = request.form['question1']
    product_name = request.form['question2']
    ideal_user = request.form['question3']
    tweets = get_tweets(company_name, product_name, ideal_user)
    return tweets

@app.route('/posts', methods=['POST'])
def getPosts():
    company_name = request.form['question1']
    product_name = request.form['question2']
    ideal_user = request.form['question3']
    posts = get_posts(company_name, product_name, ideal_user)
    return posts

@app.route('/blogs', methods=['POST'])
def getBlogs():
    company_name = request.form['question1']
    product_name = request.form['question2']
    ideal_user = request.form['question3']
    blogs = get_blogs(company_name, product_name, ideal_user)
    return blogs


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))


#Liftoff
#Generating tech startups
#students wanting to learn how to deploy side projects