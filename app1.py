import flask


app = flask.Flask(__name__)


@app.route('/')
def index():
    return "Hello, Dokku!! This is the primary web process."


if __name__ == '__main__':
    app.run(debug=True)
