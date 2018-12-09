# RUN THIS FILE IN TERMINAL USING python and file name to open the local host,
# then open the the web address given in your browser
import json, requests, urllib2
from flask import Flask, render_template
from random import randint

app = Flask(__name__)

# Links API and reads count from api
url = 'https://api.case.law/v1/cases/'
law_case = urllib2.urlopen(url)
wjson = law_case.read()
wjdata = json.loads(wjson)

# creates variable count that can be passed further to html as a var
# generates random number in interval 0 to 99 and passes it to select the
# relevant case
random_case_number = randint(0, 99)
api_id = wjdata['results'][random_case_number]['id']
# api_url = wjdata['results'][random_case_number]['url']'['/?full_case=true&format=html']
api_name = wjdata['results'][random_case_number]['name']
api_url = 'https://api.case.law/v1/cases/{}/?full_case=true&format=html'.format(api_id)
api_decision_date = wjdata['results'][random_case_number]['decision_date']

# Returns index.html when goes to the main page or homepage
@app.route("/")
@app.route("/home")
def home():
    #passes count as variable in index.html
    return render_template('index.html', title="Home Page", id = api_id, url = api_url, name = api_name,
    decision_date= api_decision_date)

@app.route("/about")
def about():
    return render_template('about.html', title="About Page")

@app.route("/random")
def random():
    return render_template('random.html', title="Randomly Generated Case")

# allows to run it on local host without exporting FLASK_APP environment vars
# and refresh without restarting server
if __name__ == '__main__':
    app.run(debug=True)
