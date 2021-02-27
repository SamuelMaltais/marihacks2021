from os import environ
from flask import Flask, render_template
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SPREADSHEET_ID = '1to8XkoienC-2ITXDZUMfnC3p_mLUwUAU-_d3CKSk-00'
RANGE_NAME = 'Tabellenblatt1'


app = Flask(__name__)

@app.route("/")
def home():
    print("something went right")
    return "lmao !"

@app.route("/getfoodbanks")
def getfoodbanks():
    return response
@app.route("/oath2callback")
def callback():
    return "200"

def getspreadsheetinfo():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,range=RANGE_NAME).execute()
    values = result.get('values', [])
    return values

app.run(environ.get('PORT'))