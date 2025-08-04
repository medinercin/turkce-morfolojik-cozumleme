from flask import Flask, render_template, request
from analyzer.analyzer_core import analyze_sentence

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = []
    sentence = ""
    if request.method == "POST":
        sentence = request.form["sentence"]
        result = analyze_sentence(sentence)
    return render_template("index.html", result=result, sentence=sentence)

if __name__ == "__main__":
    app.run(debug=True)
