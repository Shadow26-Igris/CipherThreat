from flask import Flask
from flask_bcrypt import Bcrypt
from app.config import Config
from app.utils.db import get_db_connection
from app.routes import auth_routes, complaint_routes , scan_routes , vulnerability_scan_routes


bcrypt = Bcrypt()




def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = 'secret'  # Add a secret key for session and flash messages
    
    bcrypt.init_app(app)
    # Import and register blueprints
    from app.routes.main_routes import main_routes
    from app.routes.news_routes import news_routes
    app.register_blueprint(main_routes, url_prefix='/')
    app.register_blueprint(news_routes, url_prefix='/news')
    app.register_blueprint(auth_routes, url_prefix='/auth')
    app.register_blueprint(complaint_routes, url_prefix='/complaint')
    app.register_blueprint(scan_routes, url_prefix='/scan')
    app.register_blueprint(vulnerability_scan_routes, url_prefix='/vulnerability_scan')
    return app
