from  getquckfindcodeDC import getquckfindcodeDC
from getquckUnioncodeDC import getquckUnioncodeDC
from postcheck import postcheck
from usercurd import userop
from Gettoken import login
from __init__ import  *



api.add_resource(getquckfindcodeDC,"/getquckfindcodeDC")
api.add_resource(getquckUnioncodeDC,'/getquckUnioncodeDC')
api.add_resource(postcheck,'/postcheck')
api.add_resource(login,'/login')
api.add_resource(userop,'/user')



if __name__=='__main__':
    app.run(debug=True)