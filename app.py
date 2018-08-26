#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, url_for, redirect
import random as rnd
import model

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["GET", "POST"])
def result():
    if request.method == "POST":
        my_name = request.form["name"]
        message = "これが「{}」の診断結果じゃ。ちなみにワシの精力は690じゃぞ。".format(my_name)
        result = model.diagnotic(len(my_name))
        type_name, labels, character = model.detail_diagnostic(len(my_name))

        return render_template("result.html", message = message, result = result, 
                                type_name = type_name, labels = labels, character = character)

    else:
        return redirect(url_for("index"))
   
if __name__== "__main__":
    app.run(debug = True)
    
