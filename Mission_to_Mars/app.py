## Flask Application that scrapes Mars Website

# Importing Required Libraries
import jsonify
from pathlib import Path

from flask import Flask, redirect, url_for
from flask import render_template

import os
import pymongo

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import inspect

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.marsnews_db
collection = db.items

articles = db.items.find()

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scrape")
def scrape():
    


if __name__ == "__main__":
    app.run(debug=True)


