from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('new.html')

@app.route('/reno', methods=['GET', 'POST'])
def home_reno():
    return render_template('index.html')

@app.route("/admin")
def card_view():
    return render_template('user_info.html', data={})


if __name__ == '__main__':
    app.run(debug=True)