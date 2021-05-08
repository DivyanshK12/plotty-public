from flask import render_template, session, redirect, url_for, flash, jsonify, request, Response
from datetime import datetime, timedelta, date
from . import main
from .. import db
from ..models import Update
from .utils import *

@main.route('/')
def index():
    return render_template("index.html")

@main.route("/receiver", methods=["GET", "POST"])
def receiver():
    data = request.get_json(force = True)
    td = getdate()
    savedate = date(day=td.day, month=td.month, year=td.year)
    update = Update(user = data['user'], count = data['count'], date= savedate)
    db.session.add(update)
    db.session.commit()
    response = Response(status=200)
    return response

@main.route("/api/getuserdata/<user>")
def getuserdata(user):
    data = Update.query.filter_by(user=user).all()
    data = [i.json() for i in data]
    return jsonify(data)

@main.route("/api/getusers")
def getusers():
    data = Update.query.with_entities(Update.user).distinct().all()
    data = [dat.user for dat in data]
    return jsonify(data)

@main.route("/api/getdates")
def getdates():
    data = Update.query.with_entities(Update.date).distinct().all()
    data = [str(dat.date) for dat in data]
    return jsonify(data)

@main.route("/api/getdata")
def getdata():
    data = Update.query.with_entities(Update.user).distinct().all()
    resp = {}
    for dat in data :
        user = dat.user
        content = Update.query.filter_by(user=user).all()
        resp[user] = [{'x':str(c.date),'y':c.count} for c in content]
    return jsonify(resp)


def getdate():
    time = timedelta(hours=5, minutes=30)
    date = datetime.utcnow()+time
    return date