from flask import Flask, url_for, render_template
from markupsafe import escape

app = Flask (__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ags/<ags>")
def agskey(ags):
    try:
        ags = (int(ags))
        return f"Ja, ein Integer {escape(ags)}"
    except:
        return f"Not possible! <b>{escape(ags)}</b> is not type integer."

if "__name__"  == "__main__":
    app.run()
