from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Declare the app
app = Flask(__name__)


def cal_bmi(weight, height):
    return weight / ((height /100) ** 2)

def category(cal_bmi):
    """
    Returns the BMI category
    """
    if cal_bmi < 18.5:
        return "Underweight"
    elif 18.5 <= cal_bmi < 24.9:
        return "Normal weight"
    elif 25 <= cal_bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"


# Start an app route
@app.route("/")
def main():
    return render_template("index.html")

# Route for BMI calculation result
@app.route("/bmi", methods=["GET", "POST"])


def calculate():
    if request.method == "POST":

        try:
            weight = float(request.form.get("weight"))
            height = float(request.form.get("height"))

            if weight <= 0 or height <= 0:
                error = "Weight and height must be positive values."
                return render_template("index.html", error=error)

            bmi = cal_bmi(weight, height)
    

            return render_template(
                "index.html",
                bmi=f"{bmi:.2f}",
                category=category(bmi),
                progress_percentage=min(bmi / 40 * 100, 100)  # Scale BMI to percentage for meter
            )

        except ValueError:
            error = "Invalid input. Please enter numeric values for weight and height."
            return render_template("index.html", error=error)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
