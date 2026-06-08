from flask import Flask, jsonify
from flask_cors import CORS
from app.utils.errors import AppError

def create_app():

    app = Flask(__name__)
    CORS(app)

    from app.routes.getallcourses import getallcourses_bp
    from app.routes.search import search_bp
    from app.routes.submit import submit_bp
    from app.routes.getprompt import getprompt_bp
    from app.routes.regenerate import regen_bp

    app.register_blueprint(getallcourses_bp, url_prefix="/getAllCourses")
    app.register_blueprint(search_bp, url_prefix="/search")
    app.register_blueprint(submit_bp, url_prefix="/submit")
    app.register_blueprint(getprompt_bp, url_prefix="/GetPrompt")
    app.register_blueprint(regen_bp, url_prefix="/regenerate")

    @app.get("/")
    def getHome():
        return jsonify({
            "msg": "API running"
        }), 200
    
    @app.errorhandler(AppError)
    def throwAppError(error):
        return jsonify({
            "success": False,
            "msg": error.msg
        }), error.code

    return app