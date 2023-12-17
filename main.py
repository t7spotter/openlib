import requests
from flask import Flask, jsonify, request
from icecream import ic
import http


app = Flask(__name__)

domain = "http://127.0.0.1:5000"


@app.route("/ok")
def hello():
    return "Hello World!"


@app.route("/title/<title>")
def title(title):
    parsed = title.replace("%20", "+")
    url = f"https://openlibrary.org/search.json?title={parsed}"
    response = requests.get(url).json()

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


@app.route("/author/<author_id>")
def author(author_id):
    url = f"https://openlibrary.org/authors/{author_id}.json"
    response = requests.get(url).json()
    result = {
        "1 name": response.get("name", ""),
        "2 birth date": response.get("birth_date", ""),
        "3 bio": response.get("bio", ""),
        "4 wikipedia": response.get("wikipedia", ""),
    }
    return result


@app.route("/works/<path:next>")
def works(next):
    try:
        offset = request.args.get("offset", 0)

        url = f"https://openlibrary.org/{next}?offset={offset}"

        response = requests.get(url).json()
        works = response["entries"]

        content = []
        for i in works:
            info = {
                "1 title": i.get("title", ""),
                "2 description": i.get("description", ""),
                "3 key": i.get("key", ""),
            }

            content.append(info)

        # region links
        links = response.get("links", [])
        links_dict = {
            "self": links.get("self", ""),
            "next": links.get("next", ""),
            "prev": links.get("prev", ""),
        }

        next_with_localhost = f"{domain}/works{links_dict['next']}"
        prev_with_localhost = f"{domain}/works{links_dict['prev']}"
        self_with_localhost = f"{domain}/works{links_dict['self']}"

        if links_dict["prev"] == "":
            prev_with_localhost = ""

        if links_dict["next"] == "":
            next_with_localhost = ""

        if links_dict["self"] == "":
            self_with_localhost = ""
        # endregion links

        result = {
            "1 links": {
                "1 next": next_with_localhost,
                "2 prev": prev_with_localhost,
                "3 self": self_with_localhost,
            },
            "2 works": content,
        }
        # response.raise_for_status()

        return result
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


@app.route("/authorworks/<author_id>")
def author_works(author_id):
    url = f"https://openlibrary.org/authors/{author_id}/works.json"
    response = requests.get(url).json()
    works = response["entries"]

    content = []
    for i in works:
        info = {
            "1 title": i.get("title", ""),
            "2 description": i.get("description", ""),
            "3 key": i.get("key", ""),
        }

        content.append(info)

    # region links
    links = dict(response.get("links", []))
    links_dict = {
        "self": links.get("self", ""),
        "next": links.get("next", ""),
        "prev": links.get("prev", ""),
    }

    next_with_localhost = f"{domain}/works{links_dict['next']}"
    prev_with_localhost = f"{domain}/works{links_dict['prev']}"
    self_with_localhost = f"{domain}/works{links_dict['self']}"

    if links_dict["prev"] == "":
        prev_with_localhost = ""

    if links_dict["next"] == "":
        next_with_localhost = ""
    # endregion links

    result = {
        "1 links": {
            "1 next": next_with_localhost,
            "2 prev": prev_with_localhost,
            "3 self": self_with_localhost,
        },
        "2 works": content,
    }

    return result



@app.route("/isbn/<isbn>")
def isbn(isbn):
    url = f"https://openlibrary.org/isbn/{isbn}.json"
    response = requests.get(url).json()
    return response


if __name__ == "__main__":
    app.run(debug=True)
