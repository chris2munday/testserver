from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def ind():
    return render_template('index.html')

@app.route('/<string:page_name>')
def index(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return render_template('/thankyou.html', name=data['email'].split("@")[0])
        except:
            return 'did not save to Database'
    else:
        return 'something went wrong'

def write_file(data):
    with open('database.txt', mode='a') as f:
        print (data)
        email = data['email']
        subject = data['subject']
        message = data['message']
        f.write (f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as f2:
        print (data)
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(f2, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])