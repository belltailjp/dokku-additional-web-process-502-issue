import flask


app = flask.Flask(__name__)


@app.route('/')
def index():
    return "Love, Dokku!! This is another web process."


if __name__ == '__main__':
    app.run(debug=True)
