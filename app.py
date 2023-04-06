from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return {"message": "The SoulForge is up and running"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
