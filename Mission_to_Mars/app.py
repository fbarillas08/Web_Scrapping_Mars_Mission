## Flask Application that scrapes Mars Website

# Importing Required Libraries
import jsonify
from pathlib import Path

from flask import Flask, redirect, url_for
from flask import render_template
from flask_pymongo import PyMongo

import os
import scrape_all



# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import inspect

app=Flask(__name__)
app.config["MONGO_URI"]= 'mongodb://localhost:27017/marsnews_db'

mongo = PyMongo(app)


@app.route("/")
def home():
    mars = mongo.db.items.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    db = mongo.db.marsnews_db
    marsdata = mission_to_mars
    return redirect("/",code=302)


if __name__ == "__main__":
    app.run(debug=False)


