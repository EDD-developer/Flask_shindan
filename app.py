#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 14:13:36 2018

@author: rte28
"""

from flask import Flask, request, render_template, url_for, redirect
import random as rnd

app = Flask(__name__)

@app.route("/")
def index():
    title = "エロ診断メーカー"
    message = "名前を入力するのじゃ"
    
    return render_template("index.html", title = title, message = message)

@app.route("/result", methods=['GET', 'POST'])
def result():
    
    if request.method == 'POST':
        title = "診断結果"      
        my_name = request.form["name"]
        message = "これが{}の診断結果じゃ。ちなみにワシゃ500くらい。".format(my_name)
        
        results = ["貴様の精力は9000000000000じゃと!?    ...まじぱねえっす。",
                   "貴様の精力は-5353535353535353。赤マムシでも飲んで出直すんじゃな。",
                   "貴様の精力は530。ワシといい勝負じゃな。フォッフォッフォ。"]
                
        my_result = rnd.choice(results)

        return render_template("index.html", title = title, message = message, result = my_result)    
 
    else:
        # エラーなどでリダイレクトしたい場合はこんな感じで
        return redirect(url_for('index'))




if __name__== '__main__':
    app.run(debug = True)
    
