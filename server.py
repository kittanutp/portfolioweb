from email import message
from lib2to3.pgen2.token import NEWLINE
from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contact_me', methods=['POST', 'GET'])
def contact_me():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_database(data)
        return redirect('/')


def write_database(data):
    with open('./database.csv', mode='a', newline='\n') as csvfile:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csvwriter = csv.writer(csvfile, delimiter=',',
                               quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([name, email, subject, message])
        return 'finish'
