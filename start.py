from flask import Flask
from markupsafe import escape

app = Flask (__name__)

@app.route("/")
def home():
    return "<h1>Welcome on Gerhard Posch&#39;s Website</h1><p>This is where</p>"

@app.route("/name/<ags>")
def agskey(ags):
    if ags == "Gerhard":
        return f"Guten Tag Eure Koenigliche Hoheit, {escape(ags)}"
    else:
        return f"Guten Tag, {escape(ags)}"

if "__name__"  == "__main__":
    app.run()
