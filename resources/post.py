from flask_restful import Resource, reqparse
from models.post_model import PostModel
from toolkit.data_provision import get_total_answers


class Post(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'user_id',
        type=int,
        required=True,
        help='Every course calculation needs a user_id')

    def get(self, user_id):
        post = PostModel.find_by_user_id(user_id)
        if post:
            return post
        else:
            return {'message': "An post with user_id '{}' hasn't saved in Database.".format(user_id)}, 404


class PostList(Resource):
    def get(self):
        return {'posts': [post.json() for post in PostModel.query.all()]}


class TotalAnswers(Resource):
    def get(self, bagde):
        return {'total answers with bagde {}'.format(bagde): get_total_answers(bagde)}
