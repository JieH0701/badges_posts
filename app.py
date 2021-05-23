from flask import Flask, Response
from flask_restful import Api
from db import db
from resources.badge import BadgeLists, Badge
from resources.post import PostList, Post, TotalAnswers

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.route("/")
def hello():
    return Response("Hi from your Flask app running in your Docker container!")


api.add_resource(PostList, '/posts')
api.add_resource(Post, '/post/<int:user_id>')
api.add_resource(BadgeLists, '/badges')
api.add_resource(Badge, '/badge/<string:name>')
api.add_resource(TotalAnswers, '/totalanswers/<string:bagde>')

if __name__ == '__main__':
    db.init_app(app)
    app.run("0.0.0.0", port=80, debug=True)
