import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_SECRET")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        
        response = openai.Completion.create(
            api_key= os.getenv("OPENAI_SECRET"),
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=1.0,
            stop=None,
            max_tokens=1024
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("/templates/index.html", result=result)


def generate_prompt(animal):
    return animal
    
