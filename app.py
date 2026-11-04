from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Employee Management Portal"

if __name__ == "__main__":
    app.run(debug=True)
employees = []

@app.route("/register/<name>")
def register(name):
    employees.append(name)
    return f"Employee {name} registered successfully"