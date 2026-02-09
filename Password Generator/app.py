from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""

    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Please select at least one character type!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    if request.method == "POST":
        length = int(request.form.get("length"))
        letters = request.form.get("letters")
        numbers = request.form.get("numbers")
        symbols = request.form.get("symbols")

        password = generate_password(
            length,
            letters == "on",
            numbers == "on",
            symbols == "on"
        )

    return render_template("index.html", password=password)


if __name__ == "__main__":
    app.run(debug=True)
