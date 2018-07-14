#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 14:13:36 2018

@author: rte28
"""

from flask import Flask, request, render_template, url_for, redirect
import random as rnd
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    message = "名前を入力するのじゃ"
    return render_template("index.html", message = message)

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        my_name = request.form['name']
        message = 'これが{}の診断結果じゃ。ちなみにワシゃ500くらい。'.format(my_name)
        
        results = ["貴様の精力は9000000000000じゃと!? 参った...",
                   "貴様の精力は-5353535353535353。赤マムシでも飲んで出直すんじゃな。",
                   "貴様の精力は530。ワシといい勝負じゃな。フォッフォッフォ。"]
                
        my_result = rnd.choice(results)

        return render_template('result.html', message = message, result = my_result)    
 
    else:
        return redirect(url_for('index'))

@app.route('/manual')
def manual():
    return render_template('manual.html')
    
@app.route('/about_us')
def about_us():
    return render_template('about_us.html') 

@app.route('/blog')
def blog():
    return render_template('blog.html')

if __name__== '__main__':
    app.run(debug = True)
    
