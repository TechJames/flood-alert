from flask import Flask, render_template
from app import app
import rest
import datetime
from alert import Alert

@app.route('/')
def main():
    data = rest.get_floods()
    
    alert_list = []

    for i in range(len(data["items"])):
        level = data["items"][i]["severityLevel"]
        river_sea = data["items"][i]["floodArea"]["riverOrSea"]
        county = data["items"][i]["floodArea"]["county"]
        polygon = data["items"][i]["floodArea"]["polygon"]
        region = data["items"][i]["eaRegionName"]
        message = data["items"][i]["description"]

        # populate Alert class with JSON response
        alert = Alert(level, river_sea, county, region, message, polygon)
        alert_list.append(alert)


    fmtdate = datetime.datetime.now().strftime('%c')
    
    return render_template('alert.html', alerts = alert_list, fmtdate = fmtdate)