# import the functions from model_pipeline.py here that are needed to perform the prediction task
from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        "author": "Corey Schafer",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "April 20, 2018",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "April 21, 2018",
    },
]

# create one endpoint that will take in a text input and predicts the classification output


@app.route("/")
@app.route("/")
def Home():
    return render_template("Home.html", posts=posts)


@app.route("/about")
def About():
    return render_template("About.html", title="Test About")


if __name__ == "__main__":
    app.run(debug=True)
