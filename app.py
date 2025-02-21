from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    result = None  # Variable para almacenar el resultado
    if request.method == "POST":
        try:
            num1 = float(request.form.get("num1", 0))
            num2 = float(request.form.get("num2", 0))
            operator = request.form.get("operator")
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = num1 / num2 if num2 != 0 else "Error: División por cero"
            else:
                result = "Operador no válido"
        except ValueError:
            result = "Entrada no válida"
    return render_template("index.html", result=result)
