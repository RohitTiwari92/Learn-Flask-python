from flask_restful import Resource
from flask import jsonify
from tokencheck import checktoken

class getquckUnioncodeDC(Resource):
    @checktoken.token_required
    def get(self,current_user):
        f = open("QuickUnion.py", "r")
        data = f.read()
        f.close()
        return jsonify({"Code": data})
