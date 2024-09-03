from flask import Flask
from database import db
from serializers import mapping_serializer
from models import CRMMapping
from routes import mapping_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password123@localhost/mapping"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Register the mapping routes
app.register_blueprint(mapping_routes)

if __name__ == '__main__':
    app.run()
