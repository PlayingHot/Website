from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/recruitment", methods=["GET", "POST"])
def recruitment():
    return render_template("recruitment.html")

@app.route('/submit',methods=['POST'])
def submit():
    name = request.form['full-name']
    course = request.form['course']
    number = request.form['number']
    email = request.form['email']
    link = request.form['link']
    print(name,course,number,email,link)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
    