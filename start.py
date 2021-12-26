from flask import Flask
from markupsafe import escape

app = Flask (__name__)

@app.route("/")
def home():
    return "Hello world"

if "__name__"  == "__main__":
    app.run()
