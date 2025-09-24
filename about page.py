from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Home Page! Go to /about to see details."

@app.route("/about")
def about():
    return """
    About Page
    -----------------
    My name is Syed Anwar
    Reg no: RA2432014010011
    M.Sc Applied Data Science
    """

if __name__ == "__main__":
    app.run(debug=True)
