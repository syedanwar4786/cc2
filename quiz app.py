from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def quiz():
    return """
        <h2>Simple Quiz App</h2>
        <form action="/result" method="post">
            <p>Q1: What is the capital of France?</p>
            <input type="radio" name="q1" value="Paris"> Paris<br>
            <input type="radio" name="q1" value="London"> London<br>
            <input type="radio" name="q1" value="Berlin"> Berlin<br>
            <input type="radio" name="q1" value="Rome"> Rome<br><br>

            <p>Q2: 2 + 2 = ?</p>
            <input type="radio" name="q2" value="3"> 3<br>
            <input type="radio" name="q2" value="4"> 4<br>
            <input type="radio" name="q2" value="5"> 5<br>
            <input type="radio" name="q2" value="6"> 6<br><br>

            <p>Q3: What is the color of the sky on a clear day?</p>
            <input type="radio" name="q3" value="Blue"> Blue<br>
            <input type="radio" name="q3" value="Green"> Green<br>
            <input type="radio" name="q3" value="Red"> Red<br>
            <input type="radio" name="q3" value="Yellow"> Yellow<br><br>

            <input type="submit" value="Submit">
        </form>
    """


@app.route("/result", methods=["POST"])
def result():
    q1 = request.form.get("q1")
    q2 = request.form.get("q2")
    q3 = request.form.get("q3")

    correct_answers = {"q1": "Paris", "q2": "4", "q3": "Blue"}
    score = 0

    if q1 == correct_answers["q1"]:
        score += 1
    if q2 == correct_answers["q2"]:
        score += 1
    if q3 == correct_answers["q3"]:
        score += 1

    return f"<h2>You scored {score} out of 3!</h2>"


if __name__ == "__main__":
    app.run(debug=True)