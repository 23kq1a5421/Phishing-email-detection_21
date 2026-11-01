
from flask import Flask, render_template, request
from detector import analyze_email

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        sender = request.form.get("sender", "")
        subject = request.form.get("subject", "")
        message = request.form.get("message", "")

        result = analyze_email(sender, subject, message)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
