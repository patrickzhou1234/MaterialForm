from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def saveResult():
    name = request.form['name']
    email = request.form['email']
    f = open("people.txt", "a")
    f.write(name+" "+email+"\n")
    f.close()
    return render_template('index.html')

app.run(host='0.0.0.0', port=80)