from flask import Flask, request

app = Flask(__name__)

feedback_list = []

@app.route("/", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        user_feedback = request.form.get("feedback")
        if user_feedback:
            feedback_list.append(user_feedback)
            return f"Thanks for your feedback!<br><br>All Feedbacks:<br>{'<br>'.join(feedback_list)}"
        else:
            return "Please enter some feedback."

    return '''
    <form method="POST">
        Enter your feedback: <input type="text" name="feedback">
        <input type="submit" value="Submit">
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
