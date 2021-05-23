from db import db


class BadgeModel(db.Model):
    __tablename__ = 'badges'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    name = db.Column(db.String(80))
    date = db.Column(db.String(80))
    class_id = db.Column(db.Integer)
    tag_based = db.Column(db.String(80))

    # user_id_relationship = db.relationship('PostModel', foreign_keys=user_id)

    def __init__(self, id, user_id, name, date, class_id, tag_based):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.date = date
        self.class_id = class_id
        self.tag_based = tag_based

    def json(self):
        return {'id': self.id, 'usr_id': self.user_id, 'name': self.name, 'date': self.date, 'class_id': self.class_id,
                'tag_based': self.tag_based}

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_name(cls, name):
        return {'badges': [badge.json() for badge in cls.query.filter_by(name=name).all()]}

    @classmethod
    def find_by_user_id(cls, user_id):
        return {'badges': [badge.json() for badge in cls.query.filter_by(usr_id=user_id).all()]}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
