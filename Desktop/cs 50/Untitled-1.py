from flask import Flask, render_template, session, url_for, redirect
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    if "board" not in session:
        session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
        session["turn"] = "x"
        
    return render_template("index.html", index=session["board"], turn=session["turn"])

@app.route("/play/<int:i>/<int:j>")
def play(i, j):
    return f"Played a move at position ({i}, {j})"

if __name__ == "__main__":
    app.run(debug=True, port=5001)
