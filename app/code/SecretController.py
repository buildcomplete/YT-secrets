from flask import Flask, make_response, render_template, url_for, request, redirect
import code.SecretRepo as repo

app = Flask(__name__)

@app.route('/')
def EnterSecret():
    return render_template(
        'enter-secret.html',
        save_secret_url=url_for('SaveSecret'),
        title='Secret sharing - enter your secret')

@app.route('/save', methods = ['POST'])
def SaveSecret():
    return redirect(
        url_for(
            'ConfirmSecretSaved', 
            secretId = repo.Store(request.form['secret'])))

@app.route('/saved/<uuid:secretId>')
def ConfirmSecretSaved(secretId):
    return render_template(
        'confirm_secret_saved.html',
        secret_url = url_for(
            'ViewSecret',
            secretId = secretId,
            _external = True))

@app.route('/view/secret/<uuid:secretId>')
def ViewSecret(secretId):
    if (repo.SecretExists(secretId)):
        return render_template(
            'view_secret.html',
            secret=repo.Retrieve(secretId))
    return render_template(
        'no_such_secret.html',
        url_for_new_secret=url_for('EnterSecret'))

