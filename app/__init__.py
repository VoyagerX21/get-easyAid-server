from flask import Flask, jsonify
from flask_cors import CORS
from app.utils.errors import AppError
from app.extensions import db, migrate
from app.config.config import Config
from flask_smorest import Api

def create_app(config=Config):

    app = Flask(__name__)
    CORS(app)

    app.config.from_object(config)

    api = Api(app)

    from app.routes.getallcourses import getallcourses_bp
    from app.routes.search import search_bp
    from app.routes.submit import submit_bp
    from app.routes.getprompt import getprompt_bp
    from app.routes.regenerate import regen_bp
    from app.routes.job import job_bp
    from app.routes.health import health_bp
    from app.models.courses import Course
    from app.models.specs import Spec

    api.register_blueprint(getallcourses_bp, url_prefix="/getAllCourses")
    api.register_blueprint(search_bp, url_prefix="/search")
    api.register_blueprint(submit_bp, url_prefix="/submit")
    api.register_blueprint(getprompt_bp, url_prefix="/GetPrompt")
    api.register_blueprint(job_bp, url_prefix="/job")
    api.register_blueprint(health_bp, url_prefix="/health")
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    @app.errorhandler(AppError)
    def throwAppError(error):
        return jsonify({
            "success": False,
            "msg": error.msg
        }), error.code

    return app