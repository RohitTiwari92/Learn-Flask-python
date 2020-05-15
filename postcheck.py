from flask_restful import Resource,request
import json
from tokencheck import checktoken

class postcheck(Resource):
    @checktoken.token_required
    def post(self):
        try:
            req_data = request.get_json()
            name= req_data['data']['name']
            classrank = req_data['data']['classrank']
            return name
        except:
            return "error"



