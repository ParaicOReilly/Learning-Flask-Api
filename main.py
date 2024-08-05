from flask import Flask
from flask_restful import Api, Resource,reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# wrapping app in an api - initialising a restful api
api = Api(app)
# defining the location of the database - 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# wrapping app in database
db = SQLAlchemy(app)


# Need to create a Resource for storing videos

class Video_Model(db.Model):
    video_id = db.Column(db.Integer, primary_key=True)
    video_name = db.Column(db.String(100), nullable=False)
    video_likes = db.Column(db.Integer, nullable=False)
    video_views = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"Video(video_name = {self.video_name}, video_likes = {self.video_likes}, video_views = {self.video_views})"


# Don't run this multiple times 
# with app.app_context():
#     db.create_all()

# argument parser 
# these arguments if these are not in the specified request where this is called it sends an error automatically
# required = True makes it throw an error if arg is missing/wrong
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("video_name", type=str, help="Name of the video", required = True)
video_put_args.add_argument("video_views", type=int, help="Views on the video", required = True)
video_put_args.add_argument("video_likes", type=int, help="Likes on the video", required = True)

# call with marshall with and will serialise what the query returns in this JSON format
resource_fields = {
    'video_id' : fields.Integer,
    'video_name' : fields.String,
    'video_likes' : fields.Integer,
    'video_views' : fields.Integer
}
class Video(Resource):
    # returns information stored in dict for the video id
    @marshal_with(resource_fields)
    def get(self, video_id):
       res = Video_Model.query.get(video_id)
       if not res:
           abort(409, "Video not found.")
       return res
    
    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        res = Video_Model.query.get(video_id)
        if res:
            abort(409, message = "Video ID is in use.")
        video =  Video_Model(video_id = video_id, video_name = args['video_name'], video_likes = args['video_likes'], video_views = args['video_views'] )
        db.session.add(video)
        db.session.commit()
        return video, 201
    
    # def delete(self,video_id):
    #     abort_if_no_id(video_id)
    #     if video_id in videos:
    #         del(videos[video_id])
    #         return 'video deleted', 204
        
#<> lets you specify types 
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)