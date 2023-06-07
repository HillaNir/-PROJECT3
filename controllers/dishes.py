from flask import request
from flask_restful import Resource
from models.dish import Dish


class DishAll(Resource):
    def get(self):
        dishes = Dish.query.filter_by(**request.args).all()
        return [dish.serialize() for dish in dishes][::-1]


class DishOne(Resource):
    def get(self,id):
        dish = Dish.query.get(id)
        return dish.serialize()

    
# class DishFilter(Resource):
#     def get(self,category_id):
#         dishes = Dish.query.filter_by(category_id=category_id).all()
#         return [dish.serialize() for dish in dishes]