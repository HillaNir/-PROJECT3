from db import db


class Dish(db.Model):
    __tablename__ = "orders_dish"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200))
    price = db.Column(db.Integer)
    description = db.Column(db.Text)
    imageUrl = db.Column(db.Text)
    is_gluten_free = db.Column(db.Boolean)
    is_vegeterian = db.Column(db.Boolean)
    category_id = db.Column(db.Integer,db.ForeignKey('orders_category.id'),nullable=False)
    

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "imageUrl": self.imageUrl,
            "price": self.price,
            "category": self.orders_category.name
        }