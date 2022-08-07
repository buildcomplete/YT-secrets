from flask import Flask, make_response, render_template, url_for, request, redirect
import code.SecretRepo as repo

app = Flask(__name__)

@app.route('/')
def EnterSecret():
    return render_template(
        'enter-secret.html')

@app.route('/save')
def SaveSecret():
    return "world"