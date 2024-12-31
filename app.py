from flask import Flask, render_template, request

# App declaration
app = Flask(__name__)

# BMI formula & calculation 
def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_category_and_image(bmi):
    """
    Returns the BMI category and corresponding image file name.
    """
    if bmi < 18.5:
        return "Underweight", "underweight.jpg"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight", "normal.jpg"
    elif 25 <= bmi < 29.9:
        return "Overweight", "overweight.jpg"
    else:
        return "Obesity", "obesity.jpg"

# Start an app route
@app.route("/")
def main():
    return render_template("index.html")


# Route for BMI calculation result
@app.route("/bmi", methods=["POST"])
def calculate():
        try:
            weight = float(request.form.get("weight"))
            height = float(request.form.get("height"))

            if weight > 1 or height > 1:
                bmi = calculate_bmi(weight, height)
                category, image = bmi_category_and_image(bmi)
                
                return render_template(
                "index.html", 
                bmi=f"{bmi:.2f}", 
                category=category, 
                image=image, 
                bmi_percentage=min(bmi / 40 * 100, 100)  # Scale BMI to percentage for meter
            )
               
            else:
                error = "Weight and height must be positive numbers."
                return render_template("index.html", error=error)
          
        except ValueError:
            error = "Weight and height must be positive numbers."
            return render_template("index.html", error=error)

if __name__ == "__main__":
    app.run(debug=True)
