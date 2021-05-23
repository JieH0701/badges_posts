from flask_restful import Resource, reqparse
from models.badge_model import BadgeModel


class Badge(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'id',
        type=int,
        required=True,
        help='Every course calculation needs a date')
    parser.add_argument(
        'user_id',
        type=int,
        required=True,
        help='Every course calculation needs a user_id')
    parser.add_argument(
        'name',
        type=str,
        required=True,
        help='Every badge needs a name')
    parser.add_argument(
        'date',
        type=str,
        required=True,
        help='Every badge needs a date')
    parser.add_argument(
        'class_id',
        type=int,
        required=True,
        help='Every badge needs a class_id')
    parser.add_argument(
        'tag_based',
        type=str,
        required=True,
        help='Every badge needs a tag_based')

    def get(self, name):
        bagde = BadgeModel.find_by_name(name)
        if bagde:
            return bagde
        else:
            return {'message': "An badge with name '{}' hasn't saved in Database.".format(name)}, 404

    def post(self, name):
        data = Badge.parser.parse_args()
        if BadgeModel.find_by_id(data['id']):
            return {'message': "A badge with this id already exisits"}
        bagde = BadgeModel(**data)
        try:
            bagde.save_to_db(), 201
            return {'message': "A new badge is created"}
        except:
            return {'message': "An error occurred inserting the bagde with name '{}'.".format(name)}, 50


class BadgeLists(Resource):
    def get(self):
        return {'badges': [badge.json() for badge in BadgeModel.query.all()]}
