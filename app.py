from os import environ
from flask import Flask, render_template
import pickle
import os.path
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import requests
import googlemaps
from apscheduler.schedulers.blocking import BlockingScheduler
from flask_sqlalchemy import SQLAlchemy
#authentication with google API
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
#authentication for maps
client = gspread.authorize(creds)
gmaps_key = googlemaps.Client(key = "AIzaSyA_ojPMG7H6WxeUH_nwv6xLrTF_QVVQNN0")
#Flask app
app = Flask(__name__)

#SQL database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foodbanks.db'
#db = SQLAlchemy(app)
#class foodbanks(db.Model):
 #   __tablename__ = 'foodbanks'
 #   id = db.Column(db.Integer, primary_key=True)
 #   name = db.Column(db.String(50), unique=True, nullable="false")
 #   adress = db.Column(db.String(120), unique=True, nullable="false")
 #   lattitude = db.Column(db.Float(50), unique=True, nullable="false")
 #  def __repr__(self):
 #       return '<Name> %r>' % self.id

#Response will be changed every 30sec so save needless spam
response = []

#base route
@app.route("/")
def home():
    return render_template("index.php")
#Will return the current Json response
@app.route("/getfoodbanks")
def getfoodbanks():
    return response

@app.route("/random")
def callback():
    return json.dumps(getspreadsheetinfo())

#will change response every 30sec


def getspreadsheetinfo():
    #load sheet
    sheet = client.open("Marihacks2021").sheet1
    data = sheet.get_all_records()
    response = []
    #create new response body with lat, long and uuid
    for obj in data:
        food_bank_name = obj["Name"]
        adress = obj["Address"]
        #Check if we already fetched long amd lat from a certain foodbank, saves nedless requests
#        if adress in foodbanks.adress.query.all():
#            longitude = foodbanks.longitude.filter(foodbanks.name == food_bank_name).first()
#            lattitude = foodbanks.lattitude.filter(foodbanks.name == food_bank_name).first()
#        else:    
        longitude, lattitude = get_lat_long(adress)
        phone_number = obj["Phone"]
        #Check if within a certain range from Montreal, about 56km
        if(lattitude <= 45 or lattitude >= 46 or longitude <= -74 or longitude >= -73):
            pass
        else:
            object1 = {
            #    "id": uuid,
                "name": food_bank_name,
                "full_adress": adress,
                "lat": lattitude,
                "long": longitude,
                "phoneNumber": phone_number
            }
            response.append(object1)
    return response        
def get_lat_long(adress):
    #make basic query to google maps
    data = gmaps_key.geocode(adress)
    latitude = data[0]['geometry']['location']['lat'] 
    longitude = data[0]['geometry']['location']['lng'] 
    return latitude, longitude
@app.route("/editor")
def editor():
    render_template("editor.php")
@app.route("/inventory")
def editor():
    render_template("inventory.php")
if __name__ == '__main__':
    app.run(threaded=True, port=5000)
