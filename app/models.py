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


#

# from hashlib import md5
# from werkzeug.security import generate_password_hash, check_password_hash
# from datetime import datetime
# from flask_login import UserMixin
# from app import db, login
#
#
# followers = db.Table('followers',
#                      db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
#                      db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
#                      )
#
# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     password_hash = db.Column(db.String(120))
#     posts = db.relationship('Post', backref='author', lazy='dynamic')
#     about_me = db.Column(db.String(140))
#     last_seen = db.Column(db.DateTime, default=datetime.utcnow)
#     followed = db.relationship('User', secondary=followers,
#                                primaryjoin=(followers.c.follower_id == id),
#                                secondaryjoin=(followers.c.followed_id == id),
#                                backref=db.backref('followers', lazy='dynamic'), lazy='dynamic'
#                                )
#
#     def __repr__(self):
#         return '<User {}>'.format(self.username)
#
#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)
#
#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)
#
#     def avatar(self, size):
#         digest = md5(self.email.lower().encode('utf-8')).hexdigest()
#         return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)
#
#     def follow(self, user):
#         if not self.is_following(user):
#             self.followed.append(user)
#
#     def unfollow(self, user):
#         if self.is_following(user):
#             self.followed.remove(user)
#
#     def is_following(self, user):
#         return self.followed.filter(
#             followers.c.followed_id == user.id).count() > 0
#
#     def followed_posts(self):
#         followed = Post.query.join(followers, followers.c.followed_id == Post.user_id).filter(followers.c.follower_id
#                                                                                               == self.id)
#         own = Post.query.filter_by(user_id=self.id)
#         return followed.union(own).order_by(Post.timestamp.desc())
#
# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.String(140))
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#     def __repr__(self):
#         return '<Post {}>'.format(self.body)
#
#
# @login.user_loader
# def load_user(id):
#     return User.query.get(int(id))
