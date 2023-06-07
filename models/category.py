from db import db

class Category(db.Model):
    __tablename__ = "orders_category"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200))
    imageUrl = db.Column(db.Text)
    dishes = db.relationship('Dish', backref='orders_category') # שדה וירטואלי

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "imageUrl": self.imageUrl,
            "dishes": [dish.serialize() for dish in self.dishes]
        }
    
    


# שמות זהים לטבלאות של פוסטגרס- עשיתי
# לתת שם לטבלה- עשיתי
# 24.5 MATKONIM API DOCKER