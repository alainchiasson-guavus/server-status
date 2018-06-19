from flask import Flask, request, jsonify
from flask_restplus import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy
import mysql.connector as db
import json

import os

DATABASE_CREDENTIALS = {
   'host': os.environ['DATABASE_HOST'],
   'user': os.environ['DATABASE_USER'],
   'password': os.environ['DATABASE_PASSWORD'],
   'database': os.environ['DATABASE_NAME']
}

app = Flask(__name__)

os.environ['DATABASE_URL'] = "mysql://%s:%s@%s/%s" % (DATABASE_CREDENTIALS['user'], DATABASE_CREDENTIALS['password'], DATABASE_CREDENTIALS['host'], DATABASE_CREDENTIALS['database'])

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

api = Api(app)

class Servers(db.Model):
   __tablename__ = 'servers'

   id = db.Column(db.Integer, primary_key=True)
   servername = db.Column(db.String(255), unique=True)
   status = db.Column(db.String(10))

   def __init__(self, servername, email):
       self.servername = servername
       self.status = status

   def __repr__(self):
       return '<Server %r>' % self.servername

@api.route("/servers")
class serversIndex(Resource):

    def get(self):
        to_json = lambda server: {"id": server.id, "servername": server.servername, "status": server.status}
        return jsonify([to_json(server) for server in Servers.query.all()])


@api.route("/server/<id>")
class serverInfo(Resource):

    def get(self, id):
        to_json = lambda server: {"id": server.id, "servername": server.servername, "status": server.status}
        return jsonify([to_json(server) for server in Servers.query.filter( Servers.id == id )])


@api.route('/info')
class infoSimple(Resource):

    def get(self):
        return "Built with FlaskRESTplus"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
