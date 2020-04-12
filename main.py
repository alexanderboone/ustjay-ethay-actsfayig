import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()

def get_url(fact):
    request_url_form = 'https://hidden-journey-62459.herokuapp.com/piglatinize/'
    form_key = 'input_text'
    response = requests.post(request_url_form, data={form_key:fact}, allow_redirects=False)
    location_url = response.headers['Location']
    return location_url

@app.route('/')
def home():
    fact = get_fact()
    location_url = get_url(fact)
    return location_url


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

