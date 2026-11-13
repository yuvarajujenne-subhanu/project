
from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Different excuses for different situations
excuses = {
    "Late to class": [
        "My alarm clock and I had a disagreement! 😂",
        "A traffic jam formed behind a confused cow! 🐄",
        "I was helping my neighbor find their slippers! 🤣",
        "My bed refused to let me go! 😴"
    ],

    "Homework not completed": [
        "My notebook needed a vacation! 📚",
        "My pen ran out of motivation! ✍️",
        "My homework disappeared mysteriously! 🪄",
        "I was waiting for inspiration to arrive! 😂"
    ],

    "Missed an exam": [
        "My alarm clock decided to take a holiday! 😴",
        "I was stuck in a very long dream! 😂",
        "My calendar forgot to remind me! 📅",
        "My pillow won the battle this morning! 🤣"
    ],

    "Didn't attend meeting": [
        "My Wi-Fi went on a world tour! 🌍",
        "My laptop needed emotional support! 💻",
        "I accidentally entered a time-travel experiment! 🕰️",
        "My internet connection was playing hide and seek! 😂"
    ]
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    situation = request.form.get("situation")

    if situation not in excuses:
        return render_template(
            "index.html",
            error="Please select a valid situation!"
        )

    excuse = random.choice(excuses[situation])

    return render_template(
        "index.html",
        situation=situation,
        excuse=excuse
    )


if __name__ == "__main__":
    app.run(debug=True)
