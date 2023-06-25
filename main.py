from flask import Flask, render_template, request, jsonify, send_file
import io
from flask_cors import CORS

from booksnake import DEFAULT_SEARCHERS, Book, LibgenBook, GutenbergBook

APP = Flask(__name__)
CORS(APP)

BOOK_CONSTRUCTORS = {"LibgenBook": LibgenBook, "GutenbergBook": GutenbergBook}


@APP.route("/")
def index():
    return render_template("index.html")


@APP.route("/api/search", methods=["POST"])
def api_search():
    query_text = request.json["query"]
    results = []
    for searcher, _ in DEFAULT_SEARCHERS:
        try:
            results.extend(searcher().search(query_text))
        except Exception as e:
            print(f"Error in {searcher}: {e}")
    return jsonify({"results": [r.to_dict() for r in results]})


@APP.route("/api/download", methods=["POST"])
def api_download():
    print(request.json)
    data = request.json["data"]

    print(data)
    try:
        book: Book = BOOK_CONSTRUCTORS[data["type"]].from_dict(data)
    except:
        return jsonify({"error": "Could not parse type " + data["type"]}), 500

    try:
        book_file = book.download()
    except:
        return jsonify({"error": "Could not download book " + data["title"]}), 500

    fname = data["title"].replace(" ", "-") + "." + data["ext"]
    res = send_file(io.BytesIO(book_file), as_attachment=True, download_name=fname)
    res.headers["x-suggested-filename"] = fname
    return res


if __name__ == "__main__":
    APP.run(host="0.0.0.0", debug=True, port=5020)
