from app import db


class Nonprofit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)
    description = db.Column(db.String, index=True)
    category = db.Column(db.String, index=True)
    location = db.Column(db.String, index=True)
    website = db.Column(db.String, index=True)
    phone = db.Column(db.Integer, index=True)
    email = db.Column(db.String, index=True)
    photo = db.Column(db.String)
    logo = db.Column(db.String)
    wishlist = db.relationship('Item', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Nonprofit {}>'.format(self.name)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)
    price = db.Column(db.Float(precision=2), index=True)
    photo = db.Column(db.String, index=True)
    nonprofit_id = db.Column(db.Integer, db.ForeignKey('nonprofit.id'))

    def __repr__(self):
        return '<Item {}>'.format(self.name)

