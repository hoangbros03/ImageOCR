from flask import Flask
# from views import views
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app= Flask (__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100), nullable=False)
    views= db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"Video (name ={name}, views = {views}, likes = {likes})"


video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required=True)
video_put_args.add_argument("view", type=int, help="view of the video", required=True)
video_put_args.add_argument("likes", type=int, help="likes of the video",  required=True)

Resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "views": fields.Integer,
    "likes": fields.Integer
}

names = {"hoang":{"age":19, "gender": "male"},
         "testing":{"age":16,"gender":"makle"}}


class Video(Resource):
    @marshal_with(Resource_fields)
    def get(self,video_id):
        result= VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="could not find video id")
        return result
    
    @marshal_with(Resource_fields)
    def put(self,video_id):
        args = video_put_args.parse_args()
        result= VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Video id taken...")
        

        Video = VideoModel(id=video_id, name = args['name'], views= args['view'], likes = args['likes'])
        db.session.add(Video)
        db.session.commit()
        
        return Video,201
    def delete(self, video_id):
      
        del videos[video_id]
        return {"data": "ok"}, 204

class HelloWord(Resource):
    def get(self, name,test):
        return {"data":names[name]}
    def post(self, name, test):
        return {"data":"Hello World"}
    
api.add_resource(HelloWord, "/helloworld/<string:name>/<int:test>")
api.add_resource(Video, "/video/<int:video_id>")


if __name__ == "__main__":
    app.run(debug=True, port = 8000)
    