from flask import Flask

app = Flask(__name__)

employees = []

@app.route("/")
def home():
    return "Welcome to Employee Management Portal"

@app.route("/register/<name>")
def register(name):
    employees.append(name)
    return f"Employee {name} registered successfully"

@app.route("/search/<name>")
def search(name):
    if name in employees:
        return f"Employee {name} found"
    return "Employee not found"

if __name__ == "__main__":
    app.run(debug=True)