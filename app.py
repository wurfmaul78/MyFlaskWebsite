from flask import Flask, url_for, render_template
from markupsafe import escape
from ags import bykey,byplace

app = Flask (__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/place/<place>")
def agsplace(place):
    try:
        return(byplace(place))
    except:
        return f"Not possible! Your place {place} not exists or is wrong written. Please try again :-)"

@app.route("/ags/<ags>")
def agskey(ags):
    try:
        return(bykey(ags))
    except:
        return f"Not possible! <b>{escape(ags)}</b> is not type integer."

if "__name__"  == "__main__":
    app.run()
