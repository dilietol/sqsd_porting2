#!/usr/bin/python3
"""
Very simple HTTP server in python.

Send a POST request::
    curl -d {\"key\":\"value\"} -H "Content-Type: application/json" -X POST "http://localhost:5000/employees"

"""
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

class Employees(Resource):

    def post(self):
        if(request.is_json):
            print("Json Request:")
            print(request.json)
        print("Data Request:")
        print(request.data)
        print("Remote Addr:")
        print(request.remote_addr)
        print(request.form)
        print("Headers:")
        print(request.headers)
        return {'status': 'success'}


class Tracks(Resource):
    def post(self):
        print(request.json)
        return {'status': 'success'}


app = Flask(__name__)
api = Api(app)

api.add_resource(Employees, '/employees')  # Route_1
api.add_resource(Tracks, '/tracks')  # Route_2

if __name__ == '__main__':
    app.run()