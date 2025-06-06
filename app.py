# app.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# A sample database of New York museums
museums = {
    "Metropolitan Museum of Art": "Metropolitan Museum of Art",
    "Museum of Modern Art": "Museum of Modern Art",
    "American Museum of Natural History": "American Museum of Natural History",
    "Whitney Museum of American Art": "Whitney Museum of American Art",
    "Brooklyn Museum": "Brooklyn Museum",
    "The Frick Collection": "Frick Collection",
    "The Morgan Library & Museum": "Morgan Library & Museum",
    "New York Transit Museum": "New York Transit Museum",
    "Queens Museum": "Queens Museum",
    "New Museum": "New Museum (New York City)",
    "The Strong National Museum of Play": "The Strong National Museum of Play",
    "National Baseball Hall of Fame and Museum": "National Baseball Hall of Fame and Museum",
    "Corning Museum of Glass": "Corning Museum of Glass",
    "Albany Institute of History & Art": "Albany Institute of History and Art",
    "Everson Museum of Art": "Everson Museum of Art"
}

WIKI_API_URL = "https://en.wikipedia.org/api/rest_v1/page/summary/"

def get_landmark_summary(title):
    response = requests.get(WIKI_API_URL + title)
    if response.status_code == 200:
        data = response.json()
        return {
            'title': data.get('title'),
            'extract': data.get('extract'),
            'thumbnail': data.get('thumbnail', {}).get('source'),
            'url': data.get('content_urls', {}).get('desktop', {}).get('page')
        }
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    info = None
    if request.method == 'POST':
        selected = request.form['museum']
        wiki_title = museums.get(selected)
        info = get_landmark_summary(wiki_title)
    return render_template('index.html', museums=museums, info=info)

if __name__ == '__main__':
    app.run(debug=True)
