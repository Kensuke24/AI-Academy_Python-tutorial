from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    message = "hello!"
    li = ["hello", "world"]
    dic = {"name":"AI Academy", "lang":"Python"}

    return render_template('index.html', message=message, li=li, dic=dic)


if __name__ == '__main__':
    app.run(port=12345, debug=False)
    # app.debug = True
    # app.run(host='0.0.0.0', port=8080)
