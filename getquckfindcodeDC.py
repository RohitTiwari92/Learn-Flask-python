from flask_restful import Resource
from flask import Flask, jsonify
from tokencheck import checktoken

class getquckfindcodeDC(Resource):
    @checktoken.token_required
    def get(self,current_user):
        f = open("QuickFInd_DC.py", "r")
        data = f.read()
        f.close()
        return jsonify({"Code": data})
