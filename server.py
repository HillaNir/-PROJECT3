from flask import Flask,request
from flask_restful import Api
from flask_cors import CORS
from config import DBUSER,DBHOST,DBPASS
from db import db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{DBUSER}:{DBPASS}@{DBHOST}/postgres'
app.config['SECRET_KEY'] = 'yt32fffdyju75h456h456y4yu46u576i'


db.init_app(app)
api = Api(app)

CORS(app)

from controllers.dishes import DishAll,DishOne #,DishFilter
from controllers.categories import CategoryAll,CategoryOne

api.add_resource(DishAll,'/dishes')
api.add_resource(DishOne,'/dishes/<int:id>')
api.add_resource(CategoryAll,'/categories')
api.add_resource(CategoryOne,'/categories/<int:id>')
# api.add_resource(DishFilter,'/dishes/category/<int:category_id>')


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")