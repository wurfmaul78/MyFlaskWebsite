from flask import Flask, url_for, render_template,jsonify

from markupsafe import escape
from sources.ags import bykey,byplace

app = Flask (__name__)

@app.errorhandler(404)
def page_not_found(e):
    # https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/
    return render_template('sources/404.html'), 404


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/place/<place>", methods=['GET','POST'])
def agsplace(place):
    try:
        #return(byplace(place))
        return jsonify(byplace(place))
    except:
        return f"Not possible! Your place {place} not exists or is wrong written. Please try again :-)"

@app.route("/ags/<ags>", methods=['GET','POST'])
def agskey(ags):
    try:
        return (bykey(ags))
    except:
        return f"Not possible! <b>{escape(ags)}</b> is not type integer."

if __name__ == "__main__":
    app.run()
