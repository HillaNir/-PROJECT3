from flask import Flask,request
from flask_restful import Api
from flask_cors import CORS
from config import DBUSER,DBHOST,DBPASS
from db import db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{DBUSER}:{DBPASS}@{DBHOST}/postgres'
app.config['SECRET_KEY'] = 'yt32fffdyju75h456h456y4yu46u576i'
CORS(app)

db.init_app(app)
api = Api(app)



from controllers.dishes import DishAll
from controllers.categories import CategoryAll

api.add_resource(CategoryAll,'/categories')
api.add_resource(DishAll,'/dishes')



if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")