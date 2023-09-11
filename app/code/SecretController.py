from flask import Flask, make_response, render_template, url_for, request, redirect
from werkzeug.middleware.proxy_fix import ProxyFix
import code.SecretRepo as repo

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1)

@app.route('/')
def EnterSecret():
    return render_template(
        'enter-secret.html',
        save_secret_url=url_for('SaveSecret'),
        title='Secret sharing - enter your secret')

@app.route('/save', methods = ['POST'])
def SaveSecret():
    (id, key) = repo.Store(request.form['secret'])
    return redirect(
        url_for(
            'ConfirmSecretSaved', 
            secretId = id,
            secretKey = key))

@app.route('/saved/<uuid:secretId>/<secretKey>')
def ConfirmSecretSaved(secretId, secretKey):
    return render_template(
        'confirm_secret_saved.html',
        secret_url = url_for(
            'ConfirmViewSecret',
            secretId = secretId,
            secretKey = secretKey,
            _external = True))

@app.route('/confirmview/secret/<uuid:secretId>/<secretKey>')
def ConfirmViewSecret(secretId, secretKey):
    if (repo.SecretExists(secretId)):
        return render_template(
            'confirm_view_secret.html',
             secret_url = url_for(
                'ViewSecret',
                secretId = secretId,
                secretKey = secretKey,
                _external = True))
    return render_template(
        'no_such_secret.html',
        url_for_new_secret=url_for('EnterSecret'))

@app.route('/view/secret/<uuid:secretId>/<secretKey>')
def ViewSecret(secretId, secretKey):
    if (repo.SecretExists(secretId)):
        return render_template(
            'view_secret.html',
            secret=repo.Retrieve(secretId, secretKey))
    return render_template(
        'no_such_secret.html',
        url_for_new_secret=url_for('EnterSecret'))

