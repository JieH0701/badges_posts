from db import db


class PostModel(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    post_type_id = db.Column(db.Integer)
    accepted_answer_id = db.Column(db.Integer)
    parent_id = db.Column(db.Integer)
    creation_date = db.Column(db.String(80))
    deletion_date = db.Column(db.String(80))
    score = db.Column(db.Integer)
    view_count = db.Column(db.Integer)
    owner_user_id = db.Column(db.Integer)
    ower_display_name = db.Column(db.String(80))
    last_editor_user_id = db.Column(db.Integer)
    last_editor_user_name = db.Column(db.String(80))
    last_editor_date = db.Column(db.String(80))
    last_activity_date = db.Column(db.String(80))
    answer_count = db.Column(db.Integer)
    comment_count = db.Column(db.Integer)
    closed_date = db.Column(db.String(80))
    community_owned_date = db.Column(db.String(80))

    def __init__(self, **kwargs):
        valid_keys = ["id", "post_type_id", "accepted_answer_id", "parent_id", "creation_date", "deletion_date",
                      "score", "view_count", "owner_user_id", "ower_display_name", "last_editor_user_id",
                      "last_editor_user_name", "last_editor_date", "last_activity_date",
                      "answer_count", "comment_count", "closed_date", "community_owned_date"]
        for key in valid_keys:
            if kwargs.get(key):
                setattr(self, key, kwargs.get(key))

    def json(self):
        return {'id': self.id, 'creation_date': self.creation_date, 'owner_user_id': self.owner_user_id,
                'last_editor_user_id': self.last_editor_user_id, 'last_editor_date': self.last_editor_date,
                'answer_count': self.answer_count, 'comment_count': self.comment_count, 'closed_date': self.closed_date}

    @classmethod
    def find_by_user_id(cls, user_id):
        return {user_id: [post.json() for post in cls.query.filter_by(owner_user_id=user_id).all()]}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
