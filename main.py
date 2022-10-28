
import flask

app = flask.Flask("blog-theme")
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def forward_slash():
    return flask.render_template("index.html")

@app.route("/<path:filepath>.html")
def landing_page(filepath):
    return flask.render_template(f"{filepath}.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
