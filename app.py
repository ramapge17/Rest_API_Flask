import os
#from typing_extensions import Required
from flask import Flask 
from flask_restful import Api
from flask_jwt import JWT
from security import autentication , identity
from resources.user import UserRegister
from resources.items import Item , ItemList
from resources.store import Store,StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS']=False
app.config['SQLALCHEMY_DATBASE_URI'] = os.environ.get('DATABASE_URL_1','sqlite:///data.db') 
app.secret_key = 'Jose'
api = Api(app)


jwt = JWT(app,autentication,identity)



api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList,'/stores')
api.add_resource(UserRegister,'/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()
    
    app.run(port=5000,debug=True)