
from flask_restplus import Resource
from flask import request,jsonify, make_response
import json
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask
import jwt
import datetime
from flask_jwt import JWT, jwt_required, current_identity
from  __init__  import *
from flask_restplus import reqparse

class login(Resource):
    @api.header('Content-Type', 'Type', required=True)
    @api.header('Authorization', 'Login', required=True)
    def get(self):
        auth =request.authorization
        if not auth or not auth.username or not auth.password :
            return make_response('could not verify')
        if auth.username == 'rohit' and  check_password_hash(generate_password_hash('tiwari',method='sha256') , auth.password):
            #how to import app in other files ?
            token = jwt.encode({'public_id':'1','exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=30)},'secret')
            #token = JWT({'public_id': '1', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},'secret')
            return  jsonify({'token': token.decode('UTF-8') })
            #return  jsonify({'token': 'heelo' })

        return make_response('could not verify')




