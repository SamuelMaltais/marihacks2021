from os import environ
from flask import Flask, render_template, send_file, send_from_directory
import pickle
import os.path
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import requests
import googlemaps
from apscheduler.schedulers.blocking import BlockingScheduler
from flask_sqlalchemy import SQLAlchemy
import uuid
import threading
import time
import schedule 


#authentication with google API
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
#authentication for maps
client = gspread.authorize(creds)
gmaps_key = googlemaps.Client(key = "AIzaSyA_ojPMG7H6WxeUH_nwv6xLrTF_QVVQNN0")
#Flask app
app = Flask(__name__)
#SQL database for all the foodbanks
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foodbanks.db'
db = SQLAlchemy(app)
class foodbanks(db.Model):
    __tablename__ = 'foodbanks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable="false")
    adress = db.Column(db.String(120), unique=True, nullable="false")
    lattitude = db.Column(db.Float(50), unique=True, nullable="false")
    longitude = db.Column(db.Float(50), unique=True, nullable="false")
    uuid_ = db.Column(db.VARCHAR(36), unique=True, nullable="false")
    def __repr__(self):
        return '<Name> %r>' % self.id
#default route
@app.route("/")
def home():
    return render_template("index.php", response=response)
#Will return the current Json response
@app.route("/random")
def callback():
    return json.dumps(getspreadsheetinfo())

#will change response every 30sec

def get_lat_long(adress):
    #make basic query to google maps
    data = gmaps_key.geocode(adress)
    latitude = data[0]['geometry']['location']['lat'] 
    longitude = data[0]['geometry']['location']['lng'] 
    return latitude, longitude
def getspreadsheetinfo():
    #load sheet
    sheet = client.open("Marihacks2021").sheet1
    data = sheet.get_all_records()
    updated_list = []
    #create new response body with lat, long and uuid
    for obj in data:
        food_bank_name = obj["Name"]
        adress = obj["Address"]
        phone_number = obj["Phone"]
        #Check if we already fetched long amd lat from a certain foodbank, saves nedless requests
        if foodbanks.query.filter_by(name=food_bank_name).count() == 1:
            foodbank_data = foodbanks.query.filter_by(name=food_bank_name).first()
            uuid_ = foodbank_data.uuid_
            longitude = foodbank_data.longitude
            latitude = foodbank_data.lattitude
            print(longitude, latitude, "Entry already present")
        else:    
            uuid_ = uuid.uuid4()
            latitude, longitude = get_lat_long(adress)
            try:
                test_foodbank = foodbanks(name=food_bank_name, adress=adress,lattitude=latitude,longitude=longitude, uuid_ = str(uuid_))
                db.session.add(test_foodbank)
                db.session.commit()
                print("worked")
            except:
                db.session.rollback()
                print("unlucky")
                raise
            finally:
                db.session.close()
        #Check if within a certain range from Montreal, about 56km
        if(latitude <= 45 or latitude >= 46 or longitude <= -81 or longitude >= -73):
            print("Outside of Montreal")
            pass
        else:
            object1 = {
                "id": str(uuid_),
                "name": food_bank_name,
                "full_adress": adress,
                "lat": latitude,
                "long": longitude,
                "phoneNumber": phone_number
            }
            updated_list.append(object1)
    return updated_list
#Response will be changed every 30sec to save needless spam
response = getspreadsheetinfo()

@app.route("/getfoodbanks")
def getfoodbanks():
    return json.dumps(response)
#This will change the response value every 30sec on a different thread
def run_continuously(interval=1):
    cease_continuous_run = threading.Event()
    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)
    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run

def background_job():
    global response
    response = getspreadsheetinfo()
    print("response updated")
schedule.every(10).seconds.do(background_job)
# Start the background thread
stop_run_continuously = run_continuously()      

@app.route("/editor")
def editor():
    return render_template("editor.php")
@app.route("/inventory")
def inventory():
    return render_template("inventory.php")

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
