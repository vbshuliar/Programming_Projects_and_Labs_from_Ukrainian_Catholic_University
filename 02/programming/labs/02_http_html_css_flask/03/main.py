"""Twitter followings map generator."""
from map_generator import generate_map, parse_json
from twitter2 import friends
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def main():
    """The main function."""
    if request.method == 'POST':
        name = request.form['username']
        return redirect(url_for("user_map", user=name))
    return render_template("home.html")


@app.route("/<user>")
def user_map(user):
    """Generates final map."""
    friends(user)
    user_map = generate_map(parse_json())
    return user_map


if __name__ == "__main__":
    app.run()
