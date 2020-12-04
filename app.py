from flask import Flask, render_template, Response, request, jsonify, url_for
from random import randint
from datetime import datetime
import os.path
from os import path

app = Flask(__name__)

# Google Sheets API Setup
import gspread
from oauth2client.service_account import ServiceAccountCredentials

if path.exists("static/credentials.json"):
    # This won't work unless you have valid credentials file
    credential = ServiceAccountCredentials.from_json_keyfile_name("static/credentials.json", ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"])
    client = gspread.authorize(credential)
    gsheet = client.open("Healthcare Form Log").sheet1

@app.route('/')
def index():
    return(render_template("index.html", toggle_help=False))

@app.route('/question1')
def question1():
    return(render_template("question1.html", toggle_help=True))

@app.route('/question2')
def question2():
    return(render_template("question2.html", toggle_help=True))

@app.route('/question3')
def question3():
    return(render_template("question3.html", toggle_help=True))

@app.route('/question4')
def question4():
    return(render_template("question4.html", toggle_help=True))

@app.route('/question5')
def question5():
    return(render_template("question5.html", toggle_help=True))

@app.route('/question6')
def question6():
    return(render_template("question6.html", toggle_help=True))

@app.route('/question7')
def question7():
    return(render_template("question7.html", toggle_help=True))

@app.route('/review')
def review():
    return(render_template("review.html", toggle_help=True))

@app.route('/success')
def success():
    if path.exists("static/credentials.json"):
        # Converting to Google Sheets
        patient_id = randint(1000000, 9999999)
        patient_dt = datetime.now().strftime("%d/%m/%Y %I:%M:%S")
        row = [patient_id, patient_dt, 'John','Smith','01/01/1984','9485746325','500 Lexington Street, New York, New York, 10027', 'Y', 'Y']
        gsheet.insert_row(row,2)
    return(render_template("success.html", toggle_help=True))

@app.route('/dashboard')
def dashboard():
    data = {
        'ID' : '9485746325',
        'first_name' : 'John',
        'last_name' : 'Smith',
        'dob' : '01/01/1984',
        'ssn' : '9485746325',
        'address' : '500 Lexington Street',
        'working' : 'Yes',
        'health_problems' : 'Yes'
    }
    if path.exists("static/credentials.json"):
        row = gsheet.row_values(2)
        data['ID'] = row[0]
        data['first_name'] = row[2]
        data['last_name'] = row[3]
        data['dob'] = row[4]
        data['ssn'] = row[5]
        data['address'] = row[6]
        data['working'] = row[7]
        data['health_problems'] = row[8]
 
    return(render_template("dashboard.html", toggle_help=True, data=data))



if __name__ == '__main__':

    app.run(debug = True)