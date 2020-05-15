from flask_restplus import Resource
from flask import request,jsonify
from functools import wraps
import jwt
from __init__ import *

class checktoken(Resource):
    @api.header('x-access-token', 'JWT token', required=True)
    @api.header('Content-Type', 'Type', required=True)
    def token_required(f):
        @wraps(f)
        def decorated(*args,**kwargs):
            token = None

            if 'x-access-token' in request.headers:
                token=request.headers['x-access-token']

            if not token :
                return jsonify({'message':'token is missing'})

            try:
                data = jwt.decode(token,'secret')
                current_user=data['public_id']
            except:
                return jsonify({'message':'invalid token'})
            return f(current_user,*args,**kwargs)

        return decorated

