from flask import Flask, render_template, request

app = Flask(__name__)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

@app.route("/", methods=["GET", "POST"])
def index():
    bmi = None
    category = None
    error = None

    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height = float(request.form["height"])

            if weight <= 0 or height <= 0:
                error = "Weight and height must be positive numbers."
            else:
                bmi = round(weight / (height ** 2), 2)
                category = bmi_category(bmi)

        except ValueError:
            error = "Please enter valid numbers."

    return render_template("index.html", bmi=bmi, category=category, error=error)

if __name__ == "__main__":
    app.run(debug=True)
