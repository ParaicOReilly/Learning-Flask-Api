from flask import Flask
from flask_restful import Api, Resource,reqparse, abort

app = Flask(__name__)
# wrapping app in an api - initialising a restful api
api = Api(app)

# # Example: creating a resource
# class HelloWorld(Resource):
#     def get(self):
#         return {"data":"Hello World"}
# api.add_resource(HelloWorld, "/helloworld")

videos = {}

# argument parser 
# these arguments if these are not in the specified request where this is called it sends an error automatically
# required = True makes it throw an error if arg is missing/wrong
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required = True)
video_put_args.add_argument("views", type=int, help="Views on the video", required = True)
video_put_args.add_argument("likes", type=int, help="Likes on the video", required = True)

def abort_if_no_id(video_id):
    if video_id not in videos:
        abort(404, message="Video not found")

def abort_if_id_exists(video_id):
    if video_id in videos:
        abort(409, message="Video id already exists")

class Video(Resource):
    # returns information stored in dict for the video id
    def get(self, video_id):
        abort_if_no_id(video_id)
        return videos[video_id]
    
    def put(self, video_id):
        abort_if_id_exists(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201
    
    def delete(self,video_id):
        abort_if_no_id(video_id)
        if video_id in videos:
            del(videos[video_id])
            return 'video deleted', 204
        
#<> lets you specify types 
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)