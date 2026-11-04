from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Employee Management Portal"

if __name__ == "__main__":
    app.run(debug=True)
@app.route("/search/<name>")
def search(name):
    if name in employees:
        return f"Employee {name} found"
    return "Employee not found"