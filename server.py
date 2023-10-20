from flask import Flask, render_template

from jinja2 import StrictUndefined
app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def index():
    return render_template("index.html", title="")


@app.route("/base")
def layout():
    return render_template("base.html", title="")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
