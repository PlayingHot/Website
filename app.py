from flask import Flask, render_template, request, redirect
import smtplib
import ssl
from email.message import EmailMessage
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

app = Flask(__name__)

scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
    ]
file_name = 'client_key.json'
creds = ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)
client = gspread.authorize(creds)

sheet = client.open('ACM_EXECS').sheet1

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
    row = [name, course, number, email, link, department1, department2, department3]
    sheet.append_row(row)
    lis=[email]
    cont='ACM Test2'
    gmail(lis,cont)
    return redirect('/')

def gmail(email_list, content):
    email_sender = 'dhruvpython10@gmail.com'
    email_password = 'wqtugdosslilokwg'

    subject = 'Test'
    body = content
    context = ssl.create_default_context()

    em = EmailMessage()
    em['From'] = email_sender
    em['Subject'] = subject
    em.set_content(body)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        for email in  email_list:
            em['To'] = email
            smtp.sendmail(email_sender, email, em.as_string())
            del em['To']
    return None


if __name__ == "__main__":
    app.run(debug=True)