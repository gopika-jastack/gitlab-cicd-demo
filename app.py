from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "GitLab CI/CD Pipeline Success"

if __name__ == "__main__":
    app.run()
