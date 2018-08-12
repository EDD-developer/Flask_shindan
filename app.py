#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, url_for, redirect
import random as rnd
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["GET", "POST"])
def result():
    if request.method == "POST":
        my_name = request.form["name"]
        message = "これが{}の診断結果じゃ。ちなみにワシゃ500くらい。".format(my_name)
        
        results = ["貴様の精力は9000000000000じゃと!? 参った...",
                   "貴様の精力は-5353535353535353。赤マムシでも飲んで出直すんじゃな。",
                   "貴様の精力は530。ワシといい勝負じゃな。フォッフォッフォ。"]
                
        my_result = rnd.choice(results)

        return render_template("result.html", message = message, result = my_result)    
 
    else:
        return redirect(url_for("index"))
   
if __name__== "__main__":
    app.run(debug = True)
    
