from tokencheck import checktoken
from flask import request,jsonify
import Usermodel
from __init__ import *
from flask_restplus import Resource,fields



class userop(Resource):
    @checktoken.token_required
    def get(self,current_user):
        qusers=Usermodel.flaskapiuser.query.all()
        output= []
        for userobj in qusers:
            user_data={}
            user_data['name']=userobj.user_name
            user_data['email']=userobj.email
            output.append(user_data)
        return jsonify({'users':output})

    resource_fields = api.model('Resource', {
        'name': fields.String,
        'email': fields.String,
        'password': fields.String,
    })
    @api.expect(resource_fields)
    @checktoken.token_required
    def post(self,current_user):
        data = request.get_json()
        user =  Usermodel.flaskapiuser(user_name=data['name'],email=data['email'],password=data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'message':'New user created'})

    resource_put_fields = api.model('Resource1', {
        'uid': fields.Integer,
        'newname': fields.String,
    })
    @api.expect(resource_put_fields)
    @checktoken.token_required
    def put(self,current_user):
        Puid = request.args.get('uid')
        Pnewname = request.args.get('newname')
        quser=Usermodel.flaskapiuser.query.filter_by(id=Puid).first()
        quser.user_name=Pnewname
        db.session.commit()
        return jsonify({'Message':'user updated'})

    resource_Delete_fields = api.model('Resource2', {
        'uid': fields.Integer,
    })
    @api.expect(resource_Delete_fields)
    @checktoken.token_required
    def delete(self,current_user):
        Puid = request.args.get('uid')
        quser = Usermodel.flaskapiuser.query.filter_by(id=Puid).first()
        db.session.delete(quser)
        db.session.commit()
        return jsonify({'Message':'user Deleted'})