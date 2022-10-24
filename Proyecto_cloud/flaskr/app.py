from flaskr import create_app
from flask_restful import Api
from flask_jwt_extended import JWTManager


from .modelos import db
from .vistas import LoadAudio,DownloadAudio, TaskDetail

app = create_app('default')
app_context = app.app_context()
app_context.push()
api = Api(app)
api.init_app(app)

db.init_app(app)
db.create_all()

api.add_resource(LoadAudio, '/api/tasks')
api.add_resource(DownloadAudio, '/api/files/<string:filename>')
api.add_resource(TaskDetail, '/api/tasks/<int:id_task>')

jwt = JWTManager(app)
