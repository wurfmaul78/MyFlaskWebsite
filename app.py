from flask import Flask, url_for, render_template
from markupsafe import escape

app = Flask (__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/name/<ags>")
def agskey(ags):
    if ags == "Gerhard":
        return f"Guten Tag Eure Koenigliche Hoheit, {escape(ags)}"
    else:
        return f"Guten Tag, {escape(ags)}"

if "__name__"  == "__main__":
    app.run()
