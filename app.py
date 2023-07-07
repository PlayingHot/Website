from flask import Flask, render_template, request, redirect

app = Flask(__name__)


DEPARTMENTS = [
    "Techincals",
    "Creavtives",
    "Marketing",
    "Logistics",
    "RnD",
    "SME",
    "Photography",
    "PR",
]
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/recruitment", methods=["GET", "POST"])
def recruitment():
    return render_template("recruitment.html", departments = DEPARTMENTS)

@app.route('/submit',methods=['POST'])
def submit():
    name = request.form['full-name']
    course = request.form['course']
    number = request.form['number']
    email = request.form['email']
    link = request.form['link']
    department1 = request.form.get('Department1')
    department2 = request.form.get('Department2')
    department3 = request.form.get('Department3')
    print(name,course,number,email,link, department1, department2, department3)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
    