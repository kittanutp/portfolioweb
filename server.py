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
    with open('/home/MaxPongji/portfolioweb/database.csv', mode='a', newline='\n') as csvfile:
        name = data['name']
        email = data['email']
        subject = data['subject']
        messages = data['message']
        csvwriter = csv.writer(csvfile, delimiter=',',
                               quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([name, email, subject, messages])
        return 'finish'
