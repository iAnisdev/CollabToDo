import mysql.connector
from flask import Flask , g
from .config import Config
from .routes.index import bp as index_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    def connect_db():
        return mysql.connector.connect(
            host=app.config['DB_HOST'],
            user=app.config['DB_USER'],
            password=app.config['DB_PASSWORD'],
            database=app.config['DB_NAME'],
            port=app.config['DB_PORT']
        )
    
    @app.before_request
    def before_request():
        g.db = connect_db()

    @app.teardown_request
    def teardown_request(exception):
        db = getattr(g, 'db', None)
        if db is not None:
            db.close()
    
    app.register_blueprint(index_bp)

    return app