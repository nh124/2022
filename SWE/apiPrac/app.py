import flask
from nyt import articalSearch

app = flask.Flask(__name__)

@app.route("/", methods=("GET", "POST"))
quary = ""
def index():
    if flask.request.method == "POST":
        quary = flask.request.form.get("quary")
    else:
        quary = "Apple"
    headlines, snippets = articalSearch(quary)
    return flask.render_template(
        "index.html",
        num_articles=len(headlines),
        headlines=headlines,
        snippets=snippets,
    )
    return "Hello, world!"

app.run()
