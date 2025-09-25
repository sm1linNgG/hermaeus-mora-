from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['post', 'get'])
def integer():
    mesage = ""
    if request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('password')
        mesage = mesage + user + ' ' + password
        return render_template('proba.html', mesage='mesage')

    return render_template('proba.html', mesage='mesage')


if __name__ == '__main__':
    print("run server")
    app.run()
