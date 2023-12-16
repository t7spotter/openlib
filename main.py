import requests
from flask import Flask
from icecream import ic
import http


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/title/<title>")
def title(title):
    parsed = title.replace("%20", "+")
    response = requests.get(
        f"https://openlibrary.org/search.json?title={parsed}"
    ).json()
    b = []
    for i in response["docs"]:
        b.append(i)

    result = []
    for ii in b:
        info = {
            "1 title": ii.get("title", ""),
            "2 author": ii.get("author_name", ""),
            "3 author_id": ii.get("author_key", ""),
            "4 publisher": ii.get("publisher", ""),
            "5 publish year": ii.get("publish_year", ""),
            "6 ISBN": ii.get("isbn", ""),
        }
        result.append(info)

    return result


if __name__ == "__main__":
    app.run(debug=True)
